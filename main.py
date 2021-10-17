from pprint import pprint
import re
import csv

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_list_header = contacts_list[0]
    contacts_list.remove(contacts_list[0])

    for contact in contacts_list:
        FIO_str = contact[0] + " " + contact[1] + " " + contact[2]
        FIO_str = re.sub(r'[ ]*]', ' ', FIO_str)
        try:
            contact[0] = FIO_str.strip().split(' ')[0]
        except IndexError:
            pass
        try:
            contact[1] = FIO_str.strip().split(' ')[1]
        except IndexError:
            pass
        try:
            contact[2] = FIO_str.strip().split(' ')[2]
        except IndexError:
            pass
        nomber = re.sub(r'[\ \-\(\)]*', '', contact[5])
        nomber = re.sub(r'^(\+7)|^[8|7]?', '+7', nomber).replace('доб.', ' доб.')
        if nomber != "+7":
            contact[5] = nomber
        else:
            contact[5] = ""

        #print(f"({FIO_str}: {contact[5]}")

    for i in range(0, len(contacts_list)):
        for j in range(i, len(contacts_list)):
            if contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1]:
                for k in range(2, 6):
                    if contacts_list[i][k] == '':
                        contacts_list[i][k] == contacts_list[j][k]
                        contacts_list[j][k] == ''

    pprint(contacts_list)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_list)
