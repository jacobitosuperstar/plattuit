'''Interaction module between the user and the micro blog'''
from django.db import models
from django.contrib.auth import get_user_model
# local imports
from plattuit.utils import time_zone
from microblog.models import MicroBlog

User = get_user_model()


class Interaction(models.Model):
    '''Interactions of the microblog objects'''

    microblog = models.OneToOneField(
        MicroBlog,
        on_delete=models.CASCADE,
        related_name='interaction',
    )

    likes = models.PositiveIntegerField(
        default=0,
        verbose_name="Me gusta"
    )

    dislikes = models.PositiveIntegerField(
        default=0,
        verbose_name="No me gusta"
    )

    update_time = models.DateTimeField(
        null=False,
        blank=False,
        default=time_zone,
        verbose_name='fecha de actualización'
    )

    class Meta:
        db_table = 'interaction'
        verbose_name = ('interacción')
        verbose_name_plural = ('interacciones')

    # save method
    def save(self, *args, **kawrgs):
        self.update_time = time_zone()
        super().save(*args, **kawrgs)

    def __str__(self):
        return f'{self.microblog.title}'
