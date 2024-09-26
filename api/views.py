from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartItemSerializer
from .models import CartItem

# Create your views here.
class CartItemsViews(APIView):
    serializer_class = CartItemSerializer

    # Codigo del ORM de Django para obtener todos los registros de la tabla CartItem
    def get_queryset(self):
        return CartItem.objects.all() # SELECT * FROM CartItem
    
    # Metodo POST para insertar un nuevo registro en la tabla CartItem
    def post(self, request):
        # Transformamos los datos que vienen en el request a un objeto serializado de python
        serializer = CartItemSerializer(data=request.data)
        # Validamos si los datos son correctos, son las validaicones que definimos en el serializer
        if serializer.is_valid():
            serializer.save() # Guardamos los datos en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si los datos no son correctos, retornamos un error 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET para obtener todos los registros de la tabla CartItem
    def get(self, request, pk=None):
        if pk:
            # Obtenemos un registro en especifico de la tabla CartItem
            cart_item = CartItem.objects.filter(pk=pk).first()
            # Validamos si el registro existe
            if not cart_item:
                return Response({'message': 'Cart Item not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Serializamos los datos obtenidos
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Obtenemos todos los registros de la tabla CartItem
        cart_items = CartItem.objects.all()
        # Serializamos los datos obtenidos
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    # Actualizar un ítem existente
    def put(self, request, pk):
        # Obtenemos el ítem a actualizar
        cart_item = CartItem.objects.filter(pk=pk).first()
        if not cart_item:
            return Response({'message': 'Cart Item not found'}, status=status.HTTP_404_NOT_FOUND)
        # Serializamos los datos del request
        serializer = CartItemSerializer(cart_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar un ítem
    def delete(self, request, pk):
        # Obtenemos el ítem a eliminar
        cart_item = CartItem.objects.filter(pk=pk).first()
        if not cart_item:
            return Response({'message': 'Cart Item not found'}, status=status.HTTP_404_NOT_FOUND)
        # Eliminamos el ítem
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)