import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class TestNewsList(APITestCase):
    @pytest.mark.django_db
    def test_can_get_news_list(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 8)
