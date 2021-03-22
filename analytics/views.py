from django.db.models import Count
from rest_framework.response import Response
from rest_framework import permissions, generics
from django_filters import rest_framework as filters
from django.db.models.functions import TruncDay

from .filters import LikeFilter
from posts.models import Like
from posts.serializers import LikeSerializer
from .serializers import LikeAnalyticsSerializer


class PostLikeAnalyticsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeFilter
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def list(self, request, *args, **kwargs):
        """
        Function return analytics about how many likes was made per day in specific range.
        If day haven't likes, it is pass.

        :return: Response obj
        """
        output_data = self.filter_queryset(self.queryset).annotate(day=TruncDay('timestamp')).values('day').annotate(
            likes=Count('id')).values('day', 'likes')

        return Response(LikeAnalyticsSerializer(output_data, many=True).data)
