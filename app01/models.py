from django.db import models

# Create your models here.
class Department(models.Model):
    ##部门表
    title = models.CharField(verbose_name='标题',max_length=32)


class UserInfo(models.Model):
    ##用户表
    name = models.CharField(verbose_name='名字',max_length=10)
    username = models.CharField(verbose_name='账号',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=16)
    num = models.IntegerField(verbose_name='手机')
    mail = models.CharField(verbose_name='邮箱',max_length=62)
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='加入时间')
    """
    1、表和表之前约束：models.ForeignKey(to='',to_field='',on_delete=)
    2、on_delete= 1)models.CASCADE[级联删除]
                  2)models.SET_NULL[留空，需要设置表允许为空：null=Ture,blank=Ture]
    """
    depart_id = models.ForeignKey(on_delete=models.SET_NULL,null=True,blank=True,to='Department',to_field='id')
    """
    在DJANGO中给值做约束，且使用models.SmallIntegerField()来选择小的整型
    """
    gender_choices = (
        (1,"男"),
        (2,"女"),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)