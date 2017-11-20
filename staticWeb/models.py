from django.contrib.auth.models import AbstractUser
from django.db import models


# 成绩单
class Transcripts(models.Model):
    subject = models.CharField('学科', max_length=30)
    stu_name = models.CharField('学生姓名', max_length=30)
    stu_clas = models.CharField('班级', max_length=30)
    test1 = models.IntegerField('测验1', default = 0)
    test2 = models.IntegerField('测验2', default=0)
    test3 = models.IntegerField('测验3', default=0)
    test4 = models.IntegerField('测验4', default=0)

    class Meta:
        db_table = 'transcripts'

    def __str__(self):
        return self.subject
# 应聘信息
class Candidates(models.Model):
    title = models.CharField("标题", max_length=50)
    pxban_name = models.CharField("培训班名字",max_length=50)
    enterprise_name = models.CharField("企业名字", max_length=50)
    created_date = models.DateField("创建日期", auto_now_add=True)
    modify_date = models.DateField("修改日期", auto_now=True)
    content = models.TextField()
    is_show = models.BooleanField()


    class Meta:
        db_table = 'Candidate'

    def __str__(self):
        return self.title
# 基类
class MyUser(AbstractUser):

	tele_num = models.IntegerField('联系电话', blank = True, default= 0)

	class Meta:
		db_table='MyUser'
	def __str__(self):
		return self.username
# 学生
class Student(MyUser):

    student_id = models.AutoField('学号',primary_key=True)
    stu_class = models.CharField('班级', max_length=30)
    # 成绩单
    transcripts = models.ManyToManyField(Transcripts)
    # 收藏的应聘
    candidates = models.ManyToManyField(Candidates)

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return self.username


# 培训班
class Peixunban(models.Model):
    peixun_name = models.CharField('培训班名字', max_length=30)
    # 介绍
    introduction = models.TextField()
    # 学生
    students = models.ManyToManyField(Student)
    # 招聘信息
    candidates = models.ManyToManyField(Candidates)

    class Meta:
        db_table = 'Peixunban'

    def __str__(self):
        return self.peixun_name


# 企业
class Enterprise(MyUser):
    # 企业介绍
    en_troduction = models.TextField()

    #定制的培训班
    peixunban = models.ManyToManyField(Peixunban)

    class Meta:
        db_table = 'Enterprise'
    def __str__(self):
        return self.username


# 写模型的方法：
# 下层对象写上层对象名字
# 上层对象包含下层对象


