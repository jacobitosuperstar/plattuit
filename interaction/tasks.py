from celery import shared_task
from interaction.models import Interaction
from django.db.models import F
# from plattuit.utils import time_zone
from microblog.models import MicroBlog


@shared_task(bind=True, queue='interaction.microblog.queue')
def microblog_interaction_tracking_likes(self, microblog_id: int) -> None:
    # def microblog_interaction_tracking_likes(microblog_id: int) -> None:
    '''Tracking function of the microblogs visits'''
    print("*** microblog_interaction_tracking_likes ***")
    print(microblog_id)
    try:
        microblog = MicroBlog.objects.get(id=microblog_id)
        interaction = Interaction.objects.get(
            microblog=microblog,
        )
        interaction.likes = F('likes') + 1
        interaction.save()
        # interaction.save(update_fields=["likes"])
    except Exception as e:
        print(e)


@shared_task(bind=True, queue='interaction.microblog.queue')
def microblog_interaction_tracking_dislikes(self, microblog_id: int) -> None:
    # def microblog_interaction_tracking_dislikes(microblog_id: int) -> None:
    '''Tracking function of the microblogs visits'''
    print("*** microblog_interaction_tracking_dislikes ***")
    print(microblog_id)
    try:
        microblog = MicroBlog.objects.get(id=microblog_id)
        interaction = Interaction.objects.get(
            microblog=microblog,
        )
        interaction.dislikes = F('dislikes') + 1
        interaction.save()
        # interaction.save(update_fields=["dislikes"])
    except Exception as e:
        print(e)
