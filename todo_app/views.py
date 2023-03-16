from rest_framework.decorators import api_view 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from .models import ToDo
from .serializers import ToDoSerializer, UpdateToDoSerializer 

@api_view(['GET'])
def get_todos(request: Request, pk=None) -> Response:
    if pk != None:
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({'detail': f'todo with id:{pk} does not exist'})
        serializer = ToDoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        queryset = ToDo.objects.all()
        print(queryset)
        serializer = ToDoSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='POST', request_body = ToDoSerializer)
@api_view(['POST'])
def create_todo(request: Request) -> Response:
    serializer = ToDoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    todo = ToDo.objects.create(**serializer.data)
    todo.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    # serializer.is_valid(raise_exception=True)
    # if serializer.is_valid():
    #     todo = ToDo.objects.create(**serializer.data)
    #     todo.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todo(request: Request, pk):
    try: 
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response({'detail': f'ToDo with id:{pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    todo.delete()
    return Response({'detail': 'Succesfeully deleted'}, status=status.HTTP_204_NO_CONTENT)
    
@swagger_auto_schema(method='PATCH', request_body=UpdateToDoSerializer)
@api_view(['PATCH'])
def update_todo(request: Request, pk) -> Response:
    
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response({'detail': f'ToDo with id:{pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UpdateToDoSerializer(instance=todo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_todo(reuest: Request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    serializer = ToDoSerializer(instance=todo)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    

# TODO: написать функцию для получения ОДНОГО объекта 
# TODO: подключить свагер
