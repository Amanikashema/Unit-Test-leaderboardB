import unittest
from unittest import TestCase
from website import db
from website.models import Note, Work, User, Team


class ModelsTests(unittest.TestCase):
    def tests_notes(self):
        note_info = Note(data="Hi Amani",date='20/05/2021',user_id=1)
        self.assertEqual(note_info.data,"Hi Amani")
        self.assertEqual(note_info.date,'20/05/2021')
        self.assertEqual(note_info.user_id,1)

    def tests_work(self):
        work_info = Work(id=0,title="QA Team",description="Coding is Fun",status="Online", date='20/05/2021',user_id=1, points=10)
        self.assertEqual(work_info.id, 0)
        self.assertEqual(work_info.description,"Coding is Fun")
        self.assertEqual(work_info.status,"Online")
        self.assertEqual(work_info.date, '20/05/2021')
        self.assertEqual(work_info.user_id, 1)
        self.assertEqual(work_info.points,10)

    def tests_user(self):
        user_info = User(email='amanikashema@gmail.com', password="kash123", first_name="Amani",
                         team_id=1, team_leader=False, points=13)
        self.assertEqual(user_info.email, "amanikashema@gmail.com")
        self.assertEqual(user_info.password, "kash123")
        self.assertEqual(user_info.first_name, "Amani")
        #self.assertEqual(user_info.notes, ["Code"])
        self.assertEqual(user_info.team_id, 1)
        self.assertEqual(user_info.team_leader, False)
        #self.assertEqual(user_info.work, ["Tester"])
        self.assertEqual(user_info.points, 13)

    def tests_team(self):
        team_info = Team(name="Amani")
        self.assertEqual(team_info.name,"Amani")


if __name__ == '__main__':
    unittest.main()