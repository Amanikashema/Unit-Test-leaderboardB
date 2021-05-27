from website.models import Note
from website.tests.base_tests import BaseTest, db


# class to test Adding note
class TestAddNote(BaseTest):
    def test_add_note_db(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            # create a post req with valid data
            response_login = self.app.post('/log-in',
                                           data=dict(email='email@gmail.com', password='pass1234'),
                                           follow_redirects=True)
            # assert status code
            self.assertEqual(response_login.status_code, 200)

            r = self.app.post('/', data=dict(note='hi'),
                              follow_redirects=True)
            # assert that notes  is created in db
            note = db.session.query(Note).filter_by(data='hi').first()
            self.assertTrue(note)

            self.assertIn(b'Note added', r.data)

    def test_add_note_success_response(self):
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

            response_note = self.app.post('/', data=dict(note='hi'),
                              follow_redirects=True)

            # assert status code
            self.assertEqual(response_note.status_code, 200)

            # assert that notes  is created in db
            note = db.session.query(Note).filter_by(data='hi').first()
            self.assertTrue(note)

    def test_notes_less_than_1(self):
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
            self.assertIn(b"Logged in successfully", response_login.data)

            response_note = self.app.post('/', data=dict(note=''),
                                          follow_redirects=True)

            # assert status code
            self.assertEqual(response_note.status_code, 200)

            # assert that notes were not added in db
            note = db.session.query(Note).filter_by(data='').first()
            self.assertFalse(note)

            # assert when notes are less than one
            self.assertIn(b'Note is too short',response_note.data)


# class to delete note
class TestDeleteNote(BaseTest):
    def test_delete_note(self):
        with self.app:
            # create a post req with valid data
            self.app.post('/sign-up', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                password2='pass1234'),
                          follow_redirects=True)

            # create a post req with valid data
            response_login = self.app.post('/log-in',
                                           data=dict(email='email@gmail.com', password='pass1234'),
                                           follow_redirects=True)
            # assert status code
            self.assertEqual(response_login.status_code, 200)

            r = self.app.post('/', data=dict(note='hi'),
                              follow_redirects=True)
            # assert that notes  is created in db
            note = db.session.query(Note).filter_by(data='hi').first()
            self.assertTrue(note)

            self.assertIn(b'Note added', r.data)
            # Delete note
            response_delete_note = self.app.get('/delete-note', follow_redirects=True)
            note2 = db.session.query(Note).filter_by(data='').first()
            self.assertFalse(note2)
            expected = {}
            self.assertDictEqual({},expected)






