# from django.test import TestCase
# from django.urls import reverse

# from apps.user.models import User


# # Create your tests here.
# class TestUser(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             username=" test",
#             email=" ",  # email is required
#             phone="998999999989"
#         )

#     def test_user(self):
#         self.assertEqual(self.user.username, " test")
#         self.assertEqual(self.user.email, " ")
#         self.assertEqual(self.user.phone, "998999999989")

#     def test_url_user(self):
#         url = reverse("user-list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)



def transformString(sentense):
    words = sentense.split()
    transform_string = []
    transform_string.append(words[0])
    for i in range(len(words[1:-1])):
        if ord(words[i]) < ord(words[i+1]):
            transform_string.append(words[i+1].upper())
        else:
            transform_string.append(words[i+1].lower())
    return " ".join(transform_string)

result = transformString("Hello World")
print(result)