class Person:
    #initializer a name and address for the person, both variables are private
    def __init__(self, name = "N/A", address = "N/A"):
        self.__name = name
        self.__address = address
    
    def setAddress(self, address):
        self.__address = address

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def __str__(self):
        print(f"{self.getName}: ({self.getAddress})")

class Student(Person):
    def __init__(self, numCourses = 0, Courses = {}, name = "N/A", address = "N/A"):
        super().__init__(self, name, address)
        self.__number_of_courses = numCourses
        self.__Course_andGrades = Courses

    def setNumcourses(self, numCourses):
        self.__number_of_courses = numCourses
        
    def addCoursewithGrade(self):
        for i in self.__number_of_courses:
            course = input("Input a course that the student has: ")
            grades = input("Input the grade of that corresponding course: ")
            self.__Course_andGrades[course] = grades
        return self.__Course_andGrades

    def getAverageGrade(self):
        totalGrade = sum(self.__Course_andGrades.values())
        averageGrade = totalGrade / self.__number_of_courses
        return averageGrade

    def getCoursewithGrade(self):
        return self.__Course_andGrades

    def __studentStr__(self):
        print(f"Student: {self.__name}({self.__address})")

    def __gradeStr__(self):
        for key, value in self.__Course_andGrades:
            print(f"{key} : {value}")

    class Teacher(Person):
        def __init__(self, numCourses = 0, TeachingCourses = [], name = "N/A", address = "N/A"):
            super().__init__(self, name, address)
            self.__number_of_courses = numCourses
            self.__TeachingCourses = TeachingCourses

        def setNumcourses(self, numCourses):
            self.__number_of_courses = numCourses

        def addCourse(self, course):
            for x in self.__TeachingCourses:
                if course == self.__TeachingCourses[x]:
                    return False
                    break

        def removeCourse(self, course):
            for y in self.__TeachingCourses:
                if course != self.__TeachingCourses[y]:
                    return False
                    break

        def __teacherStr__(self):
            print(f"Teacher: {self.__name}({self.__address})")


        