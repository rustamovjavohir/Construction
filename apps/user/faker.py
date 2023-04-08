from config.setUpDjango import *
from faker import Faker

from apps.user.models import User


def fake_user():
    fake = Faker()
    for _ in range(5):
        User.objects.create(
            username=fake.name(),
            email=fake.email(),
            password=fake.password(),
            phone=fake.phone_number(),
        )
