from django.urls import path
from . import views
from .views import Survey_simila_View

app_name = 'waitting'

urlpatterns = [
    path('read_json_file/', views.read_json_file, name='read_json_file'),
    path('Survey_simila_View/', Survey_simila_View.as_view(), name='Survey_simila_View'),
    path('recommend_areas/', views.recommend_areas, name='recommend_areas'),
    
]
