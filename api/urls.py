from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from users import views
from posts import views as post_views
from analytics.views import PostLikeAnalyticsView

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})
user_activity = views.UserViewSet.as_view({
    'get': 'user_activity'
})

likes_detail = post_views.LikeViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'posts', PostViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),

    path('likes/<int:pk>/', likes_detail, name='like-detail'),
    path('analytics/', PostLikeAnalyticsView.as_view(), name='like-analytics'),

    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('users/<int:pk>/user_activity/', user_activity, name='user-activity'),

    path('api-sign-up-user/', views.CreateUserView.as_view(), name='user-create')
]
