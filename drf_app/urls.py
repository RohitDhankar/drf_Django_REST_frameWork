from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from drf_app.views import *
from django.conf.urls import *
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
#from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    
    url(r'^drfAppTest/', views.drfAppTest, name='call_drfAppTest'),
]

