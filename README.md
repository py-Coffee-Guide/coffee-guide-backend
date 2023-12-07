# Установка Poetry

## Установка на Unix-системах

```bash
curl -sSL https://install.python-poetry.org | python3 -
Установка на Windows
bash
Copy code
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
Далее, необходимо добавить соответствующую директорию в PATH:

Linux, MacOS, WSL
bash
Copy code
$HOME/.local/bin
Windows
bash
Copy code
%APPDATA%\Python\Scripts
Перезагрузите оболочку и проверьте корректность установки:

bash
Copy code
poetry --version
Создание проекта
Создание проекта с нуля
bash
Copy code
poetry new my-project
В уже существующем проекте
bash
Copy code
poetry init
Подготовка виртуального окружения
(Команды new и init не создают виртуальных окружений.)

bash
Copy code
poetry env use python
По умолчанию, Poetry создает виртуальные окружения в папке {cache_dir}/virtualenvs. Если нужно, чтобы виртуальное окружение находилось в папке проекта, можно выполнить следующую команду:

bash
Copy code
poetry config virtualenvs.in-project true
Теперь создаваемое виртуальное окружение будет находиться в папке .venv в корне проекта.

Файлы pyproject.toml и poetry.lock
pyproject.toml содержит всю информацию о проекте: метаданные, зависимости и настройки других инструментов. poetry.lock содержит зависимости проекта с зафиксированными версиями и формируется автоматически (пожалуйста, не редактируйте его вручную).

[tool.poetry] содержит в себе метаданные. [tool.poetry.dependencies] содержит версию Python и основные зависимости проекта (так называемую main-группу).

Установка и удаление пакетов
Стандартная установка
bash
Copy code
poetry add django==4.2.8
Extras и groups
Dependency groups содержат в себе опциональные зависимости, используемые только при разработке. Установить зависимости из групп можно только через Poetry. Каждый проект содержит в себе одну неявную обязательную группу - main, которая находится в секции [tool.poetry.dependencies].

Установка в группу выполняется следующим образом:

bash
Copy code
poetry add --group test pytest
Extras предназначены для дополнительных зависимостей, включающих функциональность в проекте.

poetry install
Команда install при запуске выполняет следующую последовательность действий:

читает файл pyproject.toml
если существует файл poetry.lock, то версии зависимостей берутся из него. Если его не существует, Poetry выполнит разрешение зависимостей и создаст его, затем устанавливает зависимости.
Удаление пакетов
Для удаления зависимости используйте команду remove:

bash
Copy code
poetry remove requests
Если зависимость находится в группе, используйте опцию --group:

bash
Copy code
poetry remove --group my-group requests
Запуск команд через Poetry
bash
Copy code
poetry shell
С помощью poetry shell можно запустить оболочку с активированным виртуальным окружением. Если его не существует, то оно будет создано.

Т.к. poetry shell не просто активирует виртуальное окружение, а именно создает оболочку, то стоит использовать для выхода exit, а не deactivate.
