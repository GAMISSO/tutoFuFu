from database.db import db
class Users:
    def __init__(self, nom:str,emai:str,password:str,role:str) -> None: #constructeur
        self._nom = nom
        self._email = emai
        self._password = password
        self._role = role
    @property #getters
    def nom(self):
        return self._nom
    @nom.setter #setters
    def nom(self,newnom:str):
        self._nom = newnom
    @property #getters
    def email(self):
        return self._email
    @email.setter #setters
    def email(self,newemail:str):
        self._email = newemail
    @property #getters
    def password(self):
        return self._password
    @password.setter #setters
    def password(self,newpassword:str):
        self._password = newpassword
    @property #getters
    def role(self):
        return self._role
    @role.setter #setters
    def role(self,newrole:str):
        self._role = newrole
        
    def printUser(self):
        return f"Nom: {self._nom}, Email: {self._email}, Role: {self._role}"
    
    def save(self):
        user_table = db.table('Users')
        id=len(user_table)+1
        user_table.insert({
            'id': id,
            'name': self.nom,
            'email': self.email,
            'password': self.password,
           
        })
    
