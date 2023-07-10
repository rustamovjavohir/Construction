from django.db import models


# Create your models here.


class Floor(models.Model):
    floor_id = models.IntegerField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} {self.floor_id}"

    class Meta:
        ordering = ["-id"]


class Apartment(models.Model):
    room_quantity = models.IntegerField(null=True)
    area = models.FloatField(null=True, blank=True)
    # floor = models.ManyToManyField(to=Floor)
    floor = models.IntegerField(null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    balcony = models.FloatField(null=True, blank=True)
    bedroom = models.FloatField(null=True, blank=True)
    bathroom = models.FloatField(null=True, blank=True)
    hall = models.FloatField(null=True, blank=True)
    kitchen = models.FloatField(null=True, blank=True)
    dining_room = models.FloatField(null=True, blank=True)
    living_room = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='Images', null=True, blank=True)
    image_2d = models.ImageField(upload_to='2DImages', null=True, blank=True)
    image_3d = models.ImageField(upload_to='3DImages', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.floor} floor {self.room_quantity} room {self.area} m^2"

    class Meta:
        ordering = ["-id"]
