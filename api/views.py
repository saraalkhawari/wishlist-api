from rest_framework.generics import ListAPIView , RetrieveAPIView
from items.models import Item, FavoriteItem
from .serializers import ListSerializer , DetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import (
	IsOwnerOrStaff
	)

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ListSerializer
	filter_backends = [SearchFilter , OrderingFilter]
	search_fields = ['name']
	permission_classes = [AllowAny]


class ItemDetailView(RetrieveAPIView):
	queryset=Item.objects.all()
	serializer_class=DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'
	permission_classes = [IsOwnerOrStaff]



