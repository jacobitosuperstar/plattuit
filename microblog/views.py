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
    '''API sends lists of all microblogs'''
    microblogs = MicroBlog.objects.all()
    microblogs_list = [{
        "título": microblog.title,
        "me gusta": 0,
        "no me gusta": 0,
        "vistas": 0,
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
    '''API sends detailed view of a microblog'''
    try:
        microblog = MicroBlog.objects.select_related(
            "user",
        ).get(
            id=microblog_id,
        )
        microblog = {
            "usuario": microblog.user.username,
            "cuerpo": microblog.body,
            "fecha_creación": microblog.creation_time,
            "me gusta": 0,
            "no me gusta": 0,
            "vistas": 0,
        }
        info = {
            "status": 200,
            "microblog": microblog,
        }
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
    '''API sends lists of all microblogs'''
    user = request.user
    body = request.POST.get("body")
    body = body[:200]
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
