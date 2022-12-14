from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Recipe
from .permissions import IsOwnerOrReadOnly
from .serializers import Recipeserializer


class RecipeList(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer


class RecipeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
