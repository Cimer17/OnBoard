# OnBoard
Демонстрация проекта:
https://disk.yandex.ru/i/A7UBLbtHIO_Kag

#### Реализованная функциональность:

* Мобильный помощник с возможностью перевода на оператора;
* Навигатор – позволяет в несколько кликов получить полезные материалы, телефонный справочник с автоматическим импортом, а также сделать электронные справки;
* Календарь событий – позволяет просмотреть даты с определенными событиями и возможностью добавлением своих.

#### Особенность проекта:

* Сканирование QR–кода  и получение виртуальных бонусов, активация дополнительных функций
* Геймификация в виде системы достижений
* Онлайн поддержка с обработкой частых ответов ботом
* Автоматическая генерация документов, исходя из данных пользователя

#### Основной стек технологий:

* Python/HTML/CSS/Git 
### СРЕДА ЗАПУСКА
  ***
  1. Развертывание сервиса производится на windows/ubuntu;
  2. Необходима установка [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/) (либо иной редактор .docx документов)
  3. Сервер с поддержкой Python 3.10+

### УСТАНОВКА
  ***
  #### Установка python 3.9.10
  1. Для скачивания python запускаем файл install.bat, устанавливаем.
  2. Убедитесь, что флажки “Установить для всех”(рекомендуется) и «Add Python 3.9.10 to PATH» вы отметили.
##### linux:
```
apt-get update
apt-get install -y python3
```
  #### Установка зависимостей проекта
  Создаем виртуальное окружение:
  ```
  python -m venv env
  ```
  Активируем его:
  
  Windows:
  ```
  python -m venv env
  ```
  Linux/Mac:
  ```
  source env/bin/activate
  ```
  
  Для установки зависимостей использовать следующую команду: 
  ```
  pip install -r requirements.txt
  ```
 #### Настройка бота/админки
 
 1. settings.ini - содержит токен бота телеграм. [Инструкция](https://boto.agency/blog/kak-polychit-api-token-telegram/) получения токена.
 2. Настроить сервер: Настроить firewall для разрешения входящих подключений на порт, который будет использоваться для запуска приложения.
 3. Настроить reverse proxy, такой как NGINX, чтобы перенаправлять входящие запросы на соответствующий порт, на котором работает Flask-приложение.
 ##### Запуск
 ```
  python main.py
  ```
 
 РАЗРАБОТЧИКИ
 #####  Клопов Иван Валерьевич (https://t.me/jonistyle)
 #####  Савчиев Роман Валерьевич 
 #####  Стаценко Артём Александрович 

    
    
   



