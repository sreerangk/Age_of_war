from django.urls import path

from app_battles.api.battle_view import BattleAPIView, BattleView

app_name = 'battles'

urlpatterns = [
    path('', BattleView.as_view(), name='index'),
    path('api/', BattleAPIView.as_view(), name='api'),
]