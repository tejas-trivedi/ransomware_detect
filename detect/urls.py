from django.urls import include, path
from .views import RansomDetectView

urlpatterns = [
    path('detect', RansomDetectView.as_view(), name='detect'),
]

