from rest_framework import generics
from .models import Cliente, Lugar, Habitacion, Reserva, Ciudad
from .serializers import ClienteSerializer, LugarSerializer, HabitacionSerializer, ReservaSerializer, CiudadSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#Cliente
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

#Lugar
class LugarListCreateView(generics.ListCreateAPIView):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class LugarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

#Habitacion
class HabitacionListCreateView(generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class HabitacionesPorLugarView(generics.ListAPIView):
    serializer_class = HabitacionSerializer

    def get_queryset(self):
        lugar_id = self.kwargs['lugar_id']
        return Habitacion.objects.filter(lugar_id=lugar_id)

class HabitacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

#Reserva
class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservasPorClienteView(generics.ListAPIView):
    serializer_class = ReservaSerializer
    
    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Reserva.objects.filter(cliente_id=cliente_id)

class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

#Ciudad
class CiudadDetailView(APIView):
    def get(self, request, pk):
        try:
            ciudad = Ciudad.objects.get(pk=pk)
        except Ciudad.DoesNotExist:
            return Response({'error': 'Ciudad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CiudadSerializer(ciudad)
        return Response(serializer.data)

class CiudadListCreateView(generics.ListCreateAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class CiudadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class LugaresPorCiudadView(generics.ListAPIView):
    serializer_class = LugarSerializer

    def get_queryset(self):
        ciudad_id = self.kwargs['ciudad_id']
        return Lugar.objects.filter(ciudad_id=ciudad_id)

