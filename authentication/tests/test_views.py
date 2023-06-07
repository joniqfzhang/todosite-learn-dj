from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup


# Create your tests here.

class TestViews(TestSetup):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_should_signup_user(self):
        self.user = {
            'username': 'test1234',
            'email': 'test1234@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(reverse('register'), self.user)
        self.assertEquals(response.status_code, 302)  # 302 redirect

    def test_should_not_signup_user_with_taken_username(self):
        self.user = {
            'username': 'test1234',
            'email': 'email@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        # first call with username test1234
        self.client.post(reverse('register'), self.user)
        # second call with username same username
        response = self.client.post(reverse('register'), self.user)
        self.assertEquals(response.status_code, 409)  # HTTP 409 status code (Conflict)

        storage = get_messages(response.wsgi_request)
        # errors = []
        #
        # for message in storage:
        #     print(message)
        #     errors.append(message.message)

        # print('errors', errors)
        # self.assertIn('Username is taken, choose another one', errors)
        self.assertIn('Username is taken, choose another one',
                      list(map(lambda x: x.message, storage))
                      )

        # python debuger
        # import pdb
        # pdb.set_trace()

    def test_should_not_signup_user_with_taken_email(self):
        self.user = {
            'username': 'username1',
            'email': 'email@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        self.user2 = {
            'username': 'username2',
            'email': 'email@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        # first call with username test1234
        self.client.post(reverse('register'), self.user)
        # second call with username same username
        response = self.client.post(reverse('register'), self.user2)
        self.assertEquals(response.status_code, 409)  # HTTP 409 status code (Conflict)
