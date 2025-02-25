from models.Users  import Users
class Teachers(Users):
    def __init__(self, nom:str,emai:str,password:str,role:str,grade:str,salaire:float) -> None:
        super().__init__(nom,emai,password,role)
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