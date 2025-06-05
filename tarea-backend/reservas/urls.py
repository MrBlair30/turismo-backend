from django.urls import path
from .views import ClienteListCreateView, ClienteDetailView, LugarListCreateView, LugarDetailView, HabitacionListCreateView, HabitacionDetailView, ReservaListCreateView, ReservaDetailView, HabitacionesPorLugarView, ReservasPorClienteView, CiudadDetailView, CiudadListCreateView, CiudadRetrieveUpdateDestroyView, LugaresPorCiudadView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('lugares/', LugarListCreateView.as_view(), name='lugar-list-create'),
    path('lugares/<int:pk>/', LugarDetailView.as_view(), name='lugar-detail'),
    path('habitaciones/', HabitacionListCreateView.as_view(), name='habitacion-list-create'),
    path('habitaciones/<int:pk>/', HabitacionDetailView.as_view(), name='habitacion-detail'),
    path('reservas/', ReservaListCreateView.as_view(), name='reserva-list-create'),    
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('lugares/<int:lugar_id>/habitaciones/', HabitacionesPorLugarView.as_view(), name='habitaciones-por-lugar'),
    path('clientes/<int:cliente_id>/reservas/', ReservasPorClienteView.as_view(), name='reservas-por-cliente'),
    path('ciudades/<int:pk>/', CiudadDetailView.as_view(), name='ciudad-detail'),
    path('ciudades/', CiudadListCreateView.as_view(), name='ciudad-list-create'),
    path('ciudades/<int:pk>/', CiudadRetrieveUpdateDestroyView.as_view(), name='ciudad-detail'),
    path('ciudades/<int:ciudad_id>/lugares/', LugaresPorCiudadView.as_view(), name='lugares-por-ciudad'),
]