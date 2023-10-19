from rest_framework import serializers
from .models import AddSuKien, Comment, ReportComment, ReportSuKien, SavedImage, SavedNotification, SavedSuKien, \
    SavedSuKienVideo, User


class AddSuKienSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSuKien
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReportCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportComment
        fields = '__all__'


class ReportSuKienSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSuKien
        fields = '__all__'


class SavedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedImage
        fields = '__all__'


class SavedNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedNotification
        fields = '__all__'


class SavedSuKienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSuKien
        fields = '__all__'


class SavedSuKienVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSuKienVideo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
