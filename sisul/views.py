from rest_framework import status
from rest_framework.response import Response
from .models import Sisul
from rest_framework.decorators import api_view
from .serializer import SisulSerializer

# Create your views here.
@api_view(['GET'])
def SisulAPI(request):
    if request.method == 'GET':
        sisul = Sisul.objects.all()
        serializer = SisulSerializer(sisul, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
