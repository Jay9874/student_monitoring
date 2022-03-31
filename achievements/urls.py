from django.urls import path
from . import views

app_name = "achievements"

urlpatterns = [
    path("academics", views.academics, name="academics"),
    path("co_curriculum", views.co_curriculum, name="co_curriculum"),
    path("others", views.others, name="others")
    
] 