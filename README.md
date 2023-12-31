# HTTP-Сервис для Работы с CSV-Данными

HTTP-сервис, разработанный с использованием FastAPI и SQLAlchemy, предоставляет возможности загрузки, хранения, извлечения и удаления CSV-файлов. SQLite используется в качестве базы данных.

## Оглавление

- [API Endpoints](#api-endpoints)
  - [Загрузка файла](#загрузка-файла)
  - [Получение списка файлов](#получение-списка-файлов)
  - [Получение данных из файла](#получение-данных-из-файла)
  - [Удаление файла](#удаление-файла)
- [Развертывание](#развертывание)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [Авторизация](#авторизация)
- [Документация API](#документация-api)

## API Endpoints

### Загрузка файла

- **Путь**: `/upload/`
- **Метод**: `POST`
- **Описание**: Загружает CSV-файл и сохраняет информацию о его структуре.

### Получение списка файлов

- **Путь**: `/`
- **Метод**: `GET`
- **Описание**: Возвращает список всех загруженных файлов с информацией о колонках.

### Получение данных из файла

- **Путь**: `/{file_id}`
- **Метод**: `GET`
- **Описание**: Возвращает данные из конкретного файла с возможностью фильтрации и сортировки по столбцам.

### Удаление файла

- **Путь**: `/{file_id}`
- **Метод**: `DELETE`
- **Описание**: Удаляет файл с заданным ID.

## Развертывание

1. **Склонируйте репозиторий:**
```sh
git clone <url репозитория>
```
2. **Перейдите в директорию проекта:**
```sh
cd <название проекта>
```
2. **Соберите Docker-образ:**
```sh
docker build -t <название образа> .
```
3. **Запустите контейнер:**
```sh
docker run -d -p 8000:8000 <название образа>
```
4. **Проверьте работу сервиса:**
Откройте http://localhost:8000 в веб-браузере для просмотра и тестирования API.
## Разработка
1. **Создайте и активируйте виртуальное окружение:**
```sh
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate  # Для Windows
```
2. **Установите зависимости:**
```sh
pip install -r requirements.txt
```
3. **Запустите сервер разработки:**
```sh
uvicorn app.main:app --reload
```
## Документация API
Детальную информацию об эндпойнтах, параметрах и форматах ответа можно найти в документации Swagger UI, доступной по адресу http://localhost:8000/docs после запуска сервиса.
