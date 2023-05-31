# """Реализация базовых команд для асинхронного запроса к базе
# данных Postgres через Django ORM.
# """
# # from typing import List, Coroutine

# from asgiref.sync import sync_to_async
# from AdminDjango.api.models import UserModel


# @sync_to_async
# def add_user(user_id):
#     add_user_ = UserModel.objects.create(user_id=user_id)
#     add_user_.save()
#     return add_user_

# @sync_to_async
# def get_user(user_id_):
#     user = UserModel.objects.filter(user_id_).first()
#     return user


# @sync_to_async
# def get_users():
#     users = UserModel.objects.all()
#     return users


# @sync_to_async
# def count_users():
#     total = UserModel.objects.all().count()
#     return total
