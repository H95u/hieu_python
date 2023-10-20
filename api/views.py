from rest_framework import generics, status
from rest_framework.response import Response

from .models import AddSuKien, Comment, ReportComment, ReportSuKien, SavedImage, SavedNotification, SavedSuKien, \
    SavedSuKienVideo, User, UserCommentDTO
from .serializers import AddSuKienSerializer, CommentSerializer, ReportCommentSerializer, ReportSuKienSerializer, \
    SavedImageSerializer, SavedNotificationSerializer, SavedSuKienSerializer, SavedSuKienVideoSerializer, \
    UserSerializer, UserCommentDTOSerializer


class AddSuKienList(generics.ListCreateAPIView):
    queryset = AddSuKien.objects.all()
    serializer_class = AddSuKienSerializer


class AddSuKienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddSuKien.objects.all()
    serializer_class = AddSuKienSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        ip_comment = self.request.query_params.get('ip')
        user_id = self.request.query_params.get('user')
        if ip_comment is not None:
            queryset = queryset.filter(IP_Comment__icontains=ip_comment)
        elif user_id is not None:
            queryset = queryset.filter(id_user=user_id)
        return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReportCommentList(generics.ListCreateAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer


class ReportCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer


class ReportSuKienList(generics.ListCreateAPIView):
    queryset = ReportSuKien.objects.all()
    serializer_class = ReportSuKienSerializer


class ReportSuKienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportSuKien.objects.all()
    serializer_class = ReportSuKienSerializer


class SavedImageList(generics.ListCreateAPIView):
    queryset = SavedImage.objects.all()
    serializer_class = SavedImageSerializer


class SavedImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedImage.objects.all()
    serializer_class = SavedImageSerializer


class SavedNotificationList(generics.ListCreateAPIView):
    queryset = SavedNotification.objects.all()
    serializer_class = SavedNotificationSerializer


class SavedNotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedNotification.objects.all()
    serializer_class = SavedNotificationSerializer


class SavedSuKienList(generics.ListCreateAPIView):
    queryset = SavedSuKien.objects.all()
    serializer_class = SavedSuKienSerializer


class SavedSuKienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedSuKien.objects.all()
    serializer_class = SavedSuKienSerializer


class SavedSuKienVideoList(generics.ListCreateAPIView):
    queryset = SavedSuKienVideo.objects.all()
    serializer_class = SavedSuKienVideoSerializer


class SavedSuKienVideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedSuKienVideo.objects.all()
    serializer_class = SavedSuKienVideoSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        email = self.request.query_params.get('email')
        ip_register = self.request.query_params.get('ip')
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        elif ip_register is not None:
            queryset = queryset.filter(ip_register__icontains=ip_register)

        return queryset


class UserCommentList(generics.ListCreateAPIView):
    serializer_class = UserCommentDTOSerializer

    def get_queryset(self):
        queryset = []
        comment = self.request.query_params.get('comment')
        add_su_kien = self.request.query_params.get('event')

        if comment is not None:
            search_by_comment(comment, queryset)
        elif add_su_kien is not None:
            search_by_addsukien(add_su_kien, queryset)

        return queryset


def search_by_comment(comment, queryset):
    comments = Comment.objects.filter(noi_dung_Comment__icontains=comment)
    users = User.objects.all()
    matched_comments = comments.filter(id_user__in=users)
    for user in users:
        user_matched_comments = matched_comments.filter(id_user=user.id)
        for comment in user_matched_comments:
            user_comment_dto = UserCommentDTO(user, comment.noi_dung_Comment, "")
            queryset.append(user_comment_dto)


def search_by_addsukien(add_su_kien, queryset):
    event = AddSuKien.objects.filter(ten_su_kien__icontains=add_su_kien)
    users = User.objects.all()
    matched_event = event.filter(id_user__in=users)
    for user in users:
        user_matched_event = matched_event.filter(id_user=user.id)
        for event in user_matched_event:
            user_event_dto = UserCommentDTO(user, "", event.ten_su_kien)
            queryset.append(user_event_dto)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        remaining_users = User.objects.all()
        remaining_users_data = UserSerializer(remaining_users, many=True).data

        return Response(remaining_users_data, status=status.HTTP_200_OK)

