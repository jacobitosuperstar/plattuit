from django.db import models
from django.contrib.auth import get_user_model
# Local imports
from plattuit.utils import time_zone
from microblog.models import MicroBlog

User = get_user_model()


class Tracking(models.Model):
    '''Tracking Class.

    Quantifies the views of the MicroBlogs and the interaction with them.'''

    microblog = models.OneToOneField(
        MicroBlog,
        on_delete=models.CASCADE,
        related_name='tracking',
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Vistas"
    )

    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name="Interacciones"
    )

    update_time = models.DateTimeField(
        null=False,
        blank=False,
        default=time_zone,
        verbose_name='fecha de actualización'
    )

    class Meta:
        db_table = 'tracking'
        verbose_name = ('Rastreo')
        verbose_name_plural = ('Rastreos')

    # save method
    def save(self, *args, **kawrgs):
        self.update_time = time_zone()
        super().save(*args, **kawrgs)

    def __str__(self):
        return f'{self.microblog.title}'
