from rest_framework import serializers
from items.models import Item 
from django.contrib.auth.models import User



class UserSerlializer(serializers.ModelSerializer):
	class Meta :
		model = User
		fields = ['first_name','last_name']

class ListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "object_id"
        )
	favusers = serializers.SerializerMethodField()
	added_by = UserSerlializer()

	def get_favusers(self,obj):
		return len(obj.favoriteitem_set.all())

	class Meta: 
		model = Item 
		fields = ['image' , 'name' , 'description', 'detail', 'favusers', 'added_by']

	

class DetailSerializer(serializers.ModelSerializer):

	favby = serializers.SerializerMethodField()
	added_by = UserSerlializer()

	class Meta: 
		model = Item 
		fields = ['image' , 'name' , 'description', 'favby', 'added_by']

	def get_favby(self,obj):
		favorites =  obj.favoriteitem_set.all()
		users=[]
		for fav in favorites: 
			users.append(Users.objects.get(id=fav.user.id))

		return UserSerlializer(users, many=True).data

