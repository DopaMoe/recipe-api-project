from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_successful_email(self):
        email = "email@example.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.user_email, email)
        self.assertTrue(user.check_password(password))
