# Телеграм-бот Московского зоопарка 🐾

## Описание 📖
Этот Телеграм-бот помогает пользователям узнать больше о программе опекунства Московского зоопарка 🦁 и пройти увлекательную викторину, чтобы определить свое «тотемное животное» 🐯. Бот предоставляет информацию о программе, рассказывает о преимуществах для опекунов и предлагает личностный тест.

### Основные функции 🚀
- **Приветствие и знакомство**: бот приветствует пользователя и кратко рассказывает о программе опекунства.
- **Информация о программе**: пользователи могут узнать, как стать опекуном и какие привилегии это предоставляет.
- **Викторина**: интерактивная викторина из 10 вопросов для определения «тотемного животного» пользователя 🦉.
- **Поделиться результатом**: после викторины пользователи могут поделиться результатом и узнать, какое животное им подходит.

## Инструкция по установке 🔧

### 1. Установка зависимостей
- Установите необходимые библиотеки с помощью команды:
  ```bash
  pip install -r requrements.txt
  ```
- Создайте файл `.env` в корневой папке проекта и добавьте туда токен вашего бота:
  ```plaintext
  TOKEN=<Ваш_Telegram_Bot_Token>
  ```

### 2. Настройка текста бота ✍️
В файле `config.py` содержатся все текстовые сообщения и вопросы викторины, что упрощает обновление контента без изменений в логике бота. Чтобы изменить текст, откройте `config.py` и отредактируйте нужные переменные. Например, можно изменить приветственное сообщение в переменной `welcome_text`.

### 3. Запуск бота ▶️
Для запуска бота выполните команду:
```bash
python bot.py
```

### 4. Как менять текст 📝
1. Откройте `config.py`.
2. Измените текстовые переменные. Например, чтобы изменить приветственное сообщение, отредактируйте `welcome_text`.

## Пример редактирования текстов
Чтобы изменить описание программы, просто найдите переменную `info_text` в `config.py` и укажите новый текст. Пример:
```python
info_text = '💫 Теперь вы можете стать частью заботливой семьи Московского зоопарка, поддерживая наших животных! 🌍'
```

Таким образом, легко обновлять любые сообщения бота, делая взаимодействие с ним еще более персонализированным и интересным для пользователей!
