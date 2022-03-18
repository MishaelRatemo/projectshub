from django.test import TestCase

from .models import Profile, ProjectPosts , Ratings
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Mishael')
        self.user.save()

        self.profile_test = Profile(id=1, user='Mishael', profil_image='default.jpg', user_bio='this is a test profile',user_name='Mishael', email='test@coo.ke', phone='2345678889',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class TestProjectPosts(TestCase):
    def setUp(self):
        self.project_post_test = Profile(user='Mishael', user=User(username='Mishael'))
        self.project_post_test.save()

        self.project_post_test = ProjectPosts(landing_page='github.png', title='test', 
                                              description='test test test',
                                              link='https://githubwarehouse.netlify.app/' ,
                                              user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.project_post_test, ProjectPosts))

    def test_save_image(self):
        self.image_test.save_image()
        images = ProjectPosts.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.project_post_test.delete_image()
        after = ProjectPosts.objects.all()
        self.assertTrue(len(after) < 1)
        
