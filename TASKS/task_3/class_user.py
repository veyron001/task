class User():
    users_list = []
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        User.users_list.append({
             'id' : self.id,
             'name' : self.name,
             'username' : self.username,
             'email' : self.email
        })
class OperationsOnUsers(User):
    def __init__(self):
        pass

    def UserDelete(self):
        pass
    def UserEdit(self):
        pass
    def UserAdd(self):
        pass




user = User(1, "Victor", "viking001", "vik_1006@type.com")
print(user.email)
listik = [{'email' : 'qwerty@rust.com'}]
print(listik[0]['email'])
listik[0]['email'] = user.email
print(listik[0]['email'])


