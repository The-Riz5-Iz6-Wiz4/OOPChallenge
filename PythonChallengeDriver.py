import PythonChallengeClass

#creating a student
newStudent = PythonChallengeClass.Student()

def infoGather():
    newStudent.setName(input("Input student name: "))
    newStudent.setAddress(input("Input student address:"))
    newStudent.setNumcourses(int(input("Input number of courses student has: ")))
    PythonChallengeClass.addCourseWithGrade

def main():
    infoGather()
    PythonChallengeClass.__studentStr__()
    PythonChallengeClass.__gradeStr__()

