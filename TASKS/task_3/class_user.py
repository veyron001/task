# нужно создать класс User, который будет работать с пользователем
# подумай о классе, который будет реализовывать операции: добавить,
# изменить, получить, удалить

class Human:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def duplicate(self, username, list):
        '''Checking for duplication,

        the function receives a login and a list, the list is searched for matching
        logins. Returns the received login if no matches are found.
        Проверка на дублирование, функция получает логин и список,
        в списке происходит поиск совпадающих логинов. Возвращает
        полученный логин если не обнаружено совпадений.
        '''
        name = self.username
        for x in range(0, len(list)):
            usr = list[x]['username']
            if name.lower() == usr.lower():
                return print('Пользователь с таким логином уже существует.')
        return name

    def add_user(self, list):
        '''The add a new user method

        gets a list of users, if a login comes from the duplicate() function, it adds
        the user's dictionary to the received list and returns this list.
        Метод добавление нового пользователя получает список
        пользователей, если от функции duplicate() приходит логин, то
        добавляет словарь пользователя в полученный список и возвращает
        этот список.
        '''
        username = Human.duplicate(self, self.username, list)
        if username == None:
            pass
        else:
            id = self.id
            name = self.name
            email = self.email
            list.append({
                "id": id,
                "name": name,
                "username": username,
                "email": email,
            })
        return list

    def login_search(self, username, list):
        ''' The method of searching for a similar login,

        gets a login and a list, searches through the list, if there is a similar login,
        returns the index of the list object in which a suitable login was found.
        Метод поиска похожего логина, получает логин и список,
        производит поиск по списку, если находится похожий логин
        возвращает индекс объекта списка в котором нашелся подходящий
        логин
        '''
        name = self.username
        if name == None:
            name = ''
        else:
            name = name
        for x in range(len(list)):
            usr = list[x]['username']
            if name.lower() == usr.lower():
                return x
                break
        else:
            print('Пользователя с таким логином не существует.')

    def del_user(self, list):
        '''The method of deleting user data,

        from the function login_search() function, gets the index of the dictionary
        of the user to be deleted, deletes the object by the received index and
        returns the list.
        Метод удаления данных о пользователе, от функции login_search()
        получает индекс словаря пользователя которого необходимо
        удалить, удаляет объект по полученному индексу и возвращает
        список
        '''
        del_index = Human.login_search(self, self.username, list)
        if del_index == None:
            pass
        else:
            del list[del_index]
            self.id = None
            self.name = None
            self.username = None
            self.email = None
            del self
            return list

    def edit_user(self, list):
        '''The method of changing user data,

        from the login_search() function, gets the index of the user's dictionary
        whose data needs to be changed, provides the ability to change user data
        by the received index and returns the modified list.
        Метод изменения данных пользователя, от функции login_search()
        получает индекс словаря пользователя данные которого необходимо
        изменить, предоставляет возможность изменения данных
        пользователя по полученному индексу и возвращает измененный
        список.
        '''
        edit_index = Human.login_search(self, self.username, list)
        if edit_index == None:
            pass
        else:
            self.id = int(input('Введите id: '))
            self.name = input('Введите имя: ')
            self.username = input('Введите логин: ')
            self.email = input('Введите e-mail: ')
            list[edit_index] = {
                "id": self.id,
                "name": self.name,
                "username": self.username,
                "email": self.email,
            }
            return list

    def receive_user(self, list):
        '''The method for outputting the data of the requested object,

        receives the index of the object from the list of users from the
        login_search() function and returns the data of the selected user.
        Метод для вывода данных запрашиваемого объекта, получает от
        функции login_search() индекс объекта из списка пользователей и
        возвращает данные выбранного пользователя.
        '''
        receive_index = Human.login_search(self, self.username, list)
        if receive_index == None:
            pass
        else:
            return list[receive_index]

class User(Human):
    def __init__(self, id, name, username, email):
        Human.__init__(self, id, name, username, email)
        pass




user_data = []
user = User(1, 'qwerty1', 'qwerty001', 'asd@qwerty.com')
print(user.name)
print(user_data)
user.add_user(user_data)
print(user_data)
user2 = User(2, 'qwerty2', 'qwerty002', 'asd@qwerty.com')
user2.add_user(user_data)
print(user_data)
user3 = User(3, 'Nikolas', 'Nicopa', 'goose@qwerty.com')
user3.del_user(user_data)
user3.add_user(user_data)
print(user_data)
print(type(user3.name))
user3.edit_user(user_data)
print(user_data)
print(user3.name)
user.del_user(user_data)
print(user_data)
print(user.name)
print(user2.receive_user(user_data))