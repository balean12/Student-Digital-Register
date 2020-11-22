############################################   
from domeniu.entitati import Student, Discipline, Grade
from validare.validatoare import ValidatorStudent, ValidatorDiscipline , ValidatorGrade
from erori.exceptii import ValidError, RepoError
from infrastructure.repos import Repo
from business.services import ServiceStudents, ServiceDisciplines, ServiceGrades , ServiceUndo
from Iterable import *
import unittest
class TesteStudent(unittest.TestCase):
    def setUp(self):
        self._student1 = Student(20, "A")
        self._student2 = Student(21, "B")
        self._student3 = Student(22, "C")
        self._bad_id_student = Student(-20, "B")
        self._bad_name_student = Student(20, "")
        self._validStud = ValidatorStudent()
        self._repo = Repo()
        self._undoService = ServiceUndo()
        self._servStudent = ServiceStudents(self._repo, self._validStud, self._undoService)

    def test_create_student(self):
        self.assertEqual(self._student1.get_name(), "A")
        self.assertEqual(self._student1.get_s_id(), 20)
        self._student3.set_s_id(15)
        self.assertEqual(self._student3.get_s_id(), 15)
        self._student1.set_name("Karl")
        self.assertEqual(self._student1.get_name(), "Karl")
        self._other_student_same_id = Student(20, "Bob")
        self.assertEqual(self._other_student_same_id.get_s_id(), self._student1.get_s_id())
    def testSortingGnome(self):
        listastuds = []
        listastuds.append(self._student2)
        listastuds.append(self._student3)
        listastuds.append(self._student1)
        gnomeSort(listastuds)
        self.assertEqual(listastuds[0].get_s_id(), self._student1.get_s_id())
        self.assertEqual(listastuds[1].get_s_id(), self._student2.get_s_id())
    def testFiltering(self):
        listastuds = []
        listastuds.append(self._student2)
        listastuds.append(self._student3)
        listastuds.append(self._student1)
        res = filterList(listastuds)
        self.assertEqual(len(res), 1)

    def test_get_all(self):
        self._servStudent.add_student(1, "George")
        self._servStudent.add_student(2, "Marcu")
        students = self._servStudent.get_students()
        self.assertEqual(students[0].get_name(), "George")
        self.assertEqual(students[1].get_name(), "Marcu")
        self.assertEqual(len(students), 2)
    def test_validator_student(self):
        self._validStud.validate_student(self._student1)
        try:
            self._validStud.validate_student(self._bad_id_student)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid!\n")
        try:
            self._validStud.validate_student(self._bad_name_student)    
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "name invalid!\n")  
    def test_add_search_remove_repo(self):
        self.assertEqual(self._repo.size(), 0)
        self._repo.add(self._student1)
        self._repo.add(self._student2)
        self.assertEqual(self._repo.size(), 2)
        self._repo.remove_repo(self._student2)
        self.assertEqual(self._repo.size(), 1)
        #In repo a ramas doar student1! Pay attention!
        self._other_student_same_id = Student(20, "Bob")
        key_student = Student(self._student1.get_s_id(), None)
        student_found = self._repo.search(key_student)
        self.assertEqual(student_found.get_name(), self._student1.get_name())
        try:
            self._repo.add(self._other_student_same_id)
            assert (False)
        except RepoError as re:
            assert(str(re) == "id existent!\n")
        self._other_student = Student(100, "Mane")
        try:
            self._repo.search(self._other_student)
            assert (False)
        except RepoError as re:
            assert(str(re) == "id inexistent!\n")
    def test_add_searchById_searchByName_remove_update_Service(self):
        self.assertEqual(self._servStudent.get_no_students(), 0)
        self._servStudent.add_student(25, "Sparrow")
        self._servStudent.add_student(26, "Spar")
        self.assertEqual(self._servStudent.get_no_students(), 2)
        self._servStudent.remove_student(26)
        self.assertEqual(self._servStudent.get_no_students(), 1)
        student_found = self._servStudent.get_student_by_id(25)
        self.assertEqual(student_found.get_name(),"Sparrow")
        try:
            self._servStudent.add_student(-23, "Hans")
            assert (False)
        except ValidError as ve:
            assert(str(ve) == "id invalid!\n")
        try:
            self._servStudent.add_student(20,"")
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "name invalid!\n")
        try:
            self._servStudent.add_student(25, "Jack")
            assert (False)
        except RepoError as re:
            assert(str(re) == "id existent!\n")
        try:
            self._servStudent.get_student_by_id(44)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id inexistent!\n")
        new = Student(25, "Danielo")
        self._servStudent.update_student(new)
        self.assertEqual(new.get_name(), "Danielo")
        self._servStudent.add_student(55, "Ken")
        self._servStudent.add_student(56, "Ben")    
        self._servStudent.add_student(57, "Men")
        self._servStudent.add_student(58, "Fen")
        students = self._servStudent.get_students_by_name("en")
        self.assertEqual(len(students), 4)

    def test_create_init_studs(self):
        self._servStudent.create_init_studs()
        self.assertEqual(self._repo.size(), 10)
