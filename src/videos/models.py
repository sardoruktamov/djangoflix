from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)
    # timestamp
    # update
    # state

    @property
    def is_published(self):
        return self.active

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "All video"
        verbose_name_plural = "All videos"

class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published video"
        verbose_name_plural = "Published videos"