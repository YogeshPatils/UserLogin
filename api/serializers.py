from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=['password','username','last_login','date_joined','is_superuser','is_staff','is_active']