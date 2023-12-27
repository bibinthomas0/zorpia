from django.urls import path
from . import views



urlpatterns = [
    path("createpost/", views.CreatePost.as_view(), name="create-post"),
    path("listpost/", views.PostListView.as_view(), name="list-post"),
    path("likepost/", views.PostLikeView.as_view(), name="list-like"),
    path("createcomment/", views.CommentCreate.as_view(), name="create-comment"),
    path("listcomment/", views.CommentList.as_view(), name="list-comment"),
    path("createcallout/", views.AddCallout.as_view(), name="createcallout"),
    path("follow/", views.FollowManagementApi.as_view(), name="follow"),
    path('getprofilephoto/',views.ProfileImage.as_view(),name="getprofilephoto"),
    path('getcoverphoto/',views.CoverImage.as_view(),name="getcoverphoto"),
    path('profilelistpost/',views.ProfilePostListView.as_view(),name="profilelistpost"),
    path('checkfollow/',views.FollowPostChecking.as_view(),name="checkfollow"),
    path('followingList/',views.FollowingUsers.as_view(),name="followingList"),
    path('followersList/',views.FollowersUsers.as_view(),name="followersList"),

]    