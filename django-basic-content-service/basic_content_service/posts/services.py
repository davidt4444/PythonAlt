from .models import DJPost
from django.core.exceptions import ObjectDoesNotExist

class DJPostService:
    @staticmethod
    def create_post(title, content, author=None, category=None, author_id=None):
        """
        Create a new post with the given details.
        """
        post = DJPost(
            title=title,
            content=content,
            author=author,
            category=category,
            author_id=author_id
        )
        post.save()
        return post

    @staticmethod
    def get_post(post_id):
        """
        Retrieve a post by its ID.
        """
        try:
            return DJPost.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_post(post_id, **kwargs):
        """
        Update the post with the given ID with the provided attributes.
        """
        try:
            post = DJPost.objects.get(id=post_id)
            for key, value in kwargs.items():
                if hasattr(post, key):
                    setattr(post, key, value)
            post.updated_at = timezone.now()
            post.save()
            return post
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_post(post_id):
        """
        Delete the post with the given ID.
        """
        return DJPost.objects.filter(id=post_id).delete()

    @staticmethod
    def list_posts():
        """
        List all posts.
        """
        return DJPost.objects.all()

    @staticmethod
    def increase_likes(post_id):
        """
        Increase the likes count for the post with the given ID.
        """
        try:
            post = DJPost.objects.get(id=post_id)
            post.likes_count += 1
            post.save()
            return post.likes_count
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_views(post_id):
        """
        Increment the view count for the post with the given ID.
        """
        try:
            post = DJPost.objects.get(id=post_id)
            post.views += 1
            post.save()
            return post.views
        except ObjectDoesNotExist:
            return None