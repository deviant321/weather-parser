
# Импортируем text для безопасного выполнения текстового SQL-запроса через SQLAlchemy.
from sqlalchemy import text

# Импортируем движок, настроенный для подключения к PostgreSQL.
from app.database.connection import engine


# Проверяем, что приложение может подключиться к базе данных
# и выполнить простой SQL-запрос.
def main() -> None:
    try:
        # Открываем соединение с PostgreSQL.
        # Контекстный менеджер автоматически закроет соединение после завершения блока.
        with engine.connect() as connection:
            # Получаем информацию о версии PostgreSQL.
            result = connection.execute(text("SELECT version()"))

            # Выводим сообщение об успешном подключении и версию сервера.
            print("Подключение к PostgreSQL успешно!")
            print(result.scalar())

    except Exception as error:
        # Выводим информацию об ошибке, если соединение или запрос не удались.
        print(f"Ошибка подключения: {error}")


# Запускаем main() только при непосредственном запуске этого файла.
# При импорте main.py из другого модуля проверка автоматически не запустится.
if __name__ == "__main__":
    main()
