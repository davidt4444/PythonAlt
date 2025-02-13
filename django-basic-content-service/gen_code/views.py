from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views import View
from .services import DJPostService
from .models import DJPost
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class PostView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=None):
        if id:
            post = DJPostService.get_post(id)
            if post:
                return JsonResponse(post.__dict__)
            else:
                return HttpResponseNotFound("Post not found.")
        else:
            posts = DJPostService.list_posts()
            return JsonResponse([post.__dict__ for post in posts], safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            post = DJPostService.create_post(
                title=data.get('title'),
                content=data.get('content'),
                author=data.get('author'),
                category=data.get('category'),
                author_id=data.get('author_id')
            )
            return JsonResponse(post.__dict__, status=201)
        except (ValueError, KeyError, TypeError):
            return HttpResponseBadRequest("Invalid data provided.")

    def put(self, request, id):
        try:
            data = json.loads(request.body)
            post = DJPostService.update_post(id, **data)
            if post:
                return JsonResponse(post.__dict__)
            else:
                return HttpResponseNotFound("Post not found.")
        except (ValueError, KeyError, TypeError):
            return HttpResponseBadRequest("Invalid data provided.")

    def delete(self, request, id):
        result = DJPostService.delete_post(id)
        if result[0] > 0:  # If something was deleted
            return JsonResponse({"message": "Post deleted."}, status=200)
        else:
            return HttpResponseNotFound("Post not found.")

# Additional views for specific operations
class LikePostView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        likes = DJPostService.increase_likes(id)
        if likes is not None:
            return JsonResponse({"likes": likes})
        else:
            return HttpResponseNotFound("Post not found.")

class ViewPostView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        views = DJPostService.update_views(id)
        if views is not None:
            return JsonResponse({"views": views})
        else:
            return HttpResponseNotFound("Post not found.")
        