from django.test import TestCase
from apps.user.models import User


# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username=" test",
            email=" ",  # email is required
            phone="998999999989"
        )

    def test_user(self):
        self.assertEqual(self.user.username, " test")
        self.assertEqual(self.user.email, " ")
        self.assertEqual(self.user.phone, "998999999989")

        # this is new comment
