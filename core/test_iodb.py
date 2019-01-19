from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from core.models import Consulta, ExameRealizado
from django.core.management import call_command


# Testa a inclusao dos dados iniciais
class ConsulTest(APITestCase):

    def setUp(self):
        self.username = "admin"
        self.email = ""
        self.password = "master.21"
        self.user = User.objects.create_superuser(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        call_command('initialdata')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_consulta(self):
        consulta  = Consulta.objects.get(numero_guia_consulta='30')
        self.assertEqual(consulta.nome_medico, 'Ângela Costa')

    def test_get_exame(self):
        exame = ExameRealizado.objects.filter(consulta__numero_guia_consulta='1')
        self.assertEqual(exame.count(), 2)
