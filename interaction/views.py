from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_POST,
)
from django.http import (
    HttpRequest,
    JsonResponse,
)
from django.db.models import F
# local imports
from plattuit.utils import time_zone
from .models import Interaction


@require_POST
@login_required
def api_micro_blog_add_like_view(
    request: HttpRequest
) -> JsonResponse:
    '''API sends one like to the microblog

    :type info: JsonResponse
    :return info => Returns a JsonResponse with this structure

    {
        "status": int,
        "info": str,
    }
    '''
    # user = request.user
    microblog_id = request.POST.get("microblog_id")
    Interaction.objects.filter(
        microblog__id=microblog_id
    ).update(
        update_time=time_zone(),
        likes=(F('likes') + 1),
    )
    info = {
        "status": 200,
        "info": "Me Gusta agregado",
    }
    return JsonResponse(info)


@require_POST
@login_required
def api_micro_blog_add_dislike_view(
    request: HttpRequest
) -> JsonResponse:
    '''API sends one dislike to the microblog

    :type info: JsonResponse
    :return info => Returns a JsonResponse with this structure

    {
        "status": int,
        "info": str,
    }
    '''
    # user = request.user
    microblog_id = request.POST.get("microblog_id")
    Interaction.objects.filter(
        microblog__id=microblog_id
    ).update(
        update_time=time_zone(),
        dislikes=(F('dislikes') + 1),
    )
    info = {
        "status": 200,
        "info": "No me Gusta agregado",
    }
    return JsonResponse(info)
