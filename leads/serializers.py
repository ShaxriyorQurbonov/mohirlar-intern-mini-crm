from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Lead
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "source",
            "status",
            "note",
            "created_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        if self.instance is not None:
            email = attrs.get("email", self.instance.email)
            phone = attrs.get("phone", self.instance.phone)
        else:
            email = attrs.get("email")
            phone = attrs.get("phone")

        if not email and not phone:
            raise serializers.ValidationError(
                "Email or phone is required."
            )

        return attrs