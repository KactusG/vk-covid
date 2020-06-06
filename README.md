VK covid emotions
===================
English:
=========
Auto change emoticon near name<br/>
For this you must have Python >3.7<br/>

How to get a special token?
===========================
Follow this link https://vk.com/covid19</br>
Press ctrl + shift + I</br>
Go to `network`<br/>
And click on any emoticon<br/>
Appears `users.setCovidStatus` and click him<br/>
We get down to form data and copy access_token<br/>
This token works only one day<br/>
You can also enter a group token to receive a message about the expiration of current.

Linux:
===========
Download Python: `sudo apt install python3.8 git`<br/>
Download script: `git clone https://github.com/KactusG/vk-covid.git`<br/>
Install dependencies: `pip3.8 install -r requirements.txt`<br/>
And now run the script: `python3.8 vk-covid.py`

Windows:
===========
Download Python here: https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe<br/>
If there is git, then `git clone https://github.com/KactusG/vk-covid.git`<br/>
If he is not, then https://github.com/KactusG/vk-covid/archive/master.zip<br/>
Unzip it, go to the folder and run cmd or powershell there<br/>
Next, install the dependencies `pip install -r requirements.txt`<br/>
And run script `python vk-covid.py`

Русский:
===========
Значит, вам нужен специальный токен<br/>
Нам нужен Python >3.7

Как получить токен?
===================
Перейдите по этой ссылке https://vk.com/covid19</br>
Нажмите Ctrl + Shift + I</br>
Перейти во вкладку `network`<br/>
И нажмите на любой смайлик<br/>
Появляется `users.setCovidStatus` и нажимает на него<br/>
Спускаемся, во form data и копируем access_toke <br/>
Этот токен работает только один день<br/>
Вы также можете ввести групповой токен, чтобы получить сообщение в вк об истечении текущего токена.

Linux:
===========
Скачиваем Python: `sudo apt install python3.8 git`<br/>
Скачиваем сам скрипт: `git clone https://github.com/KactusG/vk-covid.git`<br/>
Переходим в папку: `cd vk-covid`<br/>
Установка зависимостей: `pip3.8 install -r requirements.txt`<br/>
И запускаем скрипт `python3.8 vk-covid.py`

Windows:
===========
Скачиваем Python: https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe<br/>
Если есть git, то `git clone https://github.com/KactusG/vk-covid.git`<br/>
Если нет, то скачиваем архив https://github.com/KactusG/vk-covid/archive/master.zip<br/>
Распаковываем. заходим в папку и запускаем cmd или powershell<br/>
Устанавливаем зависимости: `pip install -r requirements.txt`<br/>
Запускаем скрипт: `python vk-covid.py`<br/>
