## sdnmapes URL Configuration


from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core.urls import router

app_name = 'sdnmapes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/', include(router.urls)),
    path('', include('core.urls'))
]
