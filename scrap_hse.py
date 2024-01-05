import time

import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import json
import codecs


def take_description(bigstr: str):
    final_line = ''
    count_number_of_posts = bigstr.count(':\n')
    for i in range(count_number_of_posts):
        pred_final = ''
        ind_of_double_point = bigstr.find(':\n')
        bigstr = bigstr.replace(':\n', '.', 1)
        i = ind_of_double_point
        while bigstr[i] != '\t':
            pred_final += bigstr[i]
            i -= 1
        pred_final = ''.join(reversed(pred_final))
        final_line += pred_final
        while bigstr.find('</a>\n') != -1 and (bigstr.find('</a>\n') < bigstr.find(':\n') or bigstr.find(':\n') == -1):
            ind_of_a_and_n = bigstr.find('</a>\n')
            bigstr = bigstr.replace('</a>\n', '.', 1)
            final_line = final_line.replace('.', ':')
            i = ind_of_a_and_n - 1
            an_line = ''
            while bigstr[i] != '>':
                an_line += bigstr[i]
                i -= 1
            an_line = ''.join(reversed(an_line))
            final_line += an_line
            final_line += "\n"
    return final_line


letters_list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж',
                'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П',
                'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ч', 'Ш', 'Щ']

udept_list = ['22726', '135288', '135083', '135213']

Name_list = list()
list_of_staff_post = list()

for i in range(len(udept_list)):
    for g in range(len(letters_list)):
        url = f"https://www.hse.ru/org/persons/?ltr={letters_list[g]};udept={udept_list[i]}"
        q = requests.get(url)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        persons = soup.find_all(class_="g-pic person-avatar-small2")
        for person in persons:
            person_name = person.get('title')
            Name_list.append(person_name)
        persons = soup.find_all(class_="g-pic person-avatar-small2 lazy")
        for person in persons:
            person_name = person.get('title')
            Name_list.append(person_name)
        print(f"Город {i+1}, {g+1} - Буква {letters_list[g]} обработана")
        time.sleep(random.randrange(2, 4))


    for g in range(len(letters_list)):
        url = f"https://www.hse.ru/org/persons/?ltr={letters_list[g]};udept={udept_list[i]}"
        q = requests.get(url)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        persons = soup.findAll(class_="with-indent7")
        for person in persons:
            name = person.findAll('span')
            name = str(name)
            list_of_staff_post.append(take_description(name))
        print(f'Город {i+1}, {g+1} - Буква {letters_list[g]} отработана')
        time.sleep(random.randrange(2, 4))

res_list = list()

for i in range(len(Name_list)):
    name_staff_dict = dict()
    name_staff_dict['name'] = Name_list[i]
    name_staff_dict['post'] = list_of_staff_post[i]
    res_list.append(name_staff_dict)

with open('HSE_name_staff.json', 'w', encoding = 'utf-8') as json_file:
    json_file.write(json.dumps(res_list, ensure_ascii=False, indent=1))

with open('HSE_name_staff.json', 'r', encoding='utf-8') as f:
    count_list = json.load(f)

print(len(count_list))

