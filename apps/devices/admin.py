"""Регистрация в админке."""
from django.contrib import admin
from django.db import models

from .models import Device


class RadiusListFilter(admin.SimpleListFilter):
    """Фильтр для радиуса зны покрытия с шагом 100 м."""

    title = "Радиус больше чем"
    parameter_name = "radius__gt"

    def lookups(self, request, model_admin):
        """Строим список значений для фильтра."""
        max_radius = (
            model_admin.model.objects.aggregate(models.Max("radius")).get(
                "radius__max"
            )
            or 0
        )
        return [(value, f"{value} м") for value in range(0, max_radius, 100)]

    def queryset(self, request, queryset):
        """Фильтруем кверисет, если параметр задан. Строго больше, как в ТЗ."""
        # Если строка пустая или отсуствует
        if not self.value():
            return

        # Если в строке не число, а набор символов
        try:
            value = int(self.value())
        except ValueError:
            return

        return queryset.filter(radius__gt=value)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """Регистрация устройств в админке."""

    list_filter = ("type", RadiusListFilter)
    list_display = ("name", "type", "address", "lat", "lon", "radius")
    search_fields = ("name", "address")
