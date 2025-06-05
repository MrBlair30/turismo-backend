from rest_framework import serializers
from .models import Cliente, Lugar, Habitacion, Reserva, Ciudad

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        depth = 1

class LugarSerializer(serializers.ModelSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)
    class Meta:
        model = Lugar
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'habitaciones']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def create(self, validated_data):
        reserva = Reserva.objects.create(**validated_data)
        # Actualiza el estado de la habitación
        habitacion = reserva.habitacion
        habitacion.reservada = True
        habitacion.save()
        return reserva

class CiudadSerializer(serializers.ModelSerializer):
    lugares = LugarSerializer(many=True, read_only=True)
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'lugares']

