class Student(object): 
    def __init__(self, s_id, name):
        self._s_id = s_id
        self._name = name

    def get_s_id(self):
        return self._s_id

    def get_name(self):
        return self._name

    def set_s_id(self, value):
        self._s_id = value

    def set_name(self, value):
        self._name = value    

    def __eq__(self, other):
        return self._s_id == other._s_id
     
    def __str__(self):
        return "ID: " + str(self._s_id) + ", Name: " + self._name
class StudentDTO(object):
    def __init__(self, student, stud_average):
        self._student= student
        self._stud_average = stud_average

    def get_student(self):
        return self._student

    def get_stud_average(self):
        return self._stud_average
    

class Discipline(object):
    def __init__(self, id_disc, disc_name):
        self._id_disc = id_disc
        self._disc_name = disc_name

    def get_id_disc(self):
        return self._id_disc


    def get_disc_name(self):
        return self._disc_name


    def set_id_disc(self, value):
        self._id_disc = value


    def set_disc_name(self, value):
        self._disc_name = value

    #def set(self, other):
    #   self.set_disc_name(other._disc_name)

    def __eq__(self, other):
        return self._id_disc == other._id_disc 
    def __str__(self):
        return "ID Discipline: " + str(self._id_disc) + ", Discipline: " + self._disc_name
    
class DisciplineDTO(object):
    def __init__(self, discipline , disc_average):
        self._discipline= discipline
        self._disc_average = disc_average

    def get_discipline(self):
        return self._discipline


    def get_disc_average(self):
        return self._disc_average

class Grade(object):
    def __init__(self,  id_stud,id_disc, grade):
        self._id_stud = id_stud
        self._id_disc = id_disc
        self._grade = grade

    def get_id_stud(self):
        return self._id_stud


    def get_id_disc(self):
        return self._id_disc


    def get_grade(self):
        return self._grade


    def set_id_stud(self, value):
        self._id_stud = value


    def set_id_disc(self, value):
        self._id_disc = value


    def set_grade(self, value):
        self._grade = value

    #def set(self, other):
    #    self.set_grade(other._disc_name)
    
    def __eq__(self, other):
        return self._id_stud == other._id_stud and self._id_disc == other._id_disc
        
    def __str__(self):
        return "ID Student: " + str(self._id_stud) + ", ID Discipline: " +  str(self._id_disc) + ", Grade: " + str(self._grade)

