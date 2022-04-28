from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

# Create your view here.

class Musiclist (generics.ListCreateAPIView):
    
    queryset = Music.objects.all()
    serializer_class = MusicSerializer