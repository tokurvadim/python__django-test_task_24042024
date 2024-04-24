from rest_framework import serializers

from .models import Food, FoodCategory




class IsPublishFoodSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(is_publish=True)
        if data:
            return super().to_representation(data)
        else:
            return super().to_representation([])



class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        list_serializer_class = IsPublishFoodSerializer
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')
        



class IsEmptyFoodListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        for food_category in data:
            is_publish_foods = Food.objects.filter(is_publish=True, category=food_category.id).count()
            if not is_publish_foods:
                data = data.exclude(name_ru=food_category.name_ru)
        return super().to_representation(data)
        



class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        list_serializer_class = IsEmptyFoodListSerializer
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
