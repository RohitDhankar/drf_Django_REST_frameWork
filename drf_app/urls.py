from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from drf_app.views import *
from django.conf.urls import *
from django.conf import settings
#from django.contrib.auth.decorators import login_required, permission_required


from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
#from tutorial.quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #url(r'^drfAppTest/', views.drfAppTest, name='call_drfAppTest')
]

