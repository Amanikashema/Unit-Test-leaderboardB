from website.tests.unit.base_test import BaseTest, db
from website.models import Note, Work, User, Team


class TestModelsCrud(BaseTest):
    # testing that notes can be saved and deleted from the database
    def test_note_crud(self):
        with self.app_context:

            # Create new notes
            new_note = Note(data="New memo or stuff")

            # Assert that this item does not exist in db
            results = db.session.query(Note).filter_by(data="New memo or stuff").first()
            self.assertIsNone(results)

            # save to db
            db.session.add(new_note)
            db.session.commit()

            # Delete from db
            db.session.delete(new_note)
            db.session.commit()

            # Assert it no longer exist in db
            results = db.session.query(Note).filter_by(data="New memo or stuff").first()
            self.assertIsNone(results)

    def test_work(self):
        with self.app_context:
            # Create new notes
            work_info = Work(description="Coding is Fun", title="QA Team")

            # Assert that this item does not exist in db
            results = db.session.query(Work).filter_by(description="Coding is Fun",title="QA Team").first()
            self.assertIsNone(results)

            # save to db
            db.session.add(work_info)
            db.session.commit()

            # Delete from db
            db.session.delete(work_info)
            db.session.commit()

            # Assert it no longer exist in db
            results = db.session.query(Work).filter_by(description="Coding is Fun",title="QA Team").first()
            self.assertIsNone(results)

    def test_user(self):
        with self.app_context:
            # Create new notes
            user_info = User(email='amanikashema@gmail.com', password="kash123", first_name="Amani",
                             team_id=1, team_leader=False, points=13)

            # Assert that this item does not exist in db
            results = db.session.query(User).filter_by(email='amanikashema@gmail.com', password="kash123", first_name="Amani",
                             team_id=1, team_leader=False, points=13).first()
            self.assertIsNone(results)

            # save to db
            db.session.add(user_info)
            db.session.commit()

            # Delete from db
            db.session.delete(user_info)
            db.session.commit()

            # Assert it no longer exist in db
            results = db.session.query(User).filter_by(email='amanikashema@gmail.com', password="kash123", first_name="Amani",
                             team_id=1, team_leader=False, points=13).first()
            self.assertIsNone(results)

    def test_team(self):
        with self.app_context:
            team_info = Team(name="Amani")

            # Assert that this item does not exist in db
            results = db.session.query(Team).filter_by(name="Amani").first()
            self.assertIsNone(results)

            # save to db
            db.session.add(team_info)
            db.session.commit()

            # Delete from db
            db.session.delete(team_info)
            db.session.commit()

            # Assert it no longer exist in db
            results = db.session.query(Team).filter_by(name="Amani").first()
            self.assertIsNone(results)





