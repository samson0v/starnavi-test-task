from rest_framework import serializers

from posts.models import Post, Like


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(many=False, view_name='api:user-detail', read_only=True)
    like_or_dislike = serializers.HyperlinkedIdentityField(view_name='api:post-like-or-dislike', many=False)
    like_set = serializers.HyperlinkedRelatedField(many=True, view_name='api:like-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:post-detail', many=False)

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'text', 'author', 'like_or_dislike', 'created', 'like_set']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'who_like', 'post', 'timestamp']
