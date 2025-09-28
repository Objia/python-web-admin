from  django.urls import path
from user.views import Testview

urlpatterns = [
    path('test/', Testview.as_view(), name='test'),
]