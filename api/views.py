from rest_framework.generics import ListAPIView

from api.serializers import FoodListSerializer
from api.models import FoodCategory

class Foods(ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.all()
