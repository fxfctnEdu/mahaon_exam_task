# Задание

###Подготовка

- Склонируйте репозиторий с заданием.

- Создайте виртуальное окружение **exam**:
```
python -m venv examvenv
examvenv\Scripts\activate
```
- Установить необходимые библиотеки:
```
pip install -r requirements.txt
```
- Папка проекта -- **blogProject**, запустить сервер:
```
cd blogProject
python manage.py runserver
```

### Минимум
1. Создать модель **Post** (список полей создавать, опираясь на словари в файле `blog/views.py`).
2. Добавить несколько записей (консоль или dbdrowser).
3. Изменить функцию **get_index()** так, чтобы она брала posts из БД и сортировала их по дате (новые вверху).
4. Проверить, что созданные в БД записи отобразились.

### Максимум
5. Создать **path** `/<int:id>/`, такой, что ему соотвествует ФП `get_post`, а `name='post'`.
6. Изменить функцию **get_post()** так, чтобы она возвращала конкретный пост по id.
7. Изменить **index.html** так, чтобы заголовок стал ссылкой на /:id
То есть по адресу localhost:8000/1 должен быть расположен пост с id==1