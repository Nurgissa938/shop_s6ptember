"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls', namespace='main')),
    # namespace='main' - это позволяет нам использовать имена URL-адресов из приложения main в других местах нашего проекта, например, в шаблонах, без конфликтов с именами URL-адресов из других приложений.
    # В данном случае мы включаем URL-адреса из приложения main.
    # path('', include('main.urls')) - это говорит Django, что все URL-адреса, которые начинаются с '', должны быть обработаны URL-адресами из приложения main.
]
