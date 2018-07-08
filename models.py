from django.db import models

# Create your models here.
class lesson(models.Model):
    DateTime = models.DateTimeField('日付')
    StudentID = models.CharField('生徒番号', max_length=255)
    TeacherID = models.CharField('講師番号', max_length=255)
    Subject = models.CharField('教科', max_length=255)
    Subject_Unit = models.CharField('単元', max_length=255)
    Textbook = models.CharField('テキスト',max_length=255)
    Rating = models.CharField('評価', max_length=255)
    Rating_Reason = models.CharField('コメント', max_length=255)
    HomeworkID = models.CharField('宿題番号', max_length=255)