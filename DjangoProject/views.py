from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_home_page(request):
    return Response('init home page')