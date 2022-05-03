from celery import shared_task
from tracking.models import Tracking
from django.db.models import F
from plattuit.utils import time_zone


@shared_task(bind=True, queue='tracking.microblog.queue')
def microblog_view_tracking(self, microblog_id: int) -> None:
    # def microblog_view_tracking(microblog_id: int) -> None:
    '''Tracking function of the microblogs visits'''
    Tracking.objects.filter(microblog__id=microblog_id).update(
        update_time=time_zone(),
        views=(F('views') + 1),
    )
    return


@shared_task(bind=True, queue='tracking.microblog.queue')
def microblog_interaction_tracking(self, microblog_id: int) -> None:
    # def microblog_interaction_tracking(microblog_id: int) -> None:
    '''Tracking function of the microblogs visits'''
    Tracking.objects.filter(microblog__id=microblog_id).update(
        update_time=time_zone(),
        interaction=(F('interaction') + 1),
    )
    return
