from django.urls import reverse

from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo

# Create your tests here.
class TestModel(TestSetup):
    def test_should_create_todo(self):
        # user created but not login
        user = self.create_test_user()
        # login user
        self.client.post(reverse('login'), {
            'username': user.username,
            'password': 'password12!'
        })

        todos = Todo.objects.all()
        self.assertEqual(todos.count(), 0)

        response = self.client.post(reverse('create-todo'), {
            'owner': user,
            'title': 'Hello do more',
            'description': 'do remember to do this'
        })

        todos = Todo.objects.all()
        print('response', response)
        self.assertEqual(todos.count(), 1)
        self.assertEqual(response.status_code, 302)
