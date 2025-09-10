from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

# User Registration API
class RegisterAPIView(APIView):
    """This View registers a new user with username and password.
    The data is recieved in the following format:
    {"username": "the_username", "password": "the_password"}

    And the response is returned in the following format:
    {"message": "User registered successfully."}

    Or in case of error:
    {"error": "Error message"}
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        # get username and password from request
        username = request.data.get("username").strip()
        password = request.data.get("password").strip()

        # validate the incoming data and add user if valid
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "Username already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not username or not password:
                return Response(
                    {"error": "Username and password are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # add the user with validated data to database
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()

            # return success response
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED,
            )

        # return failure response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login API
class LoginAPIView(APIView):
    """This View logs in a user with username and password.

    The data is recieved in the following format:
    {"username": "the_username", "password": "the_password"}

    And the response is returned in the following format:
    {"refresh": "the_refresh_token", "access": "the_access_token"}

    Or in case of error:
    {"error": "Invalid credentials."}
    """

    permission_classes = [permissions.AllowAny]

    # login user and return jwt access and refresh tokens for valid user
    def post(self, request):

        # get username and password from request
        username = request.data.get("username")
        password = request.data.get("password")

        # authenticate the user and get user object
        user = authenticate(username=username, password=password)

        # if user object is returned, generate tokens
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )

        # else return error response
        else:
            return Response(
                {"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
            )

