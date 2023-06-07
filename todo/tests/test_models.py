# from django.test import TestCase
from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo


# class TestModel(TestCase):
class TestModel(TestSetup):
    def test_should_create_user(self):
        # user = User.objects.create_user(username='username', email='email@app.com')
        # user.set_password('password12!')
        # user.save()
        # self.assertEquals(str(user), 'email@app.com')
        user = self.create_test_user()
        todo = Todo(owner=user, title='Buy milk', description='get it done')
        todo.save()
        self.assertEquals(str(todo), 'Buy milk')

