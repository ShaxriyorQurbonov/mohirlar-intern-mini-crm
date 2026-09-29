from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
import uuid
from .models import Lead


class LeadAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

    def test_unauthorized_user_cannot_access_leads(self):
        response = self.client.get("/api/leads/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_create_lead(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "name": "Test Lead",
            "email": "test@example.com",
            "phone": "+998901234567",
            "source": "TELEGRAM",
            "status": "NEW",
            "note": "Test lead",
        }

        response = self.client.post(
            "/api/leads/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Lead.objects.count(),
            1,
        )

        self.assertEqual(
            response.data["name"],
            "Test Lead",
        )

    def test_user_can_see_only_own_leads(self):
        other_user = User.objects.create_user(
            username="otheruser",
            password="testpassword123",
        )

        Lead.objects.create(
            id=uuid.uuid4(),
            name="My Lead",
            email="my@example.com",
            source="TELEGRAM",
            status="NEW",
            created_by=self.user,
        )

        Lead.objects.create(
            id=uuid.uuid4(),
            name="Other Lead",
            email="other@example.com",
            source="INSTAGRAM",
            status="NEW",
            created_by=other_user,
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get("/api/leads/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            1,
        )

        self.assertEqual(
            response.data["results"][0]["name"],
            "My Lead",
        )

    def test_lead_requires_email_or_phone(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "name": "Invalid Lead",
            "source": "TELEGRAM",
            "status": "NEW",
            "note": "No contact information",
        }

        response = self.client.post(
            "/api/leads/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_search_leads(self):
        Lead.objects.create(
            id=uuid.UUID("11111111-1111-4111-8111-111111111111"),
            name="Ali Valiyev",
            email="ali@example.com",
            source="TELEGRAM",
            status="NEW",
            created_by=self.user,
        )

        Lead.objects.create(
            id=uuid.UUID("22222222-2222-4222-8222-222222222222"),
            name="Aziz Hasanov",
            email="hasanov@example.com",
            source="INSTAGRAM",
            status="NEW",
            created_by=self.user,
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            "/api/leads/?search=Ali"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            1,
        )

        self.assertEqual(
            response.data["results"][0]["name"],
            "Ali Valiyev",
        )