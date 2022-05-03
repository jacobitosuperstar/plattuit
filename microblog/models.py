from django.db import models
from django.contrib.auth import get_user_model
# Local imports
from plattuit.utils import time_zone

User = get_user_model()


class MicroBlog(models.Model):
    '''MicroBlog objects'''

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='usuario',
    )

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='título',
    )

    body = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='cuerpo',
    )

    creation_time = models.DateTimeField(
        null=False,
        blank=False,
        default=time_zone,
        verbose_name='fecha de cración',
    )

    update_time = models.DateTimeField(
        null=False,
        blank=False,
        default=time_zone,
        verbose_name='fecha de actualización'
    )

    class Meta:
        db_table = 'microblog'
        verbose_name = ('microblog')
        verbose_name_plural = ('microblogs')

    # save method
    def save(self, *args, **kawrgs):
        self.title = self.body[:50]
        self.update_time = time_zone()
        super().save(*args, **kawrgs)

    def __str__(self):
        return f'{self.title}'
