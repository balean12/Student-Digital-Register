from erori.exceptii import ValidError, RepoError, UndoError
import random
from domeniu.entitati import Student, Discipline, Grade, StudentDTO
from business.services import ServiceUndo
from AppSettings import *


class Console(object):

    def _ui_add_stud(self, params):
        if len(params) != 2:
            raise ValueError("No. params invalid! Must be 2!")
        s_id = int(params[0])
        name = params[1]
        self._serviceStudents.add_student(s_id, name)

    def _ui_sort_Gnome(self,params):
        for s in self._serviceStudents.sortStudsById():
            print (s)

    def _ui_showFiltered(self, params):
        for s in self._serviceStudents.filterIds():
            print (s)

    def _ui_print_students(self, params):
        studenti = self._serviceStudents.get_students()
        for student in studenti:
            print(student)

    def _ui_remove_stud(self, params):
        if len(params) != 1:
            raise ValueError("No. params invalid! Must be 1!")
        s_id = int(params[0])
        self._serviceStudents.remove_student(s_id)
        self._serviceGrades.remove_grade_by_student_id(s_id)

    def _ui_update_stud(self, params):
        if len(params) != 2:
            raise ValueError("No. params invalid! Must be 2!")
        s_id = int(params[0])
        new_name = params[1]
        self._serviceStudents.update_student(Student(s_id, new_name))

    def _ui_studs_by_name(self, params):
        if len(params) != 1:
            raise ValueError("No. params invalid! Must be 1")
        name = params[0]
        for s in self._serviceStudents.get_students_by_name(name):
            print(s)

    # @@@@@@@@@@@@@@@@@@@
    def _ui_print_disc(self, params):
        if len(params) != 0:
            raise ValueError("No. params invalid! Must be 0!")
        disciplines = self._serviceDisciplines.get_disc()
        for discipline in disciplines:
            print(discipline)

    def _ui_remove_disc(self, params):
        if len(params) != 1:
            raise ValueError("No. params invalid! Must be 1")
        d_disc = int(params[0])
        self._serviceGrades.remove_grade_by_disc_id(d_disc)
        self._serviceDisciplines.remove_disc(d_disc)

    def _ui_add_disc(self, params):
        if len(params) != 2:
            raise ValueError("No. params invalid! Must be 2!")
        disc_id = int(params[0])
        disc_name = params[1]
        self._serviceDisciplines.add_disc(disc_id, disc_name)

    def _ui_get_disc_by_name(self, params):
        if len(params) != 1:
            raise ValueError("No. params invalid! Must be 1")
        name = params[0]
        for d in self._serviceDisciplines.get_discipline_by_name(name):
            print(d)

    def _ui_update_disc(self, params):
        if len(params) != 2:
            raise ValueError("No. params invalid! Must be 2")
        disc_id = int(params[0])
        disc_name = params[1]
        self._serviceDisciplines.update_discipline(Discipline(disc_id, disc_name))

    # @@@@@@@@@@
    def _ui_give_grade(self, params):
        if len(params) != 3:
            raise ValueError("No. params invalid! Must be 3!")
        id_stud = int(params[0])
        id_disc = int(params[1])
        grade = int(params[2])
        self._serviceGrades.give_grade(id_stud, id_disc, grade)

    def _ui_print_grades(self, params):
        if len(params) != 0:
            raise ValueError("No. params invalid! Must be 0!")
        grades_stud = self._serviceGrades.get_grades()
        for grd in grades_stud:
            print(grd)

    def _ui_print_failing_studs(self, params):
        if len(params) != 0:
            raise ValueError("No. params invalid! Must be 0!")
        failing_list = self._serviceGrades.grades_average()
        for DTO in failing_list:
            # print(str(self._serviceStudents.get_student_by_id(student[0])) + ", Average: " + str(student[1]))
            print(DTO.get_student(), ", Average: ", DTO.get_stud_average())

    def _ui_show_best_students(self, params):
        if len(params) != 0:
            raise ValidError("No. params invalid! Must be 0!")
        best_student = self._serviceGrades.best_students()
        best_student = sorted(best_student, key=lambda DTO: DTO.get_stud_average(), reverse=True)
        for object in best_student:
            # object e de tipul StudentDTO
            print(object.get_student(), ", Average: ", object.get_stud_average())

    def _ui_show_best_discs(self, params):
        best_discipline = self._serviceGrades.best_disciplines()
        best_discipline = sorted(best_discipline, key=lambda DTO: DTO.get_disc_average(), reverse=True)
        for object in best_discipline:
            print(object.get_discipline(), ", Average: ", object.get_disc_average())

    # @@@@@@@@@@@@@@@
    def _undo(self, params):
        try:
            self._serviceUndo.undo()
            print("Undo performed")
        except UndoError as e:
            print(e)

    def _redo(self, params):
        try:
            self._serviceUndo.redo()
            print("Redo performed")
        except UndoError as e:
            print(e)

    def _ui_initial_list(self):
        appsettings = AppSettings()
        if appsettings.Data["repository"] == "inmemory":
            self._serviceStudents.create_init_studs()
            self._serviceDisciplines.create_init_discs()
            self._serviceGrades.create_init_grades()

    def __init__(self, serviceStudents, serviceDisciplines, serviceGrades, serviceUndo):
        self._serviceStudents = serviceStudents
        self._serviceDisciplines = serviceDisciplines
        self._serviceGrades = serviceGrades
        self._serviceUndo = serviceUndo
        self.__commands = {
            "1": self._ui_add_stud,
            "2": self._ui_print_students,
            "3": self._ui_add_disc,
            "4": self._ui_print_disc,
            "5": self._ui_give_grade,
            "6": self._ui_print_grades,
            "7": self._ui_remove_stud,
            "8": self._ui_remove_disc,
            "9": self._ui_update_stud,
            "10": self._ui_update_disc,
            "11": self._ui_studs_by_name,
            "12": self._ui_get_disc_by_name,
            "13": self._ui_print_failing_studs,
            "14": self._ui_show_best_students,
            "15": self._ui_show_best_discs,
            "16": self._ui_sort_Gnome,
            "17": self._ui_showFiltered,
            "u": self._undo,
            "r": self._redo
        }

    @staticmethod
    def menu():
        print("\nOptions: \n"
              "1. Add Student \n"
              "2. Show Students \n"
              "3. Add Discipline \n"
              "4. Show Disciplines \n"
              "5. Add Grade \n"
              "6. Show Grades \n"
              "7. Remove a student \n"
              "8. Remove a discipline \n"
              "9. Change a student's name \n"
              "10. Change a discipline's name \n"
              "11. Search for a student's name \n"
              "12. Search for a discipline \n"
              "13. Show failing students \n"
              "14. Show best students \n"
              "15. Show best disciplines \n"
              "16. Sort Gnome \n"
              "17. Show Filtered Studs (Id is Odd) \n"
              "18. Press u for Undo \n"
              "19. Press r for Redo \n"
              "0. Exit")

    def run(self):
        self._ui_initial_list()
        while True:
            self.menu()
            cmd = input(">>>")
            if cmd == "0":
                return
            cmd = cmd.strip()
            parts = cmd.split()
            nume_cmd = parts[0]
            params = parts[1:]
            if nume_cmd in self.__commands:
                try:
                    self.__commands[nume_cmd](params)
                except ValueError as ve:
                    print("UI error:\n" + str(ve))
                except ValidError as vale:
                    print("Valid error:\n" + str(vale))
                except RepoError as re:
                    print("Repo error:\n" + str(re))
            else:
                print("Invalid Command!")
