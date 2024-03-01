# Help Desk

### Установка

1. Скачиваем проект 
   ```git clone git@github.com:Srg300/help-desk.git```

2. Создаем виртуальное окружение с помощью комманды
   ```pdm venv create 3.11```

3. Устанавливаем зависимости
   ```pdm sync --clean```

4. Задать PYTHONPATH
   ```export PYTHONPATH=src```

5. Заполнить в .env файл параметры для подключения к БД
    ```
    DATABASE_NAME='help-desk'
    DATABASE_HOST='localhost'
    DATABASE_USERNAME='postgres'
    DATABASE_PASSWORD='postgres'
    DATABASE_ECHO=False
    ```
6. Применить миграции
   ```alembic upgrade head```

7. Запустить приложение коммандой
   ```python main.py``` или ```python -m main```
