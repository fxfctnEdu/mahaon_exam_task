# Задание

### Подготовка

- Склонируйте репозиторий с заданием.
```
git clone https://github.com/fxfctnEdu/mahaon_exam_task.git
cd mahaon_exam_task
```
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

## Вариант 1 (Blog приложение)

### Минимум
1. Создать модель **Post** (список полей создавать, опираясь на словари в файле `blog/views.py`). 
Добавьте дополнительное поле publish_date (тип Дата, может быть пустым).
2. Добавить несколько записей (консоль, dbdrowser, django admin).
3. Изменить функцию **get_index()** так, чтобы она брала posts из БД и сортировала их по дате (новые вверху), 
а также проверяла дату публикации, если пост отложенный -- он не должен отобразиться.
4. Проверить, что созданные в БД записи отобразились.

### Максимум
5. Создать **path** `blog/<int:id>/`, такой, что ему соотвествует ФП `get_post`, а `name='post'`.
6. Изменить функцию **get_post()** так, чтобы она возвращала конкретный пост по id.
7. Изменить **index.html** так, чтобы заголовок стал ссылкой на `blog/:id`.
То есть по адресу localhost:8000/blog/1 должен быть расположен пост с id==1.
8. Создайте шаблон **post.html** для `get_post`. 

## Вариант 2 (Staff приложение)

### Минимум
1. Создать модель **Employee** (список полей создавать, опираясь на словари в файле `staff/views.py`).
2. Добавить несколько записей (консоль, dbdrowser, django admin).
3. Изменить функцию **get_employees()** так, чтобы она брала employees из БД 
и сортировала их по имени и фамилии от а до я.
4. Проверить, что созданные в БД записи отобразились.

### Максимум
5. Создать **path** `staff/<int:id>/`, такой, что ему соотвествует ФП `get_employee`, а `name='employee'`.
6. Изменить функцию **get_employee()** так, чтобы она возвращала конкретного сотрудника по id.
7. Изменить **index.html** так, чтобы заголовок стал ссылкой на `staff/:id`. 
То есть по адресу localhost:8000/staff/1 должна быть расположена информация про сотрудника с id==1.
8. Создайте шаблон **employee.html** для `get_employee`. 
