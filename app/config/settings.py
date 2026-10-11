
# Импортируем класс для описания настроек приложения и конфигурацию его загрузки.
from pydantic_settings import BaseSettings, SettingsConfigDict


# Описываем настройки, которые приложение получает из переменных окружения.
class Settings(BaseSettings):
    # URL подключения к PostgreSQL.
    # Pydantic автоматически найдёт переменную DATABASE_URL в окружении.
    database_url: str

    # Указываем, откуда загружать настройки и как читать файл конфигурации.
    model_config = SettingsConfigDict(
        env_file=".env",              # Путь к файлу с настройками относительно рабочей директории.
        env_file_encoding="utf-8",    # Кодировка файла .env.
        extra="ignore",               # Игнорируем дополнительные переменные, не описанные в классе.
    )


# Создаём единый объект настроек, который будут использовать другие модули.
settings = Settings()
