 
class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())
 
class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class

def print_all_students(students): 
    for student in students:
        print("{}, {}, {}, {}".format(student.full_name(), student.school_class, student.mom, student.dad ))

if __name__ == '__main__':  
    st_1 = Student('Андрей', 'Александрович', 'Петров', 'Юлия Петрова', 'Алексанр Петров', '9а')
    st_2 = Student('Сергей', 'Евгенич', 'Бодров', 'Наталья Бодрова', ' Евгений Бодров ', '7б')
    st_3 = Student('Олег', 'Олегович', 'Бобров', 'Анастасия Боброва', 'Олег Бобров', '9а')
    students = [st_1, st_2, st_3]
    print_all_students(students)