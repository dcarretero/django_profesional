
from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.primera_vista, name="primera_vista"),
]