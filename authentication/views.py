from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import LoggedUserSerializer


# Create your views here.
class LoggedUserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LoggedUserSerializer

    def get(self, request):
        user = request.user

        if user is not None:
            return Response(self.serializer_class(user).data)
