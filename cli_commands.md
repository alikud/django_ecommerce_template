django-admin startproject <project_name>: Создает новый проект Django с указанным именем.

python manage.py runserver: Запускает встроенный сервер разработки Django, чтобы вы могли просматривать свой проект в браузере.

python manage.py startapp <app_name>: Создает новое Django-приложение внутри проекта.

python manage.py makemigrations: Создает миграции на основе изменений моделей в проекте.

python manage.py migrate: Применяет ожидающие миграции к базе данных.

python manage.py createsuperuser: Создает суперпользователя (администратора) для административного интерфейса Django.

python manage.py collectstatic: Собирает статические файлы проекта в одну папку для использования в продакшн-среде.

python manage.py shell: Запускает интерактивную оболочку Django, которая позволяет выполнять Python-код в контексте проекта.

python manage.py test: Запускает тесты для вашего проекта, основанные на модуле unittest или pytest.

python manage.py flush: Очищает всю базу данных, удаляя все данные.

python manage.py dbshell: Запускает интерактивную оболочку базы данных, связанную с вашим проектом.

python manage.py check: Проверяет проект на наличие ошибок и проблем.

python manage.py shell_plus: Запускает интерактивную оболочку Django с дополнительными возможностями, предоставляемыми пакетом django-extensions.

python manage.py runscript <script_name>: Запускает пользовательский сценарий (скрипт) внутри вашего проекта, используя пакет django-extensions.