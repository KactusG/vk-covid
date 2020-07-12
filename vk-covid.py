import requests
import time
import os
import json
from colorama import Fore, Back, Style
import urllib
from bs4 import BeautifulSoup
import re

email = "guz1@bk.ru"
passw = "Guznorodov1!2!"
group_token = "cb6228d9d818629e028a4dc365ced552b628aba6d9a87ca1898515a9f9049ab2013bac1b22347495da59b"
failed_auth_messages = "[vk-covid bot] Токен больше не верен, замените его"
a = 1
status_id = 1
request_id = 1
while True:
	head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
	content_main = requests.post('https://vk.com/im', headers=head)
	remixlhk = content_main.cookies.get_dict()['remixlhk']
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "cookie": f"remixlhk={remixlhk};"}
	soup = BeautifulSoup(content_main.text, 'lxml')
	ip_h = soup.find("input", attrs={'name':'ip_h', 'type':'hidden'})['value']
	lg_h = soup.find("input", attrs={'name':'lg_h', 'type':'hidden'})['value']
	params1 = {'act':'login', '_origin':'https://vk.com', 'ip_h':ip_h, 'lg_h':lg_h, 'email':email, 'pass':passw}
	encoded_params1 = urllib.parse.urlencode(params1).encode('utf-8')
	login_one = urllib.request.urlopen(urllib.request.Request("https://login.vk.com", encoded_params1, headers))
	q_hash = re.split(r'=', login_one.geturl())[6]
	soup1 = BeautifulSoup(login_one.read(), 'lxml')
	ip_h = soup1.find("input", attrs={'name':'ip_h', 'type':'hidden'})['value']
	lg_h = soup1.find("input", attrs={'name':'lg_h', 'type':'hidden'})['value']
	login_last_url = f'https://login.vk.com/?act=login&role=fast&redirect=1&to=&s=1&__q_hash={q_hash}&ip_h={ip_h}&lg_h={lg_h}&email={email}&pass={passw}'
	login_last = requests.Session()
	login_last = requests.post(login_last_url, headers=headers)
	login_last = requests.post("https://vk.com/apps.php?act=handle_vk_connect_event&al=1&app_id=7362610&event=get_auth_token_info&hash=cb7ba7e394a793c8bc&scope=", headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Cookie': 'remixsid=5b09394ac0c31cccb6c567cf4b6a3b7701f9e7d0be939ed9241b7143ecdc6'}).text
	token_request = json.loads(login_last.replace('<!--', ''))['payload'][1][0]
	token = json.loads(token_request)['access_token']
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
				a = 2
			if error_code == 100:
				print('Не существует смайлика под id: {}, переход к следующему'.format(status_id))
				if status_id == 36:
					status_id = 1
				else:
					status_id += 1
				request_id += 1
