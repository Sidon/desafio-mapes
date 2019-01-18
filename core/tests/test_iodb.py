from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.test import TestCase
from core.models import Consulta


# TODO Desenvolver testes
# class SdnTestCase(TestCase):
#
#     def setup(self):
#
#         self.username = "admin"
#         self.email = ""
#         self.password = "master.21"
#         self.user = User.objects.create_user(self.username, self.email, self.password)
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
#
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#
#     def test_get_consulta(self):

