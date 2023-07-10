from config.setUpDjango import *
from faker import Faker

from apps.user.models import User


def fake_user(user_number: int = 5):
    fake = Faker()
    for _ in range(user_number):
        User.objects.create(
            username=fake.name(),
            email=fake.email(),
            password=fake.password(),
            phone=fake.phone_number(),
        )
