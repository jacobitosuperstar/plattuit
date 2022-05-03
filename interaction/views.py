from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_POST,
)
from django.http import (
    HttpRequest,
    JsonResponse,
)
# local imports
from interaction.tasks import (
    microblog_interaction_tracking_likes,
    microblog_interaction_tracking_dislikes,
)
from tracking.tasks import (
    microblog_interaction_tracking,
)


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

    # calling the celery task
    microblog_interaction_tracking_likes.apply_async(
        args=[microblog_id],
        countdown=0
    )
    # microblog_interaction_tracking_likes(microblog_id)

    # grabando las interacciones
    microblog_interaction_tracking.apply_async(
        args=[microblog_id],
        countdown=0
    )
    # microblog_interaction_tracking(microblog_id)

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

    # calling the celery task
    microblog_interaction_tracking_dislikes.apply_async(
        args=[microblog_id],
        countdown=0
    )
    # microblog_interaction_tracking_dislikes(microblog_id)

    # grabando las interacciones
    microblog_interaction_tracking.apply_async(
        args=[microblog_id],
        countdown=0
    )
    # microblog_interaction_tracking(microblog_id)

    info = {
        "status": 200,
        "info": "No me Gusta agregado",
    }
    return JsonResponse(info)
