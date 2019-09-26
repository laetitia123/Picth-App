import unittest
from app.models import Pitch, User, Comment
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'laetitia',password = 'takecare1', email = 'uwizelaetitia@gmail.com')
        self.new_pitch = Pitch(id=1,title='Test',description='This is a test pitch',comments="cool",category="interview")

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.title,'Test')
        self.assertEquals(self.new_pitch.description,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
      

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)