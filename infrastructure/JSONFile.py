from infrastructure.repos import Repo, RepoError
from domeniu.entitati import *
import json
class JSONRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._readJSONFile()

    def _readJSONFile(self):
        try:
            f = open(self._filename, "r")
            objects = json.load(f)
            for attributes in objects["entities"]:
                obj = self._determineClassType(attributes)
                self.add(obj)
            f.close()
        except EOFError:
            raise RepoError("Empty File")
        except IOError:
            raise RepoError("Error reading file")

    def _writeToJSONFile(self):
        try:
            entities = self.get_all()
            print (len(entities))
            data = {"entities": []}
            for entity in entities:
                data["entities"].append(vars(entity))
            f = open(self._filename, "w")
            json.dump(data, f)
            f.close()
        except IOError:
            raise RepoError("Error writing to file")

    def _determineClassType(self, attributes):
        entity = None
        if self._filename == "Student.json":
            entity = Student(int(attributes["_s_id"]), attributes["_name"])
        elif self._filename == "Discipline.json":
            entity = Discipline(int(attributes["_id_disc"]), attributes["_disc_name"])
        elif self._filename == "Grade.json":
            entity = Grade(int(attributes["_id_stud"]), int(attributes["_id_disc"]), int(attributes["_grade"]))
        return entity

    def add(self, element):
        Repo.add(self, element)
        self._writeToJSONFile()

    def remove_repo(self, element):
        Repo.remove_repo(self, element)
        self._writeToJSONFile()