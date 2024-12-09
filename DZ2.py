class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_Lecturer_dict = {}           # оценки студентов за лекции лекторов

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_Student_dict = {}            # оценки за ДЗ

    def add_grade_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades_Lecturer_dict:
                lecturer.grades_Lecturer_dict[course] += [grade]
            else:
                lecturer.grades_Lecturer_dict[course] = [grade]
        else:
            return print("Ошибка")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grade_Student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_Student_dict:
                student.grades_Student_dict[course] += [grade]
            else:
                student.grades_Student_dict[course] = [grade]
        else:
            return print('Ошибка')

# исходные данные
# введем данные студентов
student_1 = Student("Иван", "Громов", "мужчина")
student_2 = Student("Ольга", "Васина", "женщина")
student_3 = Student("Николай", "Иванов", "мужчина")
student_4 = Student("Светлана", "Бусина", "женщина")
student_5 = Student("Владимир", "Мочнев", "мужчина")

# обозначим какой курс проходит каждый студент
student_1.courses_in_progress.append("C++")
student_2.courses_in_progress.append("Python")
student_3.courses_in_progress.append("C++")
student_4.courses_in_progress.append("Python")
student_5.courses_in_progress.append("C++")

# введем данные лекторов
lecturer_1 = Lecturer("Игорь", "Репин")
lecturer_2 = Lecturer("Павел", "Котин")

# обозначим какой курс читают лекторы
lecturer_1.courses_attached.append("C++")
lecturer_2.courses_attached.append("Python")

# выставим оценки лекторам от студентов
student_1.add_grade_Lecturer(lecturer_1, "C++", 8)
student_2.add_grade_Lecturer(lecturer_2, "Python", 9)
student_3.add_grade_Lecturer(lecturer_1, "C++", 10)
student_4.add_grade_Lecturer(lecturer_2, "Python", 7)
student_5.add_grade_Lecturer(lecturer_1, "C++", 6)

# введем данные рецензентов
reviewer_1 = Reviewer("Марина", "Павлова")
reviewer_2 = Reviewer("Анастасия", "Чалова")

# обозначим какие курсы проверяют рецензенты
reviewer_1.courses_attached.append("C++")
reviewer_2.courses_attached.append("Python")

# выставим оценки студентам от рецензентов
reviewer_1.add_grade_Student(student_1, "C++", 8)
reviewer_2.add_grade_Student(student_2, "Python", 10)
reviewer_1.add_grade_Student(student_3, "C++", 7)
reviewer_2.add_grade_Student(student_4, "Python", 6)
reviewer_1.add_grade_Student(student_5, "C++", 10)

# проверка
print(student_4.name, student_4.surname, student_4.courses_in_progress)
print(lecturer_1.name, lecturer_1.surname, lecturer_1.courses_attached, lecturer_1.grades_Lecturer_dict)
print(reviewer_1.name, reviewer_1.surname, reviewer_1.courses_attached, student_1.grades_Student_dict)
