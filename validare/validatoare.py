from erori.exceptii import ValidError
class ValidatorStudent(object):
      
    def validate_student(self, student):
        erori = ""
        if student.get_s_id() < 0:
            erori += "id invalid!\n"
        if student.get_name() == "":
            erori+= "name invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)


class ValidatorDiscipline(object):
    def validate_disc(self, discipline):
        erori = ""
        if discipline.get_id_disc() < 0:
            erori+= "id invalid!\n"
        if discipline.get_disc_name() == "":
            erori+= "name invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)

class ValidatorGrade(object):
    def validate_grade(self, grade):
        erori = ""
        if grade.get_id_stud() < 0:
            erori+= "id student invalid!\n"
        if grade.get_id_disc() <0:
            erori += "id discipline invalid!\n"
        if grade.get_grade() < 1 or grade.get_grade() >10:
            erori+= "grade invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)
        


