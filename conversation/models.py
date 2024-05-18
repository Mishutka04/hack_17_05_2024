from django.db import models
from django.core.exceptions import ValidationError
import os
import conversation.utils as ut
import re


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
    comment = models.TextField(
        verbose_name='Комментарий модели',
        null=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        if self.audio_file:
            try:
                data = self.audio_file.read()
                text = ut.query_wisper(data)
                if text:
                    self.audio_text = str(text)
                    payload = {
                        "inputs": {
                            "source_sentence": text,
                            "sentences": [
                                self.reference_dialog.text,
                            ]
                        }
                    }
                    accordance = 0.77
                    self.percentage_compliance = ut.query_sentence_transformers(payload)[0]
                    text_for_nlp = f"""Есть ли в этом тексте нарушения КЛАССИФИКАТОРА

нарушений регламента служебных переговоров при поездной и маневровой работе

Степень Классификация Пример нарушения Мера ответственности
1 степень упрощение - не называется фамилия, должность работника

или позывной;
- сокращение установленных форм;
- непередача показаний светофоров по маршруту
следования;
- прочие упрощения установленного регламента,
не указанные ниже

- производственный инструктаж с
записью
в журнале инструктажей работникам
хозяйства перевозок;
- при повторных нарушениях -
возможно изъятие талона
предупреждения зеленого цвета

посторонние
разговоры

- ведение разговоров, не относящихся к
выполнению должностных обязанностей

2 степень нарушение
порядка
взаимоконтроля

- передача команды (сообщения) не лаконично
(не четко, непонятно);
- неубеждение в правильности восприятия
команды;
- неуказание места нахождения руководителя
маневров при движении маневрового состава
вагонами вперед;
- нарушение руководителем маневров
периодичности сообщений машинисту при
движении вагонами вперед

- изъятие талона предупреждения
зеленого цвета
у работников хозяйства перевозок
и направление на собеседование
к начальнику центра организации
работы железнодорожных станций
(для Калининградской дирекции -
в дирекцию управления движением).

4

Степень Классификация Пример нарушения Мера ответственности
3 степень нарушение
порядка
передачи
указания,
которое может
привести к
нарушению
безопасности
движения или
травмированию

- передача указания по нерегистрируемым
средствам связи (при наличии исправной
регистрируемой связи);
- непередача сообщения о неполном
приготовлении маршрута;
- непередача сообщения о расстоянии
до сцепления с вагонами;
- нарушение регламента переговоров при приеме,
отправлении поезда при запрещающем показании
входного или выходного светофоров (не указание
литера светофора, номера приказа, фамилии ДСП,
номера поезда, сведения о готовности
маршрута...);
- нарушение регламента служебных переговоров
при производстве маневровой работы при
запрещающем показании маневрового светофоров
(не указание литера светофора, фамилии ДСП,
номера поезда, сведения о готовности маршрута
...);
- передача машинисту разрешения на отцепку
локомотива без получения доклада о закреплении
состава;
- не указание сторонности закрепления

- изъятие талона предупреждения
желтого цвета у работников
хозяйства перевозок,
- лишение премиального
вознаграждения на основании
Положения о премировании,
при необходимости - применение
к работнику мер дисциплинарного
воздействия в соответствии
со статьей 192 ТК РФ;

подвижного состава;
- передача разрешения на изъятие тормозных
башмаков без получения доклада от машиниста о
прицепке локомотива;
- движение без получения команды от

5

Степень Классификация Пример нарушения Мера ответственности

руководителя маневров

4 степень нарушения,
повлекшие за
собой
нарушение БД
или
травмирование
работников,
пользователей
услуг ж.д.
транспорта,
посторонних
людей

- невыполнение порядка ведения регламента
служебных переговоров, приведшие к нарушениям
безопасности движения или травмированию

- изъятие талона предупреждения
красного цвета,
а также рассмотрение вопроса о
привлечении работника мер
дисциплинарной ответственности в
соответствии со статьей 192 ТК РФ;
- назначение внеочередной
аттестации работникам хозяйства
перевозок в соответствии с пунктом
13 Положения о проведении
аттестации работников ОАО «РЖД»,
производственная деятельность
которых связана с движением поездов
и маневровой работой на
железнодорожных путях общего
пользования ОАО «РЖД».: {text}. Есть есть то какие"""
                    comment = ut.query_predict_nlp(text_for_nlp)
                    # text_for_nlp = f"""Есть ли в этом тексте нарушение регламента переговоров РЖД: {text}. Есть есть то какие"""
                    # print(ut.query_predict_nlp(text_for_nlp))
                    cleaned_comment = re.sub(r'[^a-zA-Z0-9а-яА-Я\s]', '', comment)
                    self.comment=cleaned_comment
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
