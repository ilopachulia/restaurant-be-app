from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from .serializers import ProductSerializer
from .models import ProductModel


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_products(request):
    try:
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "message": "success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "error", 
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_product(request):
    try:
        data = request.data.copy()
        data['creator'] = request.user.user_name

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({
                "message": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)