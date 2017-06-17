from django.db import models


# Create your models here.

class UserProfile(models.Model):
    """
    用户表
    """
    user_info = models.OneToOneField('UserInfo')
    username = models.CharField(max_length=64, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")

    def __unicode__(self):
        return self.username


class UserInfo(models.Model):
    """
    用户信息表
    """
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'管理员'),
    )
    user_type = models.IntegerField(choices=user_type_choice, verbose_name="用户类型")
    nick_name = models.CharField(max_length=32, verbose_name="昵称")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    phone = models.CharField(max_length=16, verbose_name="手机号")
    create_time = models.DateTimeField(max_length=32, verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


