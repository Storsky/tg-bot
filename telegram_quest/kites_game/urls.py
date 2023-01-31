from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='startgame'),
    path('game', startgame, name='game' )

]