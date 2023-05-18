from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run webhook bot'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Successfully run bot'))
