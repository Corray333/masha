import json
import helpers

exit = False
file = open('db.txt', 'r', encoding='utf-8')
users = json.loads(file.read())
def userList():
    for user in users:
        print(user['name'])

def addUser():
    user = {
        'name': '',
        'surname': '',
        'fathername':'',
        'login':'',
        'phone':'',
        'email':'',
        'password':''
    }
    user['name'] = input('Введите имя пользователя: ')
    if(helpers.wordValidation(user['name']) == False):
        user['name'] = input('Имя не должно содержать цифры и спец символы! Введите имя в правильном формате: ')
    # То же самое для остальных параметров
    users.append(user)



while exit != True:
    print('Меню:\n1. Посмотреть список пользователей\n2. Добавить пользователя. \n3. Удалить пользователя \n 4. Изменить пользователя')
    option = int(input())
    if option == 1:
        userList()
    elif option == 2:
        addUser()