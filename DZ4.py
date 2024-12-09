class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    list_lecturer = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_Lecturer_dict = {}          # оценки студентов за лекции лекторов
        self.list_lecturer.append(self)         # наполняем список лекторов

    def average_grade_Lecturer(self):
        grade_list_Lecturer = []
        for num in self.grades_Lecturer_dict.values():
            grade_list_Lecturer.extend(num)
        average_grade = sum(grade_list_Lecturer)/len(grade_list_Lecturer)
        return average_grade

    def __lt__(self, lecturer):
        return self.average_grade < lecturer.average_grade

    def __gt__(self, lecturer):
        return self.average_grade > lecturer.average_grade

    def __eq__(self, lecturer):
        return self.average_grade == lecturer.average_grade

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self.average_grade_Lecturer()}')
        return result

class Student:
    list_student = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_Student_dict = {}           # оценки за ДЗ
        self.list_student.append(self)          # наполняем список студентов

    def final_courses(self, course):
        self.finished_courses.append(course)

    def add_grade_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades_Lecturer_dict:
                lecturer.grades_Lecturer_dict[course] += [grade]
            else:
                lecturer.grades_Lecturer_dict[course] = [grade]
        else:
            return print("Ошибка")

    def average_grade_Student(self):
        grade_list_Student = []
        for num in self.grades_Student_dict.values():
            grade_list_Student.extend(num)
        self.average_grade = sum(grade_list_Student)/len(grade_list_Student)
        return self.average_grade

    def __lt__(self, student):
        return self.average_grade < student.average_grade

    def __gt__(self, student):
        return self.average_grade > student.average_grade

    def __eq__(self, student):
        return self.average_grade == student.average_grade

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.average_grade_Student()}\n'
                  f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                  f'Завершенные курсы: {self.finished_courses}')
        return result

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

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}')
        return result

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
student_1.add_grade_Lecturer(lecturer_1, "C++", 9)
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
reviewer_1.add_grade_Student(student_1, "C++", 10)
reviewer_2.add_grade_Student(student_2, "Python", 10)
reviewer_1.add_grade_Student(student_3, "C++", 7)
reviewer_2.add_grade_Student(student_4, "Python", 6)
reviewer_1.add_grade_Student(student_5, "C++", 10)

# вычисление средней оценки у всех студентов за указанный курс
def average_grade_student_all(self, course):
    grade_list = []
    for num in self:
        for a, b in num.grades_Student_dict.items():
            if a == course:
                grade_list.extend(b)
    if grade_list:
        average_grade_student = sum(grade_list) / len(grade_list)
        answer = f"Средняя оценка по курсу {course} у студентов {average_grade_student}"
    else: answer = f"Оценок по курсу {course} у студентов нет либо название курса указано некорректно"
    return answer

# проверка
print(average_grade_student_all(Student.list_student,"C++"))

# вычисление средней оценки лектора за указанный курс
def average_grade_lecturer_all(self, course):
    grade_list = []
    for num in self:
        for a, b in num.grades_Lecturer_dict.items():
            if a == course:
                grade_list.extend(b)
    if grade_list:
        average_grade_lecturer = sum(grade_list) / len(grade_list)
        answer = f"Средняя оценка по курсу {course} у лекторов {average_grade_lecturer}"
    else: answer = f"Оценок по курсу {course} у лекторов нет либо название курса указано некорректно"
    return answer

# проверка
print(average_grade_lecturer_all(Lecturer.list_lecturer,"C++"))