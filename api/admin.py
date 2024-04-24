from django.contrib import admin

from api.models import Food, FoodCategory

@admin.register(Food)
class Food(admin.ModelAdmin):
    pass

@admin.register(FoodCategory)
class FoodCategory(admin.ModelAdmin):
    pass