## Проект: "Кофейный гид"
## Описание проекта

Проект создан в рамках акселерации Яндекс.Практикум.

Веб-сервис "Кофейный гид" может быть полезен для любителей кофе, путешественников или просто тех, кто хочет найти новое место для работы или встречи с друзьями.

Пользователи могут найти ближайшую кофейню и получить информацию о ее местоположении, часах работы и контактной информации.

Сервис может позволить пользователям искать кофейни по различным критериям, таким как типы напитков, наличие Wi-Fi, работающие часы и т. д.

Пользователи могут оставлять отзывы о кофейнях и читать отзывы других пользователей, чтобы выбрать лучшее место для посещения.

Сервис может предоставлять информацию о транспортных маршрутах или пешеходных маршрутах до выбранной кофейни.

Проект разворачивается в Docker контейнерах:
- backend-приложение API,
- db-база данных


# Установка Poetry

### Установка на Unix-системах

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### Установка на Windows
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Далее, необходимо добавить соответствующую директорию в PATH:

### Linux, MacOS, WSL
```bash
$HOME/.local/bin
```
### Windows
```bash
%APPDATA%\Python\Scripts
```

Перезагрузите оболочку и проверьте корректность установки:

```bash
poetry --version
```
### Создание проекта
Создание проекта с нуля
```bash
poetry new my-project
```
В уже существующем проекте
```bash
poetry init
```
### Подготовка виртуального окружения
(Команды new и init не создают виртуальных окружений.)

```bash
poetry env use python
```
По умолчанию, Poetry создает виртуальные окружения в папке {cache_dir}/virtualenvs. Если нужно, чтобы виртуальное окружение находилось в папке проекта, можно выполнить следующую команду:

```bash
poetry config virtualenvs.in-project true
```
Теперь создаваемое виртуальное окружение будет находиться в папке .venv в корне проекта.

### Файлы pyproject.toml и poetry.lock
pyproject.toml содержит всю информацию о проекте: метаданные, зависимости и настройки других инструментов. poetry.lock содержит зависимости проекта с зафиксированными версиями и формируется автоматически (пожалуйста, не редактируйте его вручную).

[tool.poetry] содержит в себе метаданные. [tool.poetry.dependencies] содержит версию Python и основные зависимости проекта (так называемую main-группу).

### Установка и удаление пакетов
```bash
poetry add django==4.2.8
```

### Extras и groups
Dependency groups содержат в себе опциональные зависимости, используемые только при разработке. Установить зависимости из групп можно только через Poetry. Каждый проект содержит в себе одну неявную обязательную группу - main, которая находится в секции [tool.poetry.dependencies].

### Установка в группу выполняется следующим образом:

```bash
poetry add --group test pytest
```
Extras предназначены для дополнительных зависимостей, включающих функциональность в проекте.

### poetry install
Команда install при запуске выполняет следующую последовательность действий:

 - читает файл pyproject.toml
 - если существует файл poetry.lock, то версии зависимостей берутся из него.
 - если его не существует, Poetry выполнит разрешение зависимостей и
   создаст его, затем устанавливает зависимости.

### Удаление пакетов
Для удаления зависимости используйте команду remove:

```bash
poetry remove requests
```
Если зависимость находится в группе, используйте опцию --group:

```bash
poetry remove --group my-group requests
```

### Запуск команд через Poetry
```bash
poetry shell
```
С помощью poetry shell можно запустить оболочку с активированным виртуальным окружением. Если его не существует, то оно будет создано.

Т.к. poetry shell не просто активирует виртуальное окружение, а именно создает оболочку, то стоит использовать для выхода exit, а не deactivate.

## Системные требования
- Python 3.11
- Docker
- Works on Linux, Windows, macOS, BSD

## Стек технологий
- Python 3.11
- Django 4.2.8
- Rest API
- PostgreSQL
- Nginx
- gunicorn
- Docker
- DockerHub
- GitHub Actions (CI/CD)

## Установка проекта из репозитория
### Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/py-Coffee-Guide/coffee-guide-backend```

### Перейти в директорию инфраструктуры проекта:
``` cd coffee_guide/infra ```

### Создать и открыть файл .env с переменными окружения:

```touch .env```
### Заполнить .env файл с переменными окружения по примеру:
```
echo DB_ENGINE=django.db.backends.postgresql >> .env
echo DB_NAME=postgres >> .env
echo POSTGRES_PASSWORD=postgres >> .env
echo POSTGRES_USER=postgres >> .env
echo DB_HOST=db >> .env
echo DB_PORT=5432 >> .env

echo EMAIL_USE_SSL=True >> .env          # или EMAIL_USE_TLS=True
echo EMAIL_HOST='smtp.example.ru' >> .env
echo EMAIL_PORT=port >> .env
echo EMAIL_HOST_USER='your_mail@example.ru' >> .env
echo EMAIL_HOST_PASSWORD='your_password' >> .env
echo DEFAULT_FROM_EMAIL='your_mail@example.ru' >> .env

```
