from config.setUpDjango import *
from faker import Faker

from apps.advertising.models import Advertising


def fake_apartment(n):
    fake = Faker()
    for _ in range(n):
        Advertising.objects.create(
            title=fake.name(),
            image=fake.image_url(),
            description=fake.text(),
            created_at=fake.date(),
            finished_at=fake.date(),
            is_deleted=False,
        )
