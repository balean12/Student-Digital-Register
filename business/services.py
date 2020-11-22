from domeniu.entitati import Student, Discipline, Grade, StudentDTO, DisciplineDTO
import random
from erori.exceptii import RepoError, UndoError
from Iterable import *

class ServiceStudents(object):
    
    def __init__(self, repoStudents, validatorStudents, undoService):
        self._repoStudents = repoStudents
        self._validatorStudents = validatorStudents
        self._undoService = undoService

    def sortStudsById(self):
        listaStudenti = self._repoStudents.get_all()
        gnomeSort(listaStudenti,itemComaparison)
        return listaStudenti

    def filterIds(self):
        listaStudenti = self._repoStudents.get_all()
        res = filterList(listaStudenti)
        return res

    def get_no_students(self):
        """
        Returns the size of the repoStudents
        """
        return self._repoStudents.size()

    def add_student(self, s_id, name, from_undo = False):
        """
        Creates a student that will be added in the repoStudents
        :params s_id = id-ul noului elev creat
        :params name = numele noului elev creat
        :params from_undo: False if the function eas not called from the undo option, True otherwise
        """
        student = Student(s_id, name)
        self._validatorStudents.validate_student(student)
        self._repoStudents.add(student)
        if not from_undo:
            function = FunctionCall(self.add_student, s_id, name , True)
            reverse_function = FunctionCall(self.remove_student, s_id , True)
            operation = Operation(function, reverse_function)
            self._undoService.record_operation(operation)
    
    def get_student_by_id(self, s_id):
        """
        Returns a student from repo by id
        :params s_id = id-ul studentului
        """
        key = Student(s_id , None)
        return self._repoStudents.search(key)
    
    def get_students_by_name(self, name):
        """
        Returns a student from repo by name
        :params name = name studentului
        """
        students = [s for s in self._repoStudents.get_all() if name in s.get_name()]
        return students
        
    def remove_student(self, s_id, from_undo = False):
        """
        Removes a student from repo 
        :params s_id = id-ul studentului care va fi sters
        :params from_undo: False if the function eas not called from the undo option, True otherwise
        """
        student = Student(s_id, None)
        deleted_student = self._repoStudents.search(student)
        self._repoStudents.remove_repo(student)
        if not from_undo:
            function = FunctionCall(self.remove_student, s_id, True)
            reverse_function = FunctionCall(self.add_student, s_id , deleted_student.get_name(), True)
            operation = Operation(function, reverse_function)
            cascaded_operation = CascadedOperation()
            cascaded_operation.add(operation)
            self._undoService.record_operation(cascaded_operation)
                                               
    def update_student(self, new):
        """
        Changes a student's name
        :params new = Student who's name is to be changed
        """
        student = self._repoStudents.search(new)
        student.set_name(new.get_name())
        
    def get_students(self):
        """
        Returns all students from repo
        """
        if len(self._repoStudents.get_all()) == 0:
            raise RepoError("Repo Empty")
        return self._repoStudents.get_all()
    
    def create_init_studs(self):
            id_base = 1
            lista_studenti = ["Mario", "Dan", "Clara", "Flora", "Jane", "Jack", "Kis", "Barney", "Hector", "Ken"]
            for i in range(0, 10):
                s = Student(id_base, random.choice(lista_studenti))
                id_base+=1
                self._repoStudents.add(s)
    

