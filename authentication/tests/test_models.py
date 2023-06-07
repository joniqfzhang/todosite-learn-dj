# from django.test import TestCase
from utils.setup_test import TestSetup
from authentication.models import User


# class TestModel(TestCase):
class TestModel(TestSetup):
    def test_should_create_user(self):
        # user = User.objects.create_user(username='username', email='email@app.com')
        # user.set_password('password12!')
        # user.save()
        user = self.create_test_user()

        # self.assertEquals(str(user), 'email@app.com')
        self.assertEquals(str(user), user.email)

