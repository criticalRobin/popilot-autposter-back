from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from authentication.serializers import LoggedUserSerializer, CreateUserSerializer


# Create your views here.
class LoggedUserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LoggedUserSerializer

    def get(self, request):
        user = request.user

        if user is not None:
            return Response(self.serializer_class(user).data)


class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
