from config.setUpDjango import *
from faker import Faker

from apps.order.models import Order


def fake_order(fake_number: int = 100):
    fake = Faker()
    for _ in range(fake_number):
        try:
            Order.objects.create(
                name=fake.sentence(nb_words=5),
                user_id=fake.random_int(min=1, max=5),
                apartment_id=fake.random_int(min=1, max=10),
                status=fake.random_int(min=0, max=1),
            )
        except Exception as e:
            print(e)
