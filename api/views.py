from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def userApiView(request):
    if request.method=='GET':
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    return Response({"message": "Invalid request method"}, status=400)

