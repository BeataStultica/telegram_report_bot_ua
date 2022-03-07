# Юзер-Бот, що автоматизує репортування Телеграм каналів пропагандистів

Цей Телеграм Юзер-Бот використовується для автоматизації репорту пропагандистьских каналів.

## Налаштування системи для використання без віртуалізації
1. По-перше, вам необхідно інсталювати Python3. Python можна завантажити за [посиланням](https://www.python.org/). 
2. Запустіть консоль. Для цього використовуйте комбінацію клавіш Win+R, у з'явившомуся вікні напишіть cmd та натисніть enter
3. Далі виконуємо наступні команди:
```
git clone https://github.com/Antcating/telegram_report_bot_ua
cd telegram_report_bot_ua
pip install -r requirements.txt
```
4. Переходимо за посиланням  https://my.telegram.org/, вводимо свій номер телефону та код авторизації
<br>Переходимо у вкладку API development tools, пишемо любий App title та Short name
<br>Нагорі отримуємо App api_id та App api_hash
<br>**ПЕРЕДАВАТИ КОМУСЬ `api_id` та `api_hash` НІ В ЯКОМУ РАЗІ НЕ МОЖНА!!! Вони дають можливіть контролювати вашу персональну сторінку у Телеграмі.**

## Скаржитись на канали з використанням Docker
1. Переходимо за посиланням  https://my.telegram.org/, вводимо свій номер телефону та код авторизації
<br>Переходимо у вкладку API development tools, пишемо любий App title та Short name
<br>Нагорі отримуємо App api_id та App api_hash
<br>**ПЕРЕДАВАТИ КОМУСЬ `api_id` та `api_hash` НІ В ЯКОМУ РАЗІ НЕ МОЖНА!!! Вони дають можливіть контролювати вашу персональну сторінку у Телеграмі.**
2. Запускаєте команду:
```
docker run -e API_ID=... -e API_HASH=... -it sprotyv2/telegram-report-bot-ua:1.0.0
```
3. По черзі вводимо:
- Телефон вашого аккаунта у форматі +380ххххххххх
- Код автентифікації який прийде повідомленням у телеграм
4. Бот автоматично напише репорти на канали, що записані у файлі `telegram_db.csv` з текстом, що генеруєтся у файлі `report_message_generator.py`
<br>**Правильно налаштована програма буде відображати такий результат:**
<br><br>![image](https://user-images.githubusercontent.com/39994538/155859028-e83b5228-e711-4f21-bf4e-db9b1cfccb24.png)
5. Щоб "звернути" Docker контейнер для работи на фоні можна використати наступну комбінацію клавіш: Ctrl+P followed by Ctrl+Q. Контейнер продовжить працювати, ви можете переглянути логи за допомогою команди:
```
docker logs /*CONTAINER_ID*/
```
CONTAINER_ID можна знайти виконавши команду для перегляду контейнерів:
```
docker container ls
```
Контейнер можна зупинити за допомогою команди:
```
docker stop /*CONTAINER_ID*/
```
Та знов запустити зупинений контейнер за допомогою команди:
```
docker start /*CONTAINER_ID*/
```
При запуску зупиненого контейнеру він запамʼятає, на які канали вже були надіслані скарги та не бути надсилати повторні скарги на них.

## Використання

### Скражитись на канали:
1. запускаємо бота:`python report_channels.py`
2. По черзі вводимо:
- App api_id
- App api_hash
- Телефон вашого аккаунта у форматі +380ххххххххх
- Код автентифікації який прийде повідомленням у телеграм
3. Бот автоматично напише репорти на канали, що записані у файлі `telegram_db.csv` з текстом, що генеруєтся у файлі `report_message_generator.py`
<br>**Правильно налаштована програма буде відображати такий результат:**
<br><br>![image](https://user-images.githubusercontent.com/39994538/155859028-e83b5228-e711-4f21-bf4e-db9b1cfccb24.png)

Щоб використати інший аккаунт, треба видалили файл session_new.session у папці з програмою (або використати команду `del session_new.session`).

### Лишати коментарі

Будьте уважні! Перед там як відсилати повідомлення, приховайте в налаштуваннях приватності
власний телефон, повне справжнє ім'я, таке інше. Якщо ви не певні як то зробить, краще
не використовуйте даний скрипт.

У всіх каналах де ввімкнені коментарі, бот відповідає на останній пост рандомним меседжем з `comments/text_comments.txt`.
Перед тим як запускати бота - додайте свої думки. Щось конструктивне може спрацювати краще, агресія = бан.
Ставте незручні питання, пояснюйте що відбувається насправді.

В ваш основний telegram client (на телефоні та/або десктопі) почнуть надходити відповіді.
Вимкніть нотифікації та не читайте їх (дуже важко психологічно).

Запускаємо бота так само як і попереднього `python spam_channels.py`

## Оновлення бота та бази каналів
Ми намагаємося періодично оновляти бота та базу пропагадистських каналів, тому рекомендуємо іноді перевіряти чи не додались нові канали. 
Якщо ви хочете оновити базу/бота вам необхідно: 
1. Зайти у теку проекту
2. Відкрити консоль у цій теці 
3. Вписати команду 
``` 
git pull
```
4. База/бот оновлені, можете як вказано вище запускати бота та відсилати репорти на більшу кількість пропагандистів.


## Безпека телеграм-акаунту
Під час налаштування бота вам буде потрібно вказати одноразовий код на сайті my.telegram.org та у python модулі [telethon](https://github.com/LonamiWebs/Telethon). Перше - це офіційний сайт телеграму, друге - це дуже відомий модуль, код якого був перевірений досвідченими програмістами не один раз. Тож ваш акаунт не передається третім особам на протязі всього процесу налаштування та використання програми.
<br>Також програма емулює поведінку нового пристрою який використовує ваш акаунт. Ви можете побачити цей віртуальний пристрій в активних сеансах телеграму (Налаштування -> Приватність і безпека  -> Показати всі сеанси). Він матиме таку ж назву і тип які ви вкажете під час реєстрації на my.telegram.org. *Після виконання програми ви можете видалити цей девайс з активних сеансів.*

## Додаткова інформація
У теці проєкту знаходиться файл `telegram_db.csv`, що містить у собі список пропагандистських каналів. Якщо ви маєте інформацію про інші канали, що не війшли у список, але заслуговують репорту - присилайте їх мені у [телеграм](https://www.t.me/Achating) або додавайте їх у реквестах на Github.
