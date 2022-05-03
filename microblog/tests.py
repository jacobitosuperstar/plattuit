'''Test MicroBlog functionality'''
from django.test import (
    TestCase,
    Client,
)
from django.contrib.auth import get_user_model
from .models import MicroBlog

User = get_user_model()


class MicroBlogFunctionalityTest(TestCase):
    def test_micro_blog_creation(self):
        """Test of all microblog views"""
        # user creation
        user = User.objects.create_user(
            email='dummy@dummy.com',
            username='dummy',
            password='testbed123'
        )

        # client
        c = Client()
        c.force_login(user)

        # Creation of the blog
        dumy_text = (
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "
            "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis "
            "natoque penatibus et magnis dis parturient montes, nascetur "
            "ridiculus mus. Donec qu"
        )
        response = c.post(
            "/api/microblog/create/",
            data={"body": dumy_text},
        )
        print("\n** microblog creación **")
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_micro_blog_list(self):
        """Test of all microblog views"""
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

        # Creation of the blog
        response = c.get(
            "/api/microblog/",
        )
        print("\n** microblog vista general **")
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_micro_blog_detail(self):
        """Test of all microblog views"""
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
        micro_blog = MicroBlog.objects.create(
            user=user,
            body=dumy_text,
        )

        # client
        c = Client()
        c.force_login(user)

        # Creation of the blog
        response = c.get(
            f"/api/microblog/{micro_blog.id}/",
        )
        print("\n** microblog vista detalle **")
        print(response)
        self.assertEqual(response.status_code, 200)
