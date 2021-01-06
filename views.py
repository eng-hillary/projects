from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from landlord.models import House
from .serializers import HouseSerializer

@api_view(['GET',])
def api_house_detail_view(request, id):
    try:
        house = House.objects.get(id=id)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HouseSerializer(house)
        return Response(serializer.data)

@api_view(['PUT',])
def api_house_detail_update(request,id):
    try:
        house = House.objects.get(id=id)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update success'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)