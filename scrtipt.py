import os
import json

# Определяем структуру проекта
project_structure = {
    "index.html": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Главная</title>
      <link rel="stylesheet" href="styles/style.css">
    </head>
    <body>
      <header>
        <h1>Добро пожаловать на главную страницу</h1>
      </header>
      <main>
        <p>Это главная страница вашего сайта.</p>
      </main>
      <footer>
        <p>&copy; 2023 Ваш Сайт</p>
      </footer>
    </body>
    </html>
    """,
    "blog.html": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Блог</title>
      <link rel="stylesheet" href="styles/style.css">
    </head>
    <body>
      <header>
        <h1>Блог</h1>
      </header>
      <main>
        <article>
          <h2>Статья 1</h2>
          <p>Краткое описание статьи 1.</p>
          <a href="article.html">Читать далее</a>
        </article>
      </main>
      <footer>
        <p>&copy; 2023 Ваш Сайт</p>
      </footer>
    </body>
    </html>
    """,
    "article.html": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Статья</title>
      <link rel="stylesheet" href="styles/style.css">
    </head>
    <body>
      <header>
        <h1>Статья 1</h1>
      </header>
      <main>
        <p>Полный текст статьи 1.</p>
      </main>
      <footer>
        <p>&copy; 2023 Ваш Сайт</p>
      </footer>
    </body>
    </html>
    """,
    "chat.html": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Чат</title>
      <link rel="stylesheet" href="styles/style.css">
    </head>
    <body>
      <header>
        <h1>Онлайн Чат</h1>
      </header>
      <main>
        <div id="chat-window">
          <div class="message">
            <strong>Пользователь 1:</strong> Привет!
          </div>
        </div>
        <form id="chat-form">
          <input type="text" id="username" placeholder="Ваше имя">
          <input type="text" id="message" placeholder="Ваше сообщение">
          <button type="submit">Отправить</button>
        </form>
      </main>
      <footer>
        <p>&copy; 2023 Ваш Сайт</p>
      </footer>
    </body>
    </html>
    """,
    "styles/style.css": """
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    header, footer {
      background-color: #f8f9fa;
      text-align: center;
      padding: 1em;
    }
    main {
      padding: 1em;
    }
    .message {
      margin: 0.5em 0;
    }
    """
}

# Создаем директории и файлы
for path, content in project_structure.items():
    dir_path = os.path.dirname(path)
    if dir_path:  # Проверяем, что путь не пустой
        os.makedirs(dir_path, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content.strip())

# Создаем файл конфигурации ESLint
eslint_config = {
    "env": {
        "browser": True,
        "es2021": True
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "rules": {
        # Ваши правила
    }
}

with open(".eslintrc.json", "w", encoding="utf-8") as eslint_file:
    json.dump(eslint_config, eslint_file, indent=2)

# Создаем файл конфигурации GitHub Actions
github_actions_config = """
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'
    - run: npm install
    - run: npx eslint .
"""

os.makedirs(".github/workflows", exist_ok=True)
with open(".github/workflows/ci.yml", "w", encoding="utf-8") as github_file:
    github_file.write(github_actions_config.strip())

print("Проект успешно создан!")
