from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist # Import this for robust error handling

from user.models import UserModel

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        data = request.data

        # Check for existing email
        if UserModel.objects.filter(email=data.get('email')).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing username
        # It seems you intended to check user_name here, not email again.
        if UserModel.objects.filter(user_name=data.get('user_name')).exists():
            return Response({'message': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure passwords match
        if data.get('password') != data.get('password2'):
            return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user using the custom manager's create_user method
        try:
            user = UserModel.objects.create_user(
                user_name=data.get('user_name'),
                email=data.get('email'),
                password=data.get('password') # The create_user method handles hashing
            )
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Catch any other potential errors during user creation
            return Response({'message': f'Error creating user: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # This return None is unreachable due to the if request.method check always returning a Response
    # It's good practice to ensure all paths return a Response.
    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def user_login(request):
    data = request.data
    try:
        user = UserModel.objects.get(email=data.get('email')) # Use .get() for single object retrieval
        if not check_password(data.get('password'), user.password):
            return Response({'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        # The `login` function is for Django's session authentication.
        # Ensure you have Django's authentication middleware configured.
        login(request, user)

        return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist: # Catch the more general exception
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND) # 404 is more appropriate for "not found"
    except Exception as e:
        # Catch any other unexpected errors
        return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)