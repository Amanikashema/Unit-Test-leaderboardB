from flask.wrappers import Response
from website.tests.base_tests import BaseTest, db
from website.models import User
from flask_login import current_user
from flask import request


# Class to test Login

class TestLogin(BaseTest):
    # test signing up user successfully
    def test_sign_up_post_success(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

    # Testing Login
    def test_log_in_success(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                               password2='pass1234'),
                                     follow_redirects=True)
            # create a post req with valid data
            response_login = self.app.post('/log-in',
                                     data=dict(email='email@gmail.com', password='pass1234'),
                                     follow_redirects=True)

            # assert that route works
            request = self.app.get('/log-in')
            self.assertEqual(request.status_code, 200)

            # assert 200 status code of response
            self.assertEqual(response_login.status_code, 200)

            # assert that user is logged in
            self.assertIn(b"Logged in successfully",response_login.data)

    # test logging with wrong email
    def test_log_in_invalid_user(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            # create a post req with invalid data (non existing email)
            response_login = self.app.post('/log-in',
                                           data=dict(email='amani@gmail.com', password='pass1234'),
                                           follow_redirects=True)

            # Test non existing email
            self.assertIn(b'Email does not exist',response_login.data)

    # test logging with wrong password
    def test_log_in_wrong_password(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            # create a post req with invalid data (non wrong password)
            response_login = self.app.post('/log-in',
                                           data=dict(email='email@gmail.com', password='pass'),
                                           follow_redirects=True)

            # Test logging in with wrong password
            self.assertIn(b'Logged in unsuccessfully',response_login.data)


class TestLogout(BaseTest):
    # function to test route when user is logged in
    def test_route_logged_in(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            response_logout = self.app.get('/log-out',
                                           data=dict(email='email@gmail.com', password='pass1234'),
                                           follow_redirects=True)
            # test response code of route if logged in user accessed it
            self.assertEqual(response_logout.status_code,200)

    # function to test if route is accessible when user is not logged in
    def test_route_logged_out(self):
        response_logout = self.app.get('/log-out')
        self.assertEqual(response_logout.status_code, 302)

    # function to test response code when user navigates to page logged in
    def test_user_nav_login(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            # create a post req with valid data
            response_login = self.app.post('/log-in',
                                           data=dict(email='email@gmail.com', password='pass1234'),
                                           follow_redirects=True)
            self.assertEqual(response_login.status_code,200)

    # test response code when user navigates to page not logged in
    def test_user_nav_not_logged_in(self):
        response_logout = self.app.get('/log-in')
        self.assertEqual(response_logout.status_code, 200)

    # test that current_user is none after logging out
    def test_current_user(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            response_logout = self.app.get('/log-out',
                                           data=dict(email='email@gmail.com', password='pass1234'),
                                           follow_redirects=True)
            self.assertEqual(response_logout.status_code,200)
            # user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertIsNone(current_user.get_id())

    # test that user is redirected to login page after log out
    def test_user_redirected_home_page(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            response_logout = self.app.get('/log-out',follow_redirects=True)
            self.assertEqual('http://localhost/log-in',request.url)


































