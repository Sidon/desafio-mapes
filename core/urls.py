from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()
router.register(r'consultas', views.ConsultaViewSet)
# router.register(r'api/exames', views.ExamesViewSet)


urlpatterns = [
    url(r'^$', views.ConsultaListView.as_view(), name='home'),
    url(r'consultas/', views.ConsultaListView.as_view(), name='consultas'),
    url(r'exames/', views.ExameListView.as_view(), name='exames'),
    url('update-consulta/(?P<pk>[\w-]+)$', views.ConsultaUpdateView.as_view(), name='update1'),
    url('update-exame/(?P<pk>[\w-]+)$', views.ExameUpdateView.as_view(), name='update-exame'),
]


