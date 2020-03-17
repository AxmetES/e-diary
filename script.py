from datacenter.models import Schoolkid, Commendation, Teacher, Chastisement, Mark
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.shortcuts import get_object_or_404

import random

schoolkid_name = "Фролов Иван"
teacher_name = "Селезнева Майя Макаровна"
praise = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
          'Великолепно!',
          'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
          ' Сказано здорово – просто и ясно!', ' Ты, как всегда, точен!', ' Очень хороший ответ!', ' Талантливо!',
          ' Ты сегодня прыгнул выше головы!', ' Я поражен!', ' Уже существенно лучше!', ' Потрясающе!',
          ' Замечательно!', ' Прекрасное начало!', ' Так держать!', ' Ты на верном пути!', ' Здорово!',
          ' Это как раз то, что нужно!', ' Я тобой горжусь!', ' С каждым разом у тебя получается всё лучше!',
          ' Мы с тобой не зря поработали!', ' Я вижу, как ты стараешься!', ' Ты растешь над собой!',
          ' Ты многое сделал, я это вижу!', ' Теперь у тебя точно все получится!']
schoolkid_id = 6551
teacher_id = None
commendation_created_date = '2019-05-08'


def lookup_schoolkid(schoolkid_name):
    objects = None
    try:
        objects = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print('more than one object was found')
    except Schoolkid.DoesNotExist:
        print('does not exist')
    return objects


def get_teacher_id(teacher_name):
    teacher_id = None
    try:
        objects = Teacher.objects.get(full_name__contains=teacher_name)
    except MultipleObjectsReturned:
        print(f"more then one object founds")
    except Teacher.DoesNotExist:
        print('does not exist')
    else:
        teacher_id = objects.id
    return teacher_id


teacher_id = get_teacher_id(teacher_name)


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid__full_name__contains=schoolkid, points__lt=4)
    for mark in marks:
        mark.points = 4
        mark.save()


def remove_chastisements(schoolkid_name):
    chastisements = Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid_name)
    chastisements.delete()


def create_commendation(schoolkid_id, teacher_id, praise, created):
    text = random.choice(praise)
    Commendation.objects.create(text=text, created=created, schoolkid_id=schoolkid_id, teacher_id=teacher_id)


schoolkids = lookup_schoolkid(schoolkid_name)
fix_marks(schoolkid_name)
remove_chastisements(schoolkid_name)
create_commendation(schoolkid_id, teacher_id, praise, commendation_created_date)
print(schoolkids)
