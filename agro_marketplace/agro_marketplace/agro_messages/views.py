from datetime import datetime

import pytz
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.utils import timezone
from .forms import MessageForm
from .models import Message, MessageStatus
from ..accounts.models import AppUser
from ..buyers.models import BuyerItems
from ..sellers.models import SellerItems


sofia_tz = pytz.timezone('Europe/Sofia')
current_time = now().astimezone(sofia_tz)


def send_message(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')
    recipient = get_object_or_404(AppUser, pk=pk) if pk else None
    product = None

    if pk:
        try:
            product = SellerItems.objects.get(profile__user=pk)
        except SellerItems.DoesNotExist:
            try:
                product = BuyerItems.objects.get(profile__user=pk)
            except BuyerItems.DoesNotExist:
                product = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            MessageStatus.objects.create(message=message, profile=recipient)
            return redirect('message-inbox')
    else:
        form = MessageForm()

    return render(request, 'messages/message-send.html', {'form': form,
                                                          'recipient': recipient, 'product': product})


def read_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    current_user = request.user
    read_status, created = MessageStatus.objects.get_or_create(
        message=message, profile=current_user
    )
    read_status.mark_as_read()
    return render(request, 'messages/message-read.html', {'message': message})


@login_required
def reply_message(request, pk):
    parent_message = get_object_or_404(
        Message,
        Q(pk=pk) & (Q(sender=request.user) | Q(recipient=request.user))
    )

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.recipient = (
                parent_message.sender if parent_message.recipient == request.user else parent_message.recipient
            )

            if not parent_message.title.startswith("Re:"):
                reply.title = f"Re: {parent_message.title}"
            else:
                reply.title = parent_message.title

            reply.parent_message = parent_message
            reply.save()

            MessageStatus.objects.create(message=reply, profile=reply.recipient)

            return redirect('message-inbox')
        else:
            print("Form errors:", form.errors)  # Debugging output
    else:
        # Prepopulate the form fields with the parent message details
        # Check if "Re:" is already in the title before adding it
        title = parent_message.title if parent_message.title and parent_message.title.startswith(
            "Re:") else f"Re: {parent_message.title}"

        form = MessageForm(initial={
            'title': title,
            'body': (
                f"\n\n--- Replying to message from {parent_message.sender.username} on "
                f"{parent_message.timestamp:%Y-%m-%d %H:%M} ---\n{parent_message.body} "
            ),
        })

    return render(
        request,
        'messages/reply_message.html',
        {
            'form': form,
            'parent_message': parent_message,
        }
    )


@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    user_profile = request.user

    try:
        status = message.statuses.get(profile=user_profile)
    except MessageStatus.DoesNotExist:
        return HttpResponse("You are not allowed to delete this message.", status=403)

    if request.method == 'POST':
        status.is_deleted = True
        status.save()

        all_deleted = message.statuses.filter(is_deleted=False).count() == 0
        if all_deleted:
            message.delete()

        return redirect('message-inbox')

    return render(request, 'messages/message-delete.html', {'message': message})


@login_required
def message_inbox(request):
    filter_type = request.GET.get('filter', 'inbox')
    user = request.user

    base_query = Message.objects.filter(
        Q(sender=user) | Q(recipient=user)
    ).select_related('sender', 'recipient').prefetch_related('statuses')

    if filter_type == 'unread':
        # Unread messages for the recipient
        messages = base_query.filter(
            recipient=user,
            statuses__profile=user,
            statuses__is_read=False,
            statuses__is_deleted=False
        ).distinct().order_by('-timestamp')
    elif filter_type == 'sent':
        messages = base_query.filter(
            sender=user
        ).exclude(
            statuses__profile=user, statuses__is_deleted=True
        ).distinct().order_by('-timestamp')
    elif filter_type == 'all':
        messages = base_query.exclude(
            statuses__profile=user, statuses__is_deleted=True
        ).distinct().order_by('-timestamp')
    else:
        messages = base_query.filter(
            recipient=user,
            statuses__profile=user,
            statuses__is_deleted=False
        ).distinct().order_by('-timestamp')

    paginator = Paginator(messages, 5)  # Show 5 messages per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'messages': page_obj,
        'filter_type': filter_type
    }

    return render(request, 'messages/message-inbox.html', context)
