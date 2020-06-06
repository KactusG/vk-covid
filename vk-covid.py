import requests
import time
import os
import json
from colorama import Fore, Back, Style
import random

token = input("Введите токен специальный для установления смайлика (инструкция в README): ")
group_token = input("Введите токен для присылке уведомления от группы (можно не вводить): ")
failed_auth_messages = "[vk-covid bot] Токен больше не верен, замените его"
a = 1
status_id = 1
request_id = 1
while a == 1:
	send = requests.post("https://api.vk.com/method/users.setCovidStatus?api_id=7362610&method=users.setCovidStatus&format=json&v=5.103&status_id={}&access_token={}&request_id={}".format(status_id,token,request_id))
	try:
		json.loads(send.text)["response"]
		print('Смайлик под id: {} установлен'.format(status_id))
		if status_id == 36:
			status_id = 1
		else:
			status_id += 1
		request_id += 1
		time.sleep(7)
	except KeyError:
		error_code = json.loads(send.text)["error"]["error_code"]
		if error_code == 5:
			print(failed_auth_messages)
			random = random.randrange(0, 9223372036854775807)
			send_error = requests.post("https://api.vk.com/method/messages.send?access_token={}&user_id=193291332&message={}&v=5.103&random_id={}".format(group_token,failed_auth_messages,random))
			exit()
		if error_code == 100:
			print('Не существует смайлика под id: {}, переход к следующему'.format(status_id))
			if status_id == 36:
				status_id = 1
			else:
				status_id += 1
			request_id += 1
