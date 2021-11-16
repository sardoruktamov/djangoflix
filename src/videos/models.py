from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        #constant = 'DB_Value', 'User_Display_value'
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # PRIVATE = 'PR', 'Private'
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    update = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamp = None
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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