from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from agro_marketplace.buyers.forms import BuyersForm
from agro_marketplace.buyers.models import BuyerItems


def card_info_buyer(request, pk):
    item = get_object_or_404(BuyerItems, pk=pk)
    return render(request, 'buyers/card-info-buyers.html', {'item': item})


@login_required
def create_buyer(request):

    if request.method == 'POST':
        form = BuyersForm(request.POST, request.FILES)
        if form.is_valid():
            buyer_item = form.save(commit=False)
            buyer_item.profile = request.user.profile
            buyer_item.save()
            return redirect(reverse_lazy('dash'))
    else:
        form = BuyersForm()

    return render(request, 'buyers/buyers-form.html', {'buyer_form': form})
