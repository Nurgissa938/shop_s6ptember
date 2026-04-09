from django.shortcuts import render, get_object_or_404
from . models import Category, Product
# идет перед тем как прописать urls, так как там мы будем использовать views
# views - это функции, которые обрабатывают запросы от пользователей и возвращают ответы.
# Они принимают запросы, извлекают данные из базы данных, обрабатывают их и возвращают HTML-страницы или другие типы ответов.

# Create your views here.


# функция получает из базы данных все категории и все доступные товары, затем проверяет,
# передан ли параметр category_slug: если да, то находит соответствующую категорию (или выдаёт 404, если её нет)
# и фильтрует товары только по этой категории, после чего с помощью render передаёт в HTML-шаблон список категорий,
# выбранную категорию и отфильтрованные товары для отображения на странице.
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/products/list.html', {'category': category, 'categories': categories, 'products': products})

# request - это объект, который содержит информацию о запросе, который был отправлен пользователем.
# когда мы открываем страницу, браузер отправляет запрос к серверу, джанго его принимает и создает объект request,
# который содержит информацию о том, какой URL был запрошен, какие данные были отправлены и т.д.
