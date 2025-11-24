from django.contrib import admin
from django.db import models

from djangoql.admin import DjangoQLSearchMixin


class CustomModelAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    exclude_fields = []
    exclude_readonly_fields = []

    def get_list_display(self, request):
        if self.list_display == admin.ModelAdmin.list_display:
            fields = [
                field.name
                for field in self.model._meta.get_fields()
                if not isinstance(field, (models.ManyToManyField, models.ManyToOneRel, models.ForeignKey))
                   and field.name not in self.exclude_fields
            ]

            id_field = [f for f in fields if f == "id"]
            created_updated = [f for f in fields if f in ("created", "updated")]
            status_fields = [f for f in ("processed", "success", "error_message") if f in fields]
            other_fields = [
                f for f in fields
                if f not in ("id", "created", "updated", *status_fields)
            ]
            self.list_display = list(id_field + other_fields + status_fields + created_updated)

        return self.list_display

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields == admin.ModelAdmin.readonly_fields:
            readonly_fields = [
                field.name
                for field in self.model._meta.get_fields()
                if not field.auto_created
                   and isinstance(
                    field,
                    (
                        models.ForeignKey,
                        models.OneToOneField,
                        models.ManyToManyField,
                    ),
                ) and field.name not in self.exclude_readonly_fields
            ]
            return readonly_fields
        return self.readonly_fields
