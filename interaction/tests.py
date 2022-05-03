'''Test Interaction functionality'''
import time
import json
from django.test import (
    TestCase,
    Client,
)
from django.contrib.auth import get_user_model
from .models import MicroBlog
# from celery.contrib.testing.worker import start_worker

User = get_user_model()


class InteractionFunctionalityTest(TestCase):

    def test_micro_blog_list_add_like(self):
        """Test of api_micro_blog_add_like_view and
        api_micro_blog_add_dislike_view"""
        print("\n** microblog vista general  con Likes y Dislikes**")

        # user creation
        user = User.objects.create_user(
            email='dummy@dummy.com',
            username='dummy',
            password='testbed123'
        )

        # micro blog creation
        dumy_text = (
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "
            "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis "
            "natoque penatibus et magnis dis parturient montes, nascetur "
            "ridiculus mus. Donec qu"
        )

        MicroBlog.objects.create(
            user=user,
            body=dumy_text,
        )

        # client
        c = Client()
        c.force_login(user)

        # adding the like
        response = c.post(
            "/interaction/api/like/",
            data={"microblog_id": self.microblog.id},
        )
        print("Added Like")
        print(json.loads(response.content))

        # adding the dislike
        response = c.post(
            "/interaction/api/dislike/",
            data={"microblog_id": self.microblog.id},
        )
        print("Added DisLike")
        print(json.loads(response.content))

        # Checking the blog after 30 seconds
        time.sleep(30)
        print('esperando')

        response = c.get(
            f"/api/microblog/{self.microblog.id}/",
        )
        content = json.loads(response.content)
        print(content)

        microblog_likes = content.get("microblog").get("me_gusta")
        result_likes = bool(microblog_likes == 1)
        microblog_dislikes = content.get("microblog").get("no_me_gusta")
        result_dislikes = bool(microblog_dislikes == 1)
        result = bool(result_likes and result_dislikes)

        print("Eliminando el usuario")
        User.objects.filter(id=self.user.id).delete()
        print("Eliminando el blog")
        MicroBlog.objects.filter(id=self.microblog.id).delete()
        self.assertTrue(result)
