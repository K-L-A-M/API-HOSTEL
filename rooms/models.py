from django.db import models
from uuid import uuid4
from promotions.models import Promotion


class RoomFeature(models.Model):
    class Meta:
        ordering = ["id",]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(unique=True)


class BedType(models.TextChoices):
    SINGLE = "SI", "Single"
    DOUBLE = "DO", "Double"
    KING_SIZE = "KS", "King Size"
    QUEEN_SIZE = "QS", "Queen Size"


class Room(models.Model):
    class Meta:
        ordering = ["id",]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    floor = models.PositiveIntegerField(null=False)
    room_number = models.CharField(max_length=10, unique=True, null=False)
    capacity = models.PositiveIntegerField(null=False)
    is_occupied = models.BooleanField(default=False)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    promotions = models.ManyToManyField(Promotion, blank=True)
    beds = models.ManyToManyField("Bed", blank=True, related_name="bed_rooms")
    features = models.ManyToManyField(RoomFeature, blank=True)


class Bed(models.Model):
    class Meta:
        ordering = ["id",]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    bed_type = models.CharField(max_length=20, choices=BedType.choices, null=False)
    quantity = models.PositiveIntegerField(null=False)
