from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['PATCH'], detail=True, url_name='like-or-dislike',
            permission_classes=[permissions.IsAuthenticated])
    def like_or_dislike(self, request, pk=None):
        user = request.user
        post = self.get_object()
        like = post.like_set.filter(who_like__exact=user.pk, post__exact=post).first()

        if like:
            like.delete()
        else:
            like = Like.objects.create(who_like=user, post=post)
            like.save()
            post.like_set.add(like)

        return Response({'post': PostSerializer(post, context={'request': request}).data})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
