'''Test Interaction functionality'''
import json
from django.test import (
    TestCase,
    Client,
)
from django.contrib.auth import get_user_model
from .models import MicroBlog

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

        microblog = MicroBlog.objects.create(
            user=user,
            body=dumy_text,
        )

        # client
        c = Client()
        c.force_login(user)

        # adding the like
        response = c.post(
            "/interaction/api/like/",
            data={"microblog_id": microblog.id},
        )
        print("Added Like")
        print(json.loads(response.content))

        # adding the dislike
        response = c.post(
            "/interaction/api/dislike/",
            data={"microblog_id": microblog.id},
        )
        print("Added DisLike")
        print(json.loads(response.content))

        # Creation of the blog
        response = c.get(
            f"/api/microblog/{microblog.id}/",
        )
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("microblog").get("me_gusta"), 1)
        self.assertEqual(content.get("microblog").get("no_me_gusta"), 1)
