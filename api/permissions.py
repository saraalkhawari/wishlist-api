from rest_framework.permissions import BasePermission
from datetime import date

class IsOwnerOrStaff(BasePermission):
	message  ='Only Owners and Staff have Access !'

	def has_object_permission(self,request,view,obj):
		if request.user.is_staff or request.user == obj.added_by :
			return True 
		return False
