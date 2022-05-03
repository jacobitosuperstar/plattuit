'''Test MicroBlog functionality'''
import json
from django.test import (
    TestCase,
    Client,
)
from django.contrib.auth import get_user_model
from .models import MicroBlog

User = get_user_model()


class MicroBlogFunctionalityTest(TestCase):
    def test_micro_blog_creation_fine(self):
        """Test of api_micro_blog_create_view"""
        print("\n** microblog creación -> MicroBlog con Cuerpo **")
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
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("status"), 200)

    def test_micro_blog_creation_errror(self):
        """Test of api_micro_blog_create_view"""
        print("\n** microblog creación -> MicroBlog sin Cuerpo **")
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
        dumy_text = ""

        response = c.post(
            "/api/microblog/create/",
            data={"body": dumy_text},
        )
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("status"), 403)

    def test_micro_blog_list(self):
        """Test of api_micro_blog_list_view"""
        print("\n** microblog vista general **")
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
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("status"), 200)

    def test_micro_blog_detail_existing(self):
        """Test of api_micro_blog_detail_view"""
        print("\n** microblog vista detalle -> MicroBlog Existente **")
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
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("status"), 200)

    def test_micro_blog_detail_non_existing(self):
        """Test of api_micro_blog_detail_view"""
        print("\n** microblog vista detalle -> MicroBlog no Existente **")
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
        response = c.get("/api/microblog/10000/")
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content.get("status"), 404)
