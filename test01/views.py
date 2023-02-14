from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Test01
from .serializers import TestDataSerializer
from rest_framework import status

@api_view(['GET'])
def getTestDatas(request):
    datas = Test01.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTestData(request, name):
    data = Test01.objects.get(name=name)
    serializer = TestDataSerializer(data, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postMember(request):
    reqData = request.data
    serializer = TestDataSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def putMember(request, pk):
    reqData = request.data
    data = Test01.objects.get(id=pk)
    serializer = TestDataSerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)