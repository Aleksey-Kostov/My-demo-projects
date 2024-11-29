from django import template

from ..models import Message, MessageStatus

register = template.Library()


@register.simple_tag
def message_counts(user):
    """
    Returns counts of messages for the given user, including unread, inbox, sent, and all messages.
    """
    # Unread messages (received, not deleted, and not read)
    unread_count = MessageStatus.objects.filter(
        profile=user,
        is_read=False,
        is_deleted=False
    ).count()

    # Inbox messages (received and not deleted)
    inbox_count = Message.objects.filter(
        recipient=user,
        statuses__profile=user,
        statuses__is_deleted=False
    ).distinct().count()

    # Sent messages (sent by the user and not marked as deleted)
    sent_count = Message.objects.filter(
        sender=user
    ).exclude(
        statuses__profile=user, statuses__is_deleted=True
    ).distinct().count()

    # All messages (received or sent, excluding deleted ones)
    all_count = Message.objects.exclude(
            statuses__profile=user, statuses__is_deleted=True
        ).distinct().count()

    return {
        'unread_count': unread_count,
        'inbox_count': inbox_count,
        'sent_count': sent_count,
        'all_count': all_count,
    }


@register.simple_tag
def message_read_status(message, user):
    """
    Returns the read status ('read' or 'unread') of a specific message for the given user.
    """
    status = MessageStatus.objects.filter(message=message, profile=user, is_deleted=False).first()
    return 'read' if status and status.is_read else 'unread'
