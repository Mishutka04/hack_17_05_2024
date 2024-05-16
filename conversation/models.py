from django.db import models
from django.core.exceptions import ValidationError
import os
import conversation.utils as ut


def validate_audio_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Получаем расширение файла
    valid_extensions = ['.mp3', '.wav', '.ogg']  # Допустимые расширения
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Line(models.Model):
    """Линия связи"""
    title = models.CharField(
        verbose_name='Название',
        max_length=100
        )
    description = models.TextField(
        max_length=3000,
        verbose_name='Описание линии связи'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Линия связи'
        verbose_name_plural = 'Линии связи'


class ReferenceDialog(models.Model):
    """Эталонный диалог"""
    title = models.CharField(
        verbose_name='Название',
        max_length=100
        )
    text = models.TextField(
        max_length=3000,
        verbose_name='Текст эталонного диалога'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Эталонный диалог'
        verbose_name_plural = 'Эталонные диалоги'


class Negotiation(models.Model):
    """Служебные переговоры"""
    line = models.ForeignKey(
        Line,
        on_delete=models.CASCADE
        )
    reference_dialog = models.ForeignKey(
        ReferenceDialog,
        on_delete=models.CASCADE
        )
    title = models.CharField(
        verbose_name='Название',
        max_length=100
        )
    audio_text = models.TextField(
        verbose_name='Распознанный текст из аудио',
        null=True,
        blank=True
        )
    date = models.DateField(
        auto_now_add=True
        )
    audio_file = models.FileField(
        upload_to='negotiation_audio/',
        validators=[validate_audio_file_extension],
        verbose_name='Аудиофайл диалога',
        )
    percentage_compliance = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Процент соответвия регламенту',
    )
    regulations_complies = models.BooleanField(
        default=False,
        verbose_name='Соответсвует ли регламенту',
        )

    def save(self, *args, **kwargs):
        if self.audio_file:
            try:
                data = self.audio_file.read()
                text = ut.query_wisper(data)
                if text:
                    self.audio_text = text
                    payload = {
                        "inputs": {
                            "source_sentence": text,
                            "sentences": [
                                self.reference_dialog.text,
                            ]
                        }
                    }
                    accordance = 0.8
                    self.percentage_compliance = ut.query_sentence_transformers(payload)[0]
                    if self.percentage_compliance >= accordance:
                        self.regulations_complies=True
                    super(Negotiation, self).save(*args, **kwargs)
                else:
                    print("File does not exist:", self.audio_file.path)
            except Exception as e:
                print("Failed to extract text from audio:", e)
        else:
            super(Negotiation, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Служебные переговоры'
        verbose_name_plural = 'Служебные переговоры'
