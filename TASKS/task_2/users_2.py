# Реализовать две функции:
# - поиск по e-mail, возвращает данные пользователя с заданным эмейлом
# - поиск по имени, возвращает массив с пользователями с заданным именем

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
}, {
    "id": 4,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner2@kory.org",
}, {
    "id": 5,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere2@april.biz",
}, {
    "id": 6,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger2@annie.ca",
}]

# def search_name() - performs an array search, if the entered values match,
# adds it to the list and returns it/ выполняет поиск по массиву, при
# совпадении введенных значений добавляет в список и возвращает его
def search_name(list):
    name = input('Введите имя для поиска: ')
    users_list = []
    for x in range(len(list)):
        usr = list[x]['name']
        if name.lower() == usr.lower():
            users_list.append(list[x])
    return users_list

# using the function search_name(list), it gets a list with the requested users
# and returns this list / с помощью функции search_name(list) получает
# список с запрашиваемыми пользователями и возвращает этот список
def search_user_by_name(list):
    processed_list = search_name(list)
    if processed_list == []:
        print('Такого пользователя не существует.')
        return search_user_by_name(list)
    else:
        return processed_list


# searches for an email in an array, returns the index of the user's dictionary
# if it matches / выполняет поиск емейла по массиву, при совпадении
# возвращает индекс словаря пользователя
def search_email(list):
    email = input('Введите email для поиска: ')
    for x in range(len(list)):
        usr_mail = list[x]['email']
        if email.lower() == usr_mail.lower():
            return x

# using the function search_email(list) , it gets the user's index by the
# requested email and returns the user's data according to the received index /
# с помощью функции получает индекс пользователя  по запрашиваемому
# емейлу и возвращает данные пользователя согласно полученного индекса
def user_search_by_email(list):
    user_email = search_email(list)
    if user_email == None:
        print('Пользователя с таким email не зарегистрирован.')
        return user_search_by_email(list)
    else:
        return list[user_email]



print(user_search_by_email(users))