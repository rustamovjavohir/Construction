from config.setUpDjango import *
from apps.sendEmail.models import Email
from faker import Faker


def fake_sendEmail(fake_number: int):
    fake = Faker()
    for _ in range(fake_number):
        try:
            Email.objects.create(
                email=fake.email(),
                subject=fake.sentence(nb_words=15),
                message=fake.sentence(nb_words=5),
                recipient=fake.email(),
            )
        except Exception as e:
            print(e)
