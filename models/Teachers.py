from models.Users  import Users
from database.db import db
class Teachers(Users):
    def __init__(self, nom:str,emai:str,password:str,grade:str,salaire:float) -> None:
        super().__init__(nom,emai,password,"Teacher")
        self._grade=grade
        self._salaire=salaire
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,newgrade):
        self._grade=newgrade
        
    @property
    def salaire(self):
        return self._salaire
    @salaire.setter
    def salaire(self,newsalaire):
        self._salaire=newsalaire
        
    def PrintTeacher(self):
        return super().printUser() + f"\n Grade:{self.grade} Salaire:{self.salaire}"
    
    def save(self):
        user_table = db.table('Users')
        id=len(user_table)+1
        user_table.insert({
            'id': id,
            'nom': self.nom,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'salaire': self.salaire,
            'grade': self.grade
        })