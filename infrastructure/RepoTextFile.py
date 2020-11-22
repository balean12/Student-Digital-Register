from infrastructure.repos import Repo, RepoError
from domeniu.entitati import *

class StudentTextFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._readFromFile()
    def _readFromFile(self):
       try:
           f = open(self._filename, "r")
           line = f.readline().strip()
           while len(line) > 0:
               line = line.split(",")
               student = Student(int(line[0]), line[1])
               super().add(student)
               line = f.readline().strip()
           f.close()
       except IOError as e:
           print("An error occured - " + str(e))
           raise e

    def add(self, object):
        Repo.add(self, object)
        self._writeToFile()

    def remove_repo(self, object):
        Repo.remove_repo(self, object)
        self._writeToFile()

    def _writeToFile(self):
        f = open(self._filename, "w")
        listaStudenti = Repo.get_all(self)
        for element in listaStudenti:
            f.write(str(element.get_s_id()) + "," + element.get_name() + "\n")
        f.close()

class DisciplineTextFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._readFromFile()
    def _readFromFile(self):
        try:
            f = open(self._filename, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                discipline = Discipline( int(line[0]), line[1])
                super().add(discipline)
                line = f.readline().strip()
            f.close()
        except EOFError as e:
            print("An error occured - " + str(e))
            raise e
    def add(self, object):
        Repo.add(self, object)
        self._writeToFile()

    def remove_repo(self, object):
        Repo.remove_repo(self, object)
        self._writeToFile()

    def _writeToFile(self):
        f = open(self._filename, "w")
        listaDiscipline = Repo.get_all(self)
        for element in listaDiscipline:
            f.write(str(element.get_id_disc()) + ", " + element.get_disc_name())

class GradesTextFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._readFromFile()

    def _readFromFile(self):
        try:
            f = open(self._filename, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                grade = Grade(int(line[0]), int(line[1]), int(line[2]))
                super().add(grade)
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print("An error occured - " + str(e))
            raise e

    def add(self, object):
        Repo.add(self, object)
        self._writeToFile()

    def remove_repo(self, object):
        Repo.remove_repo(self, object)
        self._writeToFile()

    def _writeToFile(self):
        f = open(self._filename, "w")
        listGrades = Repo.get_all(self)
        for element in listGrades:
            f.write(str(element.get_id_stud()) + ", " + str(element.get_id_disc()) + ", " + str(element.get_grade()))
        f.close()