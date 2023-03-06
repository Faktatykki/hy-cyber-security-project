import unittest
import uuid

from django.contrib.auth.models import User
from django.test import TestCase

from src.models import Secret
from django.test import Client
from django.contrib import auth
from django.contrib.auth import get_user

c = Client()

class everythingTest(TestCase):
    def get_passwords(self):
        return [str(uuid.uuid4()), str(uuid.uuid4())]

    def setUp(self):
        
        User.objects.create_user(username="User1", password=self.get_passwords()[0])
        User.objects.create_user(username="User2", password=self.get_passwords()[1])

    def test_create_user(self):
        users = User.objects.all()

        self.assertEqual(len(users), 2)

    def test_login(self):
        user = User.objects.create_user(username="User3", password="")
        user.set_password("1234")
        user.save()
        
        is_logged_in = c.login(username="User3", password="1234")

        self.assertTrue(is_logged_in)

    def test_create_secret(self):
        return



