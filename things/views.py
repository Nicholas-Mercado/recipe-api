from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from .serializers import Recipeserializer


class ThingList(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = Recipeserializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = Recipeserializer
