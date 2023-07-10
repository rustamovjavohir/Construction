from config.setUpDjango import *
from faker import Faker

from apps.apartment.models import Apartment


def fake_apartment(apartment_number: int = 5):
    fake = Faker()
    for _ in range(apartment_number):
        Apartment.objects.create(
            room_quantity=fake.random_int(min=1, max=5),
            area=fake.random_int(min=40, max=200),
            floor=fake.random_int(min=1, max=16),
            price=fake.random_int(min=1000000, max=100000000),
            balcony=fake.random_int(min=0, max=1),
            bedroom=fake.random_int(min=0, max=1),
            bathroom=fake.random_int(min=0, max=1),
            hall=fake.random_int(min=0, max=1),
            kitchen=fake.random_int(min=0, max=1),
            dining_room=fake.random_int(min=0, max=1),
            living_room=fake.random_int(min=0, max=1),
        )
