from models.Users import Users
from database.db import db
class Students(Users):
    def __init__(self, nom:str, emai:str, password:str,matricule:str,montant:float)->None:
        super().__init__(nom, emai, password, "Student")
        self._matricule = matricule
        self._montant = montant
        
    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, matricule):
        self._matricule = matricule

    @property
    def montant(self):
        return self._montant
    
    @montant.setter
    def montant(self, montant):
        self._montant = montant
        
    def printStudent(self):
        return super().printUser() + f" Matricule: {self.matricule} Montant: {self.montant}"
    
    def save(self):
        user_table = db.table('Users')
        id=len(user_table)+1
        user_table.insert({
            'id': id,
            'nom': self.nom,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'matricule': self.matricule,
            'montant': self.montant
        })