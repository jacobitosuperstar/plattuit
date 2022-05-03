from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_POST, require_GET,
)
from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)
# local imports
from .models import MicroBlog
from tracking.tasks import microblog_view_tracking


# landing page

def micro_blog_view(request: HttpRequest) -> HttpResponse:
    '''Landing page micro blogs'''
    context = {}
    template = 'microblog/microblog.html'
    return render(request, template, context)


# microblogs list

@require_GET
@login_required
def api_micro_blog_list_view(
    request: HttpRequest,
) -> JsonResponse:
    '''API sends lists of all microblogs

    :type info: JsonResponse
    :return info => Returns a JsonResponse with this structure
    {
        "status": int,
        "título": str,
        "me_gusta": int,
        "no_me_gusta": int,
        "vistas": int,
    }
    '''
    microblogs = MicroBlog.objects.prefetch_related(
        "interaction",
        "tracking",
    ).all()
    microblogs_list = [{
        "título": microblog.title,
        "me_gusta": microblog.interaction.likes,
        "no_me_gusta": microblog.interaction.dislikes,
        "vistas": microblog.tracking.views,
    }for microblog in microblogs]
    info = {
        "status": 200,
        "microblogs_list": microblogs_list,
    }
    return JsonResponse(info)


# microblog detailed view

@require_GET
@login_required
def api_micro_blog_detail_view(
    request: HttpRequest,
    microblog_id: int,
) -> JsonResponse:
    '''API sends detailed view of a microblog

    :type info: JsonResponse
    :return info => Returns a JsonResponse with this structure if the MicroBlog
    exists

    {
        "status": int,
        "cuerpo": str,
        "fecha_creación": str,
        "me_gusta": int,
        "no_me_gusta": int,
        "vistas": int,
    }

    else

    {
        "status": int,
        "info": str,
    }
    '''
    try:
        microblog = MicroBlog.objects.select_related(
            "user",
        ).prefetch_related(
            "interaction",
            "tracking",
        ).get(
            id=microblog_id,
        )
        microblog = {
            "usuario": microblog.user.username,
            "cuerpo": microblog.body,
            "fecha_creación": microblog.creation_time,
            "me_gusta": microblog.interaction.likes,
            "no_me_gusta": microblog.interaction.dislikes,
            "vistas": microblog.tracking.views,
        }
        info = {
            "status": 200,
            "microblog": microblog,
        }

        # contando las vistas
        # microblog_view_tracking.apply_async(
        #     args=[microblog_id],
        #     countdown=0
        # )
        microblog_view_tracking(microblog_id)

    except MicroBlog.DoesNotExist:
        info = {
            "status": 404,
            "info": "el microblog que estás buscando no existe"
        }
    return JsonResponse(info)


# microblog creation view

@require_POST
@login_required
def api_micro_blog_create_view(
    request: HttpRequest
) -> JsonResponse:
    '''API sends lists of all microblogs

    :type info: JsonResponse
    :return info => Returns a JsonResponse with this structure if the MicroBlog
    could be created

    {
        "status": int,
        "microblog_id": int,
    }

    else

    {
        "status": int,
        "info": str,
    }
    '''
    user = request.user
    body = request.POST.get("body")
    body = body[:200]
    if len(body) == 0:
        info = {
            "status": 403,
            "info": "No se puede crear un MicroBlog sin cuerpo",
        }
        return JsonResponse(info)
    try:
        microblog = MicroBlog.objects.create(
            user=user,
            body=body,
        )
        info = {
            "status": 200,
            "microblogs_id": microblog.id,
        }
    except ValueError:
        info = {
            "status": 403,
            "info": "Revisa la información que estás ingresando al sistema",
        }
    return JsonResponse(info)
