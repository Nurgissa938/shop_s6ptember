from django.urls import path
from . import views
# по идее сперва должен создаться views
app_name = "main"

urlpatterns = [
    path('', views.product_list, name='product_list'),
]
