import pathlib
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class User(AbstractUser):
    """
    Наследуем все поля из `AbstractUser`
    И добавляем новое поле `phone`
    """
    phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = "users"
        
def upload_to(instance: "Note", filename: str) -> str:
    """Путь для файла относительно корня медиа хранилища."""
    return f"{instance.uuid}/{filename}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    # Стандартный ID для каждой таблицы можно не указывать, Django по умолчанию это добавит.

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mode_time = models.DateTimeField(auto_now=True,db_index=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True, verbose_name="Превью")
    # auto_now_add=True автоматически добавляет текущую дату и время.
    
    tags = models.ManyToManyField(Tag, related_name="notes", verbose_name="Теги")
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Владелец")
    objects = models.Manager()  # Он подключается к базе.

    class Meta:
        # db_table = 'notes'  # Название таблицы в базе.
        ordering = ['mode_time']  # Дефис это означает DESC сортировку (обратную).
        indexes = [
            models.Index(fields=("created_at",), name="created_at_index"),
            models.Index(fields=("mode_time",), name="mode_at_index")
        ]





@receiver(post_delete, sender=Note)
def after_delete_note(sender, instance: Note, **kwargs):
    if instance.image:
        note_media_folder: pathlib.Path = (settings.MEDIA_ROOT / str(instance.uuid))

        for file in note_media_folder.glob("*"):
            file.unlink(missing_ok=True)
#        note_media_folder.rmdir(missing_ok=True)
        note_media_folder.rmdir()
    
# Create your models here.
