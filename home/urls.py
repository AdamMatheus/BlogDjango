from froala_editor import views
from django.urls import path,include
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('login/',login_view,name='login_view'),
    path('register/',register_view,name='login_view'),
    path('add-blog/' , add_blog, name="add_blog"),
    path('blog-detail/<slug>' , blog_detail, name="blog_detail"),
    path('see-blog/' ,see_blog,name='see_blog' ),
    path('blog-delete/<id>' ,blog_delete,name='blog_delete' ),
    path('blog-update/<slug>/' ,blog_update,name='blog_update' ),
    path('logout-view/' ,logout_view , name='logout_view' ),
    path('verify/<token>/', verify , name ='verify'),
    path('' , post_view, name='post-list'),
    path('like/' , like_post, name='like-post'),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment' ),
    path('froala_editor/',include('froala_editor.urls')),
]

