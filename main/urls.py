from django.urls import path
from . import views
# по идее сперва должен создаться views
app_name = "main"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    # если в URL есть category_slug, то вызывается функция product_list, которая отображает список товаров, отфильтрованных по категории
    path('<int:id>/<slug:slug>',
         views.product_detail, name='product_detail'),
    # если в URL есть id и slug, то вызывается функция product_detail, которая отображает подробную информацию о товаре
]
