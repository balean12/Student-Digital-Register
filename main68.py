'''
Created on Nov 18, 2019

@author: flavi
'''
from validare.validatoare import ValidatorStudent, ValidatorDiscipline, ValidatorGrade
from infrastructure.repos import Repo
from business.services import ServiceStudents, ServiceDisciplines, ServiceGrades
from presentation.ui import Console
from business.services import ServiceUndo
from AppSettings import *
from infrastructure.RepoTextFile import StudentTextFileRepo, DisciplineTextFileRepo, GradesTextFileRepo
from infrastructure.RepoBinaryFile import BinaryFileRepo
from infrastructure.JSONFile import JSONRepo
validatorStudent = ValidatorStudent()
validatorDiscipline = ValidatorDiscipline()
validatorGrade = ValidatorGrade()
appsettings = AppSettings()
if appsettings.Data["repository"] == "inmemory":
    repoStudents = Repo()
    repoDisciplines = Repo()
    repoGrades = Repo()
elif appsettings.Data["repository"] == "textfiles":
    repoStudents = StudentTextFileRepo(appsettings.Data["student"])
    repoDisciplines = DisciplineTextFileRepo(appsettings.Data["discipline"])
    repoGrades = GradesTextFileRepo(appsettings.Data["grade"])
elif appsettings.Data["repository"] == "binaryfile":
    repoStudents = BinaryFileRepo(appsettings.Data["student"])
    repoDisciplines = BinaryFileRepo(appsettings.Data["discipline"])
    repoGrades = BinaryFileRepo(appsettings.Data["grade"])
elif appsettings.Data["repository"] == "json":
    repoStudents = JSONRepo(appsettings.Data["student"])
    repoDisciplines = JSONRepo(appsettings.Data["discipline"])
    repoGrades = JSONRepo(appsettings.Data["grade"])
serviceUndo = ServiceUndo()
serviceStudents = ServiceStudents(repoStudents, validatorStudent, serviceUndo)
serviceDisciplines = ServiceDisciplines(repoDisciplines, validatorDiscipline, serviceUndo)
serviceGrades = ServiceGrades(repoStudents, repoDisciplines, repoGrades, validatorGrade, serviceUndo)
ui = Console(serviceStudents, serviceDisciplines, serviceGrades, serviceUndo)
ui.run()



