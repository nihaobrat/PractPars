
# PractPars

PractPars - это проект на Django, предназначенный для парсинга данных с различных источников, в частности, с сайта hh.ru. Это руководство поможет вам установить, настроить и запустить проект, а также предоставит важные советы по работе с приложением.

## Содержание

1. [Описание проекта](#описание-проекта)
2. [Требования](#требования)
3. [Установка и настройка](#установка-и-настройка)
   - [Клонирование репозитория](#клонирование-репозитория)
   - [Настройка окружения](#настройка-окружения)
   - [Установка зависимостей](#установка-зависимостей)
   - [Миграции базы данных](#миграции-базы-данных)
4. [Запуск проекта](#запуск-проекта)
   - [Запуск с использованием Docker](#запуск-с-использованием-docker)
   - [Запуск локально](#запуск-локально)
5. [Основные функции](#основные-функции)
6. [API примеры с использованием curl](#api-примеры-с-использованием-curl)
7. [Дополнительные настройки](#дополнительные-настройки)

## Описание проекта

PractPars - это мощный инструмент для парсинга вакансий с сайта hh.ru, который использует Django для управления проектом и Django REST Framework для создания API. Проект поддерживает интеграцию с различными базами данных и может быть развернут с использованием Docker.

## Требования

Для работы с проектом вам понадобятся следующие инструменты и библиотеки:

- Python 3.10+
- Django 3.2.25
- Django REST Framework
- Docker и Docker Compose (для запуска с Docker)
- PostgreSQL (рекомендуется для использования в продакшн среде)

## Установка и настройка

### Клонирование репозитория

Склонируйте репозиторий проекта на ваш локальный компьютер:

```bash
git clone https://github.com/username/PractPars.git
cd PractPars
```

### Настройка окружения

Создайте виртуальное окружение для установки зависимостей:

```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

### Установка зависимостей

Установите все необходимые зависимости:

```bash
pip install -r requirements.txt
```

### Миграции базы данных

Выполните миграции для настройки базы данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Запуск проекта

### Запуск с использованием Docker

Для запуска проекта с использованием Docker, убедитесь, что у вас установлены Docker и Docker Compose. Затем выполните следующие команды:

```bash
docker-compose up --build
```

Эта команда соберет и запустит контейнеры для приложения и базы данных.

### Запуск локально

Для локального запуска проекта выполните следующие команды:

1. Запуск сервера разработки:

    ```bash
    python manage.py runserver
    ```

2. Откройте браузер и перейдите по адресу `http://localhost:8000/`.

## Основные функции

- **API для парсинга вакансий с hh.ru**: Используя Django REST Framework, проект предоставляет API для взаимодействия с функциями парсинга.
- **Панель администратора**: Django Admin предоставляет интерфейс для управления данными.
- **Поддержка различных источников данных**: Легко настраиваемые скрипты для парсинга данных с различных источников.

## API примеры с использованием curl

Для взаимодействия с API PractPars можно использовать команды curl. Ниже приведены примеры запросов для просмотра вакансий и кандидатов.

### Получение списка вакансий

```bash
curl -X GET http://localhost:8000/api/vacancies/
```

### Получение информации о конкретной вакансии

```bash
curl -X GET http://localhost:8000/api/vacancies/{id}/
```

### Создание новой вакансии

```bash
curl -X POST http://localhost:8000/api/vacancies/      -H "Content-Type: application/json"      -d '{
           "title": "Python Developer",
           "description": "Looking for an experienced Python developer.",
           "company": "Tech Corp",
           "location": "Moscow",
           "salary": "100000"
         }'
```

### Обновление вакансии

```bash
curl -X PUT http://localhost:8000/api/vacancies/{id}/      -H "Content-Type: application/json"      -d '{
           "title": "Senior Python Developer",
           "description": "Looking for a senior Python developer with Django experience.",
           "company": "Tech Corp",
           "location": "Moscow",
           "salary": "150000"
         }'
```

### Удаление вакансии

```bash
curl -X DELETE http://localhost:8000/api/vacancies/{id}/
```

### Получение списка кандидатов

```bash
curl -X GET http://localhost:8000/api/candidates/
```

### Получение информации о конкретном кандидате

```bash
curl -X GET http://localhost:8000/api/candidates/{id}/
```

### Создание нового кандидата

```bash
curl -X POST http://localhost:8000/api/candidates/      -H "Content-Type: application/json"      -d '{
           "name": "John Doe",
           "email": "john.doe@example.com",
           "resume": "Experienced Python developer..."
         }'
```

### Обновление кандидата

```bash
curl -X PUT http://localhost:8000/api/candidates/{id}/      -H "Content-Type: application/json"      -d '{
           "name": "John Doe",
           "email": "john.doe@example.com",
           "resume": "Senior Python developer with extensive Django experience..."
         }'
```

### Удаление кандидата

```bash
curl -X DELETE http://localhost:8000/api/candidates/{id}/
```

## Дополнительные настройки

### Настройка базы данных

По умолчанию проект использует SQLite. Для использования PostgreSQL, измените настройки базы данных в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

### Настройка переменных окружения

Создайте файл `.env` в корне проекта и добавьте следующие переменные:

```env
SECRET_KEY='your_secret_key'
DEBUG=True
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'
DB_HOST='your_db_host'
DB_PORT='your_db_port'
```

### Статические файлы

Для сбора статических файлов выполните:

```bash
python manage.py collectstatic
```

### Управление пользователями

Для создания суперпользователя (администратора), выполните следующую команду:

```bash
python manage.py createsuperuser
```
