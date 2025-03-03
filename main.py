# from models.Users import Users
from models.Teachers import Teachers
from models.Students import Students
# use1=Users("moussa","moussa@gmail.com","1234","admin")
# print(use1.printUser())
# use1.nom="moussa diop"
# print(use1.nom)
# print(use1.email)
teach1=Teachers("BAILA","BAILA@gmail.com","1234","IT",500000)
student1=Students("TOTO","TOTO@gmail.com","1234","MAT001",500000)
student2=Students("TATA","TATA@gmail.com","1234","MAT002",500000)
print(teach1.PrintTeacher())
teach1.save()
student1.save()
student2.save()