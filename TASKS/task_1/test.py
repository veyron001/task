users = [{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
}, {
    "id": 2,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
}, {
    "id": 3,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
}]


def login_search(list):
    name = input('Введите логин: ')
    for x in range(len(list)):
        usr = list[x]['username']
        if name.lower() == usr.lower():
            return x
            break
    else:
        print('Такого пользователя не существует.')


def del_user(list):
    print('Введите логин для удаления')
    name = login_search(list)
    if name == None:
        del_user(list)
    else:
        del list[name]
        return list


del_user(users)