class ServiceDisciplines(object):
    
    def __init__(self, repoDisciplines, validatorDiscipline, undoService):
        self._repoDisciplines = repoDisciplines
        self._validatorDiscipline = validatorDiscipline
        self._undoService = undoService
    def add_disc(self, id_disc, name_disc, from_undo = False):
        """
        Creates a discipline that will be added in the repoDisciplines
        :params id_disc = The id of the new discipline
        :params name_disc = The name of the new discipline
        :params from_undo: False if the function eas not called from the undo option, True otherwise
        """
        discipline = Discipline(id_disc, name_disc)
        self._validatorDiscipline.validate_disc(discipline)
        self._repoDisciplines.add(discipline)
        if not from_undo:
            function = FunctionCall(self.add_disc,id_disc , name_disc, True)
            reverse_function = FunctionCall(self.remove_disc , id_disc, True)
            operation = Operation(function, reverse_function)
            self._undoService.record_operation(operation)
    
    def get_disc(self):
        """
        Returns all disciplines from repo
        """
        return self._repoDisciplines.get_all()
    
    def get_disc_by_id(self, disc_id):
        """
        Returns all disciplines with the given id
        :params disc_id = given id
        """
        key = Discipline(disc_id, None)
        return self._repoDisciplines.search(key)
    
    def get_discipline_by_name(self, name):
        """
        Returns all disciplines with the given name
        :params name = given name
        """
        disciplines = [d for d in self._repoDisciplines.get_all() if name in d.get_disc_name()]
        return disciplines
    
    def get_disc_no(self):
        """
        Returns the size of repoDisciplines
        """
        return self._repoDisciplines.size()
    
    def update_discipline(self, new):
        """
        Changes the name of a given discipline
        :params new = the discipline whose name is to be changed
        """
        discipline = self._repoDisciplines.search(new)
        discipline.set_disc_name(new.get_disc_name())
            
    def create_init_discs(self):
        #lista_disc = [(1,"Bio"), (2,"Algebra"), (3,"Geometry"), (4,"Informathics"), (5,"Chemistry"), (6,"Sport"), (7,"Marketing"), (8,"Economics"), (9,"Volunteering"), (10,"Nutrition")]
        lista_disc = ["Bio", "Algebra", "Geometry", "Informathics", "Chemistry", "Sport", "Marketing", "Economics", "Volunteering", "Nutrition"]
        i = 10
        while i > 0:
            #d = Discipline(id_base, random.choice(lista_disc))
            idx_dis = random.randrange(0, len(lista_disc))
            d = Discipline(idx_dis, lista_disc[idx_dis])
            #id_base+=1
            try:
                self._repoDisciplines.add(d)
                i-=1
            except RepoError:
                pass
            
    def remove_disc(self , id_disc, from_undo = False):
        """
        Removes disciplines with the given id
        :params id_disc = The id of the discipline to be deleted
        :params from_undo :False if the function eas not called from the undo option, True otherwise
        """
        disc= Discipline(id_disc, None)
        deleted_disc = self._repoDisciplines.search(disc)
        self._repoDisciplines.remove_repo(disc)
        if not from_undo:
            function = FunctionCall(self.remove_disc, id_disc, True)
            reverse_function = FunctionCall(self.add_disc, id_disc, deleted_disc.get_disc_name(), True)
            operation = Operation(function, reverse_function)
            cascaded_operation = CascadedOperation()
            cascaded_operation.add(operation)
            self._undoService.record_operation(cascaded_operation)
           
    
