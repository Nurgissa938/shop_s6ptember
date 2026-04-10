from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        # это словарь, который содержит очищенные данные из формы.
        cd = form.cleaned_data
        # Когда мы вызываем form.is_valid(), Django проверяет, что данные, введенные пользователем, соответствуют требованиям, которые мы указали в форме (например, что quantity - это число от 1 до 20)
        # Если данные валидны, то мы можем получить их из form.cleaned_data.
        # В нашем случае, cd будет содержать ключи 'quantity' и 'override', которые мы определили в CartAddProductForm.
        cart.add(product=product,
                 quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})
