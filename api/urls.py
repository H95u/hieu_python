from django.urls import path
from .views import AddSuKienList, AddSuKienDetail, CommentList, CommentDetail, ReportCommentList, ReportCommentDetail, \
    ReportSuKienList, ReportSuKienDetail, SavedImageList, SavedImageDetail, SavedNotificationList, \
    SavedNotificationDetail, SavedSuKienList, SavedSuKienDetail, SavedSuKienVideoList, SavedSuKienVideoDetail, UserList, \
    UserDetail, UserCommentList

urlpatterns = [
    path('add_sukien/', AddSuKienList.as_view()),
    path('add_sukien/<int:pk>/', AddSuKienDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('report_comment/', ReportCommentList.as_view()),
    path('report_comment/<int:pk>/', ReportCommentDetail.as_view()),
    path('report_sukien/', ReportSuKienList.as_view()),
    path('report_sukien/<int:pk>/', ReportSuKienDetail.as_view()),
    path('saved_image/', SavedImageList.as_view()),
    path('saved_image/<int:pk>/', SavedImageDetail.as_view()),
    path('saved_notification/', SavedNotificationList.as_view()),
    path('saved_notification/<int:pk>/', SavedNotificationDetail.as_view()),
    path('saved_sukien/', SavedSuKienList.as_view()),
    path('saved_sukien/<int:pk>/', SavedSuKienDetail.as_view()),
    path('saved_sukien_video/', SavedSuKienVideoList.as_view()),
    path('saved_sukien_video/<int:pk>/', SavedSuKienVideoDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/filter/', UserCommentList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
