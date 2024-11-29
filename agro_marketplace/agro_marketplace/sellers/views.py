from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from agro_marketplace.sellers.forms import SellersForm
from agro_marketplace.sellers.models import SellerItems


def card_info_sellers(request, pk):
    item = get_object_or_404(SellerItems, pk=pk)
    return render(request, 'sellers/card-info-sellers.html', {'item': item})


@login_required
def create_seller(request):

    if request.method == 'POST':
        form = SellersForm(request.POST, request.FILES)
        if form.is_valid():
            seller_item = form.save(commit=False)
            seller_item.profile = request.user.profile
            seller_item.save()
            return redirect(reverse_lazy('dash'))
    else:
        form = SellersForm()

    return render(request, 'sellers/sellers-form.html', {'seller_form': form})


