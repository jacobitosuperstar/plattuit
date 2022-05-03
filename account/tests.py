'''TEST Account Module'''
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserManagerTest(TestCase):
    def test_create_user(self):
        print("\n** Creación de Usuario **")
        '''Testbed for the account creation module.

        In this module we will evalueate, creation, values and errors.'''

        # creation
        user = User.objects.create_user(
            email='dummy@dummy.com',
            username='dummy',
            password='testbed123'
        )

        # value checking
        self.assertEqual(user.email, 'dummy@dummy.com')
        self.assertEqual(user.username, 'dummy')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)

        # error type checking
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.name)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(username='',
                                     email='dummy@dummy.com',
                                     password='testbed123')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='',
                                     email='',
                                     password='testbed123')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='',
                                     email='',
                                     password='')

    def test_create_superuser(self):
        '''Testbed for the account creation module, superuser.

        In this module we will evalueate, creation, values and errors.'''

        print("\n** Creación de Super Usuario **")
        # creation
        admin_user = User.objects.create_superuser(
            username='dummy',
            email='dummy@dummy.com',
            password='testbed123'
        )

        # value checking
        self.assertEqual(admin_user.username, 'dummy')
        self.assertEqual(admin_user.email, 'dummy@dummy.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_admin)

        # error type cheking
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.name)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_superuser()

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='',
                email='dummy@dummy.com',
                password='testbed123',
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='',
                email='',
                password='testbed123',
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='',
                email='',
                password='',
            )
