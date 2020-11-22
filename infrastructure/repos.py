from erori.exceptii import RepoError
from domeniu.entitati import Student, Discipline, Grade
import pickle
from Iterable import Lista, ListIterator
class Repo(object):
    def __init__(self):
        """
        Initializes an empty repo which is a list!
        """
        self._entities = Lista()
    
    def size(self):
        """
        Returns the length of the repo
        """
        return len(self._entities)

    def add(self, element):
        """
        Adds a new element in the repo
        :params element = the new element
        """
        if element in self._entities:   
            raise RepoError("id existent!\n")
        self._entities.append(element)
    
    def add_grade(self, element):
        """
        Adds a new grade in the repo! This is used only for REPOGRADES because there grades can have the same id
        :params element = the new element
        """
        self._entities.append(element)
    
    def search(self, element):
        """
        Searches for an element in the repo
        :params element = element to be looking for
        :return: the element looked for
        """
        if element not in self._entities:
            raise RepoError("id inexistent!\n")
        for x in self._entities:
            if x == element:
                return x
    '''
    This function removes an element from repo
    '''
    def remove_repo(self, element):
        """
        Removes an element from repo
        :params element = the element to be deleted
        """
        self._entities.remove(element)
    '''
    This function gets all the elements from repo
    '''
    def get_all(self):
        """
        Returns all elements from a repo
        """
        return self._entities[:]



