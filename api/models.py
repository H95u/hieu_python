from django.db import models


class User(models.Model):
    link_avatar = models.TextField()
    user_name = models.TextField()
    ip_register = models.TextField()
    device_register = models.TextField()
    password = models.TextField()
    email = models.TextField()
    count_sukien = models.IntegerField()
    count_comment = models.IntegerField()
    count_view = models.IntegerField()


class AddSuKien(models.Model):
    id_toan_bo_su_kien = models.TextField()
    ten_su_kien = models.TextField()
    noi_dung_su_kien = models.TextField()
    ten_nam = models.TextField()
    ten_nu = models.TextField()
    device_them_su_kien = models.TextField()
    ip_them_su_kien = models.TextField()
    link_img = models.TextField()
    link_video = models.TextField()
    id_template = models.TextField()
    thoigian_themsk = models.TextField()
    so_thu_tu_su_kien = models.IntegerField()
    count_comment = models.IntegerField()
    count_view = models.IntegerField()
    status = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    noi_dung_Comment = models.TextField()
    IP_Comment = models.TextField()
    device_Comment = models.TextField()
    id_toan_bo_su_kien = models.TextField()
    imageattach = models.TextField()
    thoi_gian_release = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.TextField()
    avatar_user = models.TextField()
    so_thu_tu_su_kien = models.IntegerField()
    location = models.TextField()


class ReportComment(models.Model):
    report_reason = models.TextField()
    content = models.TextField()
    id_user_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_reports')
    id_user_report = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_comments')


class ReportSuKien(models.Model):
    so_thu_tu_su_kien = models.IntegerField()
    report_reason = models.TextField()
    id_user_report = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sukien_reports')
    id_user_sukien = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_sukien')


class SavedImage(models.Model):
    link_image = models.TextField()
    thoigian = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class SavedNotification(models.Model):
    id_toan_bo_su_kien = models.TextField()
    user_name = models.TextField()
    link_avatar = models.TextField()
    link_imagesk = models.TextField()
    status = models.TextField()
    thoigian = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class SavedSuKien(models.Model):
    link_nam_goc = models.TextField()
    link_nu_goc = models.TextField()
    link_nam_chua_swap = models.TextField()
    link_nu_chua_swap = models.TextField()
    link_da_swap = models.TextField()
    thoigian_swap = models.TextField()
    ten_su_kien = models.TextField()
    noidung_su_kien = models.TextField()
    id_toan_bo_su_kien = models.TextField()
    so_thu_tu_su_kien = models.IntegerField()
    thoigian_sukien = models.TextField()
    device_them_su_kien = models.TextField()
    ip_them_su_kien = models.TextField()
    id_user = models.IntegerField()
    tomLuocText = models.TextField()
    ten_nam = models.TextField()
    ten_nu = models.TextField()
    count_comment = models.IntegerField()
    count_view = models.IntegerField()
    id_template = models.IntegerField()
    phantram_loading = models.IntegerField()


class SavedSuKienVideo(models.Model):
    link_video = models.TextField()
    link_image = models.TextField()
    link_da_swap = models.TextField()
    ten_su_kien = models.TextField()
    noidung_su_kien = models.TextField()
    id_video = models.TextField()
    thoigian_sukien = models.TextField()
    device_them_su_kien = models.TextField()
    ip_them_su_kien = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    count_comment = models.IntegerField()
    count_view = models.IntegerField()
