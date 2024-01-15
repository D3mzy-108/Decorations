from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('designs/', designs_page, name='designs'),
    path('designs/<int:id>/details/', design_details, name='design_details'),
]
