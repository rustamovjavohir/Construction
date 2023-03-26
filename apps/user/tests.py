from django.test import TestCase
from apps.user.models import User


# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name=" test",
            email=" ",  # email is required
            phone="998999999999",
            is_web=True,
            is_telegram=False,
        )

    def test_user(self):
        self.assertEqual(self.user.name, " test")
        self.assertEqual(self.user.email, " ")
        self.assertEqual(self.user.phone, "998999999999")
        self.assertEqual(self.user.is_web, True)
        self.assertEqual(self.user.is_telegram, False)
