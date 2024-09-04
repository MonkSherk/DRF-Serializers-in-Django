from django.urls import path

from second_APP import views

urlpatterns = [
    path('get',views.GetPostList.as_view()),
    path('get/v2/',views.GetPostListGeneric()),
    path('get/v2/<int:pk>',views.GetPostById.as_view()),
    path('post/v2/',views.CreatePostGeneric.as_view()),
    path('update/v2/<int:pk>',views.UpdatePostById.as_view()),
    path('delete/v2/<int:pk>',views.DeletePostById.as_view())
]