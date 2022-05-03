'''Signals of the Interactions module'''

from typing import Type
from django.db.models.signals import (
    # pre_save,
    post_save,
    # pre_delete,
    # post_delete
)
from django.dispatch import receiver
from microblog.models import MicroBlog
from .models import Interaction


@receiver(post_save, sender=MicroBlog)
def proceeding_m_creator_updater(
    sender: Type[MicroBlog],
    instance: MicroBlog,
    created: bool,
    **kwargs: [int, str]
) -> None:
    if created:
        Interaction.objects.create(
            microblog=instance,
        )
    return
