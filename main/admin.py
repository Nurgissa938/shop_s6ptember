from django.contrib import admin

from .models import Category, Product


# это декоратор, который регистрирует модель Category в административной панели Django.
@admin.register(Category)
# Это позволяет нам управлять категориями через административную панель.
class CategoryAdmin(admin.ModelAdmin):
    # это список полей, которые будут отображаться в списке категорий в административной панели.
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    # это словарь, который говорит Django, что поле slug должно быть автоматически заполнено на основе поля name при создании новой категории.


# это декоратор, который регистрирует модель Product в административной панели Django.
@admin.register(Product)
# Это позволяет нам управлять продуктами через административную панель.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    # это список полей, которые будут отображаться в списке продуктов в административной панели.
    list_filter = ["available", "created", "updated", "category"]
    # это список полей, по которым можно фильтровать продукты в административной панели.
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}
    # это словарь, который говорит Django, что поле slug должно быть автоматически заполнено на основе поля name при создании нового продукта.


# Register your models here.
