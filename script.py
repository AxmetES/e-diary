from datacenter.models import Schoolkid, Commendation, Teacher, Chastisement, Mark
from django.core.exceptions import MultipleObjectsReturned
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
teacher_id = 697
commendation_created_date = '2019-05-08'


def lookup_ivan(schoolkid):
    Ivan = None
    try:
        Ivan = Schoolkid.objects.get(full_name__contains=schoolkid)
    except MultipleObjectsReturned:
        print('more than one object was found')
    return Ivan


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid__full_name__contains=schoolkid)
    for mark in marks:
        mark.points = 4
        mark.save()


def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid)
    chastisement.delete()


def create_commendation(schoolkid_id, teacher_id, praise, created):
    text = random.choice(praise)
    Commendation.objects.create(text=text, created=created, schoolkid_id=schoolkid_id, teacher_id=teacher_id)


def get_schoolkid_id(student_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=student_name)
    schoolkid_id = schoolkid[0].id
    return schoolkid_id


def get_teacher_id(teacher_name):
    teacher = Teacher.objects.get(full_name__contains=teacher_name)
    teacher_id = teacher[0].id
    return teacher_id


schoolkid = lookup_ivan(schoolkid_name)
lookup_ivan(schoolkid)
fix_marks(schoolkid)
remove_chastisements(schoolkid)
create_commendation(schoolkid_id, teacher_id, praise, commendation_created_date)
