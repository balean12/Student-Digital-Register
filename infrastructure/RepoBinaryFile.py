from infrastructure.repos import Repo, RepoError

from domeniu.entitati import *
import pickle
class BinaryFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        #self._readBinaryFile()

    def _readBinaryFile(self):
        try:
            f = open(self._filename, "rb")
            objects = pickle.load(f)
            for obj in objects:
                super().add(obj)
            f.close()
        except EOFError:
            raise RepoError("Empty File")
        except IOError:
            raise RepoError("Error reading file")

    def _writeToBinaryFile(self):
        try:
            f = open(self._filename, "wb")
            entities = self.get_all()
            pickle.dump(entities, f)
            f.close()
        except IOError:
            raise RepoError("Error writing file")

    def add(self, object):
        Repo.add(self, object)
        self._writeToBinaryFile()

    def remove_repo(self, object):
        Repo.remove_repo(self, object)
        self._writeToBinaryFile()