from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["status", "source"]

    search_fields = ["name", "email", "phone"]

    ordering_fields = [
        "created_at",
        "updated_at",
        "name",
        "status",
    ]

    ordering = ["-created_at"]

    def get_queryset(self):
        return Lead.objects.filter(
            created_by=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)