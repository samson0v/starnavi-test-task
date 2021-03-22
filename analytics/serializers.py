from rest_framework import serializers


class LikeAnalyticsSerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    likes = serializers.IntegerField()