class TesteDiscipline(unittest.TestCase):
    def setUp(self):
        self._discipline1 = Discipline(50, "Math")
        self._discipline2 = Discipline(80, "Drawing")
        self._discipline3 = Discipline(90, "Flying")
        self._bad_id_discipline = Discipline(-20, "Algebra")
        self._bad_name_discipline = Discipline(20, "")
        self._validDisc = ValidatorDiscipline()
        self._repo = Repo()
        self._undoService  = ServiceUndo()
        self._servDiscipline = ServiceDisciplines(self._repo, self._validDisc, self._undoService)
        
    def test_create_discipline(self):
        self.assertEqual(self._discipline1.get_id_disc(), 50)
        self.assertEqual(self._discipline1.get_disc_name(), "Math")
        self._discipline1.set_disc_name("Trigo")
        self._discipline3.set_id_disc(49)
        self.assertEqual(self._discipline1.get_disc_name(), "Trigo")
        self.assertEqual(self._discipline3.get_id_disc(), 49)
        self._other_disc_same_id = Discipline(50, "Sport")
        self.assertEqual(self._other_disc_same_id.get_id_disc(), 50)
        self.assertEqual(self._other_disc_same_id.get_disc_name(),"Sport")
        self.assertEqual(self._discipline1.get_id_disc(), self._other_disc_same_id.get_id_disc())
    
    def test_validator_discipline(self):
        self._validDisc.validate_disc(self._discipline1)
        try:
            self._validDisc.validate_disc(self._bad_id_discipline)
            assert (False)
        except ValidError as ve:
            assert(str(ve) == "id invalid!\n")
        try:
            self._validDisc.validate_disc(self._bad_name_discipline)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "name invalid!\n")
    def test_get_all_discs(self):
        self._servDiscipline.add_disc(1, "Fifi")
        self._servDiscipline.add_disc(2, "Gigi")
        disciplines = self._servDiscipline.get_disc()
        self.assertEqual(len(disciplines), 2)
    def test_add_searchById_searchByName_remove_update_repo(self):
        self.assertEqual(self._repo.size(), 0)
        self._repo.add(self._discipline1)
        self._repo.add(self._discipline2)
        self.assertEqual(self._repo.size(), 2)
        self._repo.remove_repo(self._discipline2)
        self.assertEqual(self._repo.size(), 1)
        self._other_disc_same_id = Discipline(50, "Biology")
        self.assertEqual(self._other_disc_same_id.get_disc_name(), "Biology")
        self.assertEqual(self._other_disc_same_id.get_id_disc(), 50)
        key_disc = Discipline(self._discipline1.get_id_disc(), None)
        disc_found = self._repo.search(key_disc)
        self.assertEqual(disc_found.get_disc_name(), self._discipline1.get_disc_name())
        try:
            self._repo.add(self._other_disc_same_id)
            assert (False)
        except RepoError as re:
            assert(str(re) == "id existent!\n")
        self._other_discipline = Discipline(100, "Mapping")
        try:
            self._repo.search(self._other_discipline)
            assert (False)
        except RepoError as re:
            assert (str(re) == "id inexistent!\n")

    def test_add_searchById_searchByName_remove_update_Service(self):
        self.assertEqual(self._servDiscipline.get_disc_no(), 0)
        self._servDiscipline.add_disc(30, "Bio")
        self._servDiscipline.add_disc(31, "Hiking")
        self.assertEqual(self._servDiscipline.get_disc_no(), 2)
        self._servDiscipline.remove_disc(31)
        self.assertEqual(self._servDiscipline.get_disc_no(), 1)
        disc_found = self._servDiscipline.get_disc_by_id(30)
        self.assertEqual(disc_found.get_disc_name(), "Bio")
        try:
            self._servDiscipline.add_disc(-23, "Chemistry")
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "id invalid!\n")
        try:
            self._servDiscipline.add_disc(3, "")
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "name invalid!\n")
        try:
            self._servDiscipline.add_disc(30, "Guitar")
            assert (False)
        except RepoError as re:
            assert (str(re) == "id existent!\n")
        try:
            self._servDiscipline.get_disc_by_id(98)
            assert (False)
        except RepoError as re:
            assert (str(re) == "id inexistent!\n")
        new = Discipline(30, "Piano")
        self._servDiscipline.update_discipline(new)
        self.assertEqual(new.get_disc_name(), "Piano")
        self._servDiscipline.add_disc(55, "Violin")
        self._servDiscipline.add_disc(56, "Games")
        self._servDiscipline.add_disc(57, "Coding")
        self._servDiscipline.add_disc(58, "Nustiu")
        disciplines = self._servDiscipline.get_discipline_by_name("i")
        self.assertEqual(len(disciplines), 4)

    def test_init_discs(self):
        self._servDiscipline.create_init_discs()
        self.assertEqual(self._repo.size(), 10)

        
