from rest_framework import generics

from .models import AddSuKien, Comment, ReportComment, ReportSuKien, SavedImage, SavedNotification, SavedSuKien, \
    SavedSuKienVideo, User
from .serializers import AddSuKienSerializer, CommentSerializer, ReportCommentSerializer, ReportSuKienSerializer, \
    SavedImageSerializer, SavedNotificationSerializer, SavedSuKienSerializer, SavedSuKienVideoSerializer, UserSerializer


class AddSuKienList(generics.ListCreateAPIView):
    queryset = AddSuKien.objects.all()
    serializer_class = AddSuKienSerializer


class AddSuKienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddSuKien.objects.all()
    serializer_class = AddSuKienSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


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
            queryset = queryset.filter(email__contains=email)
        elif ip_register is not None:
            queryset = queryset.filter(ip_register__contains=ip_register)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
