"""Модели приложения."""
from django.db import models


class Device(models.Model):
    """Модель устройства."""

    class Type(models.TextChoices):
        """Константы типов устройств."""

        SIREN = "siren", "Сирена"
        SPEAKER = "speaker", "Громкоговоритель"

    name = models.CharField("Название", max_length=255)
    type = models.CharField(
        "Тип устройста", max_length=10, choices=Type.choices
    )
    address = models.CharField("Адрес", max_length=255)
    lat = models.DecimalField("Широта", max_digits=8, decimal_places=6)
    lon = models.DecimalField("Долгота", max_digits=9, decimal_places=6)
    radius = models.PositiveIntegerField("Радиус зоны звукопокрытия")

    class Meta:
        """Meta."""

        verbose_name = "Устройство оповещения"
        verbose_name_plural = "Устройства оповещения"

    def __str__(self):
        """Отображение в адмике и repr в консоли."""
        return f"Устройство {self.name} (#{self.pk})"
