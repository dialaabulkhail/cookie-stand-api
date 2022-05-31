from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStands
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandserializer


class CookieStandList(ListCreateAPIView):
    queryset = CookieStands.objects.all()
    serializer_class = CookieStandserializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStands.objects.all()
    serializer_class = CookieStandserializer
