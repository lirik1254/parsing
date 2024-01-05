import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import json
import codecs

# persons_url_list = []
#
# for i in range(0, 740, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={i}'
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all(class_='bt-open-in-overlay')
#
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#
# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')

# res_list = list()
#
# with open('persons_url_list.txt') as file:
#     lines = [line.strip() for line in file.readlines()]
#     count = 1
#     for line in lines:
#         print(f'Обрабатывается {count} элемент..', end = " ")
#         q = requests.get(line)
#         result = q.content
#
#         soup = BeautifulSoup(result, 'lxml')
#         person = soup.find(class_='bt-biografie-name').find('h3').text
#         person_name_company = person.strip().split(',')
#         person_name = person_name_company[0]
#         person_company = person_name_company[1].strip()
#
#         person_main = soup.find('div', {'id': 'bt-kontakt-collapse'})
#         social_networks = person_main.find_all(class_="bt-link-extern")
#
#         social_networks_url = []
#         for item in social_networks:
#             social_networks_url.append(item.get('href'))
#
#         res_dict = {'name': person_name,
#                     'partion': person_company,
#                     'social_network_links': social_networks_url}
#
#         res_list.append(res_dict)
#         with open('data.json', 'w', encoding = 'utf-8') as json_file:
#             json.dump(res_list, json_file, indent= 4)
#         print(' Готово!')
#         count += 1
#         sleep(random.randrange(2, 4))



