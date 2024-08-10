from django.shortcuts import render
from rest_framework.views APIView
from .serializers import LoginSerializer
from rest_framework import Response
from rest_framework import status
from models import User

# APIView: handle API logic

# Create your views here.
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        # check if data gotten from serializer is valid
        try:
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            username = serializer.validated_date.get('username')

            # get the user vlass
            user = User.objects.get(username=username)

            if user.password == password:
                        return Response({"message":"success"}, status.HTTP_200_OK)
                        else:
                            return Response({"message":"error"}, status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"message": e}, status.HTTP_400_BAD_REQUEST)


        else:
             Response({"message":"error"}, status.HTTP_400_BAD_REQUEST)
           

