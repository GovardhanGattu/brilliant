from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class Select(models.Model):
	classes=[("VI class","VI class"),
			("VII class","VII class"),
			("VIII class","VIII class"),
			("IX class","IX class"),
			("X class","X class")]

	Subjects=[("Telugu","Telugu"),
			("Hindi","Hindi"),
			("English","English"),
			("Maths","Maths"),
			("Science","Science"),
			("Physics","Physics"),
			("Biology","Biology"),
			("Soical","Soical")]


	Class = models.CharField(max_length=50,choices=classes)
	Subject = models.CharField(max_length=50,choices=Subjects)
	


class T6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50)


class H6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50,default=" ")


class E6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50,default=" ")


class M6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50,default=" ")


class S6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50,default=" ")


class Sc6M(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    title = models.CharField(max_length=50,default=" ")
