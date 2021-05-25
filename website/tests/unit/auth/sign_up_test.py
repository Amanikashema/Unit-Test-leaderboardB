from website.tests.base_tests import BaseTest, db
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User


class TestSignUp(BaseTest):
    def test_get_sign(self):
        with self.app:
            response = self.app.get('/sign-up',follow_redirects=True)
            self.assertIn('/sign-up',request.url)

            self.assertIn(b'<title>\nSign Up\n</title',response.data)
            self.assertEqual(response.status_code,200)
            self.assertEqual(current_user.get_id(),AnonymousUserMixin.get_id(self))

    def test_sign_up_post_short_email(self):
        with self.app:
            response = self.app.post('/sign-up',data=dict(email='meh',first_name='NormalName',password='pass123',follow_redirects=True))
            self.assertIn(b'Email must be greater than 3 characters', response.data)
            self.assertEqual(response.status_code,200)
            user = db.session.query(User).filter_by(email='meh').first()
            self.assertFalse(user)
            self.assertIsNone(current_user.get_id())

    def test_sign_up_post_short_name(self):
        with self.app:
            response = self.app.post('/sign-up',data=dict(email='email@gmail.com',firstName='h',password='pass1234', follow_redirects=True))
            # assert that flash message appears
            self.assertIn(b'First name must be greater than 1 character', response.data)
            # assert status code
            self.assertEqual(response.status_code, 200)  # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())

    # test sign up post if passwords don't match

    def test_sign_up_post_passwords_mismatched(self):
        with self.app:
            # create our post req
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                               password2='pass6789'),
                                     follow_redirects=True)
            # assert flash message appears
            self.assertIn(b'Passwords don&#39;t match', response.data)
            # assert status code
            self.assertEqual(response.status_code, 200)  # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())