class ServiceGrades(object):
    def __init__(self, repoStudents, repoDisciplines, repoGrades , validatorGrade, undoService):
        self._repoStudents = repoStudents
        self._repoDisciplines = repoDisciplines
        self._repoGrades = repoGrades
        self._validatorGrade = validatorGrade
        self._undoService = undoService

    def get_grades_no(self):
        """
        Returns the size of repogrades
        """
        return self._repoGrades.size()

    def give_grade(self, id_stud, id_disc, grade, from_undo = False ):
        """
        Adds a new grade in the repo
        :params id_stud = Student's id
        :params id_disc = Discipline's id
        :params grade = grade
        :params from_undo : False if the function eas not called from the undo option, True otherwise
        """
        grade_stud = Grade(id_stud, id_disc, grade)
        self._repoGrades.add_grade(grade_stud)
        if not from_undo:
            function = FunctionCall(self.give_grade, id_stud, id_disc, grade , True)
            reverse_function = FunctionCall(self.remove_grade_by_idStud_and_grade, id_stud, id_disc, grade, True)
            operation = Operation(function, reverse_function)
            self._undoService.record_operation(operation)
    def get_grades(self):
        """
        Returns all grades
        """
        return self._repoGrades.get_all()
    
    def remove_grade_by_student_id(self, s_id, from_undo = False):
        """
        Removes a grade by student's id
        :params s_id = Student's id
        :params from_undo = False if the function eas not called from the undo option, True otherwise
        """
        #grade = Grade(s_id, None, None)
        #self._repoGrades.remove_repo(grade)
        deleted_grades = []
        grades = [g for g in self._repoGrades.get_all() if g.get_id_stud() == s_id]
        for g in grades:
            deleted_grades.append(g)
            self._repoGrades.remove_repo(g)   
        if not from_undo:
            function = FunctionCall(self.remove_grade_by_student_id, s_id, True)
            reverse_function = FunctionCall(self.add_deleted_grades, deleted_grades )
            operation = Operation(function, reverse_function)
            #cascaded_operation = CascadedOperation()
            #cascaded_operation.add(operation)
            self._undoService.record_operation(operation)
    def remove_grade_by_idStud_and_grade(self, s_id, d_id, grade, from_undo = False):
        deleted_grades = []
        grades = [g for g in self._repoGrades.get_all() if g.get_id_stud() == s_id and g.get_id_disc() == d_id and g.get_grade() == grade]
        for g in grades:
            deleted_grades.append(g)
            self._repoGrades.remove_repo(g)
        if not from_undo:
                function = FunctionCall(self.remove_grade_by_idStud_and_grade, s_id, d_id, grade, True)
                reverse_function = FunctionCall(self.add_deleted_grades, deleted_grades)
                operation = Operation(function, reverse_function)
                # cascaded_operation = CascadedOperation()
                # cascaded_operation.add(operation)
                self._undoService.record_operation(operation)

    def remove_grade_by_disc_id(self, d_id, from_undo = False):
        """
        Removes a grade by discipline's id
        :params s_id = Student's id
        :params from_undo = False if the function eas not called from the undo option, True otherwise
        """
        deleted_grades = []
        grades = [d for d in self._repoGrades.get_all() if d.get_id_disc() == d_id ]
        for d in grades:
            deleted_grades.append(d)
            self._repoGrades.remove_repo(d)
        if not from_undo:
            function = FunctionCall(self.remove_grade_by_disc_id, d_id, True)
            reverse_function = FunctionCall(self.add_deleted_grades, deleted_grades )
            operation = Operation(function, reverse_function)
            #cascaded_operation = CascadedOperation()
            #cascaded_operation.add(operation)
            self._undoService.record_operation(operation)

    def add_deleted_grades(self, deleted_grades):
        for grade in deleted_grades:
            self._repoGrades.add(grade)

    def create_init_grades(self):
        id_base = 1
        grades = [1,2,3,4,5,6,7,8,9,10]
        id_disc  = [0,1,2,3,4,5,6,7,8,9]
        for i in range(0,10):
            g = Grade(id_base, random.choice(id_disc) , random.choice(grades))
            id_base+=1
            self._repoGrades.add(g)

    def grades_average(self):
        """
        Calculates the average of the grades and shows the students that fail
        """
        stud_dict = {}
        for grade in self._repoGrades.get_all():
            if (grade.get_id_stud(), grade.get_id_disc()) not in stud_dict:
                stud_dict[(grade.get_id_stud(), grade.get_id_disc())] = []
            stud_dict[(grade.get_id_stud(), grade.get_id_disc())].append(grade.get_grade())
        res = []
        for item in stud_dict.items():
            average = sum(item[1])/len(item[1])
            if average < 5:
                student = self._repoStudents.search(Student(item[0][0], ""))
                res.append(StudentDTO(student, average))
        return res
    
    def best_students(self):
        """
        Creates statisctic! More precisely, it returns the students with the best averages
        """
        stud_dict = {}
        for grade in self._repoGrades.get_all():
            if (grade.get_id_stud()) not in stud_dict:
                stud_dict[grade.get_id_stud()] = []
            stud_dict[grade.get_id_stud()].append(grade.get_grade())
        res = []
        for item in stud_dict.items():
            average = sum(item[1])/len(item[1])
            student = self._repoStudents.search(Student(item[0], ""))
            res.append(StudentDTO(student, average))
        return res
    
    def average_student_discipline(self, id_disc):
        """
        Calculates the average at one discipline!
        """
        indx = 0
        suma = 0
        for grade in self._repoGrades.get_all():
            if grade.get_id_disc() == id_disc:
                suma += grade.get_grade()
                indx += 1
        average_disc = suma/indx
        return average_disc

    def find_by_id(self, id_disc):
        list_disc = self._repoDisciplines.get_all()
        for d in list_disc:
            if id_disc == d.get_id_disc():
                return d
    
    def dict_to_list(self, dict_disc):
        """
        Converts a dictionary to a list!
        """
        lista_obiecte_DTO = []
        for item in dict_disc.items():
            disciplina = self.find_by_id(item[0])
            lista_obiecte_DTO.append(DisciplineDTO(disciplina, item[1]))
        return lista_obiecte_DTO
    
    def best_disciplines(self):
        """
        Returns the disciplines with best averages
        """
        dict_disc = {}
        for grade in self._repoGrades.get_all():
            if grade.get_id_disc() not in dict_disc:
                dict_disc[grade.get_id_disc()] = self.average_student_discipline(grade.get_id_disc())
        return self.dict_to_list(dict_disc)

class ServiceUndo(object):
    def __init__(self):
        self._undo_list = []
        self._redo_list = []
    
    def record_operation(self, operation):
        self._undo_list.append(operation)
        self.clear_redo_list()
    
    def add_to_cascaded_operation(self, operation):
        self._undo_list[-1].add(operation)
    
    def clear_redo_list(self):
        self._redo_list.clear()
    
    def clear_undo_list(self):
        self._undo_list.clear()
    
    def undo(self):
        if len(self._undo_list) == 0:
            raise UndoError("No more undos!")
        else:
            operation = self._undo_list.pop()
            self._redo_list.append(operation)
            operation.undo()
    
    def redo(self):
        if len(self._redo_list) == 0:
            raise UndoError("No more redos!")
        else:
            operation = self._redo_list.pop()
            self._undo_list.append(operation)
            operation.redo()

class FunctionCall:
    def __init__(self, function, *parameters):
        self._function  = function
        self._params = parameters
    
    def call(self):
        self._function(*self._params)

class Operation:
    def __init__(self, function, reverse_function):
        self._function = function
        self._reverse_function = reverse_function
    
    def undo(self):
        self._reverse_function.call()
    
    def redo(self):
        self._function.call()

class CascadedOperation:
    def __init__(self):
        self._operations = []
    
    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for o in self._operations:
            o.undo()

    def redo(self):
        for o in self._operations:
            o.redo()