class TesteGrade(unittest.TestCase):
    def setUp(self):
        self._grade = Grade(20, 30, 10)
        self._bad_id_student_grade = Grade(-20, 20, 10)
        self._bad_id_disc_grade = Grade(20,-20, 10)
        self._bad_grade = Grade(20, 20, -5)
        self._validGrade = ValidatorGrade()
        self._validStud = ValidatorStudent()
        self._validDisc = ValidatorDiscipline()
        self._undoService = ServiceUndo()
        self._repoStudents = Repo()
        self._repoGrades = Repo()
        self._repoDisciplines = Repo()
        self._serviceStudent = ServiceStudents(self._repoStudents, self._validStud, self._undoService)
        self._serviceDisc = ServiceDisciplines(self._repoDisciplines, self._validDisc, self._undoService)
        self._gradeService = ServiceGrades(self._repoStudents, self._repoDisciplines, self._repoGrades, self._validGrade, self._undoService )
    def test_create_grade(self):
        self.assertEqual(self._grade.get_id_stud(),20)
        self.assertEqual(self._grade.get_id_disc(),30)
        self.assertEqual(self._grade.get_grade(),10)
        self._grade.set_id_stud(1)
        self._grade.set_id_disc(1)
        self._grade.set_grade(1)
        self.assertEqual(self._grade.get_id_stud(),1)
        self.assertEqual(self._grade.get_id_disc(),1)
        self.assertEqual(self._grade.get_grade(),1)
        self._otherGrade_same_id = Grade(1, 1, 5)
        self.assertEqual(self._otherGrade_same_id.get_id_disc() and self._otherGrade_same_id.get_id_stud(), self._grade.get_id_disc() and self._grade.get_id_stud())

    def test_creat_init_grades(self):
        self._gradeService.create_init_grades()
        self.assertEqual(self._repoGrades.size(), 10)

    def test_validator_grade(self):
        self._validGrade.validate_grade(self._grade)
        try:
            self._validGrade.validate_grade(self._bad_id_student_grade)
            assert (False)
        except ValidError as ve:
            assert(str(ve) == "id student invalid!\n")
        try:
            self._validGrade.validate_grade(self._bad_id_disc_grade)
            assert (False)
        except ValidError as ve:
            assert(str(ve) == "id discipline invalid!\n")
        try:
            self._validGrade.validate_grade(self._bad_grade)
            assert (False)
        except ValidError as ve:
            assert(str(ve) == "grade invalid!\n")

    def test_add_remove_repo(self):
        self.assertEqual(self._repoGrades.size(), 0)
        self._repoGrades.add_grade(self._grade)
        self.assertEqual(self._repoGrades.size(), 1)
        self._repoGrades.remove_repo(self._grade)
        self.assertEqual(self._repoGrades.size(), 0)
        self._grade2 = Grade(5, 8, 9)
        self._repoGrades.add_grade(self._grade)

    def test_add_removebyID_average_SERVICE(self):
        #self._gradeService.give_grade(4, 5, 6)
        #grades = self._gradeService.get_grades()
        #self.assertEqual(len(grades) ,1)
        self.assertEqual(self._gradeService.get_grades_no(), 0)
        self._gradeService.give_grade(9, 3, 5)
        self._gradeService.give_grade(9, 4, 8)
        self.assertEqual(self._gradeService.get_grades_no(), 2)
        self._gradeService.remove_grade_by_idStud_and_grade(9,3 ,5)
        self.assertEqual(self._gradeService.get_grades_no(), 1)
        self._gradeService.remove_grade_by_disc_id(4)
        self.assertEqual(self._gradeService.get_grades_no(),0)
        self._gradeService.give_grade(1, 8, 10)
        self._gradeService.remove_grade_by_student_id(1)
        self.assertEqual(self._gradeService.get_grades_no(), 0)
        self._gradeService.give_grade(1, 1, 1)
        grades = self._gradeService.get_grades()
        self.assertEqual(len(grades) ,1 )
        self._serviceStudent.add_student(1, "Jane")
        self._serviceStudent.add_student(2, "Marc")
        self._gradeService.give_grade(2, 2, 1)
        self._gradeService.give_grade(1, 3, 2)
        failing_students = self._gradeService.grades_average()
        self.assertEqual(len(failing_students), 3)
        average_disc= self._gradeService.average_student_discipline(2)
        self.assertEqual(average_disc, 1.0)
        best_studs = self._gradeService.best_students()
        self.assertEqual(len(best_studs), 2)
        self.assertEqual(best_studs[0].get_student(), Student(1, "Jane"))
        self.assertEqual(best_studs[0].get_stud_average(), 1.5)
        self._repoDisciplines.add(Discipline(2, "Ala"))
        self._repoDisciplines.add(Discipline(3, "Kaka"))
        grade = self._gradeService.find_by_id(2)
        self.assertEqual(grade.get_id_disc(), 2)
        best_disc = self._gradeService.best_disciplines()
        self.assertEqual(len(best_disc), 3)
        self.assertEqual(best_disc[0].get_discipline(), None)
        self.assertEqual(best_disc[1].get_disc_average(), 1.0)
