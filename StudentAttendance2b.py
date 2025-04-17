"""Write a program to define a funtion that accepts roll numbers and returns whether the student is present or absent
NAME:KASHISH GUPTA 231P081/09"""
def StudentAttendance(roll,AttendanceList):
    if roll in AttendanceList:
        return "Present"
    else:
        return "Absent"
AttendanceList=[9,3,40,41,42,36,23,11,5]
roll=int(input("Enter the roll number of student to be checked if present or not:"))
Attendance=StudentAttendance(roll,AttendanceList)
print(f"The roll number {roll} is {Attendance}.")
print("~A python program by Kashish Gupta 09/231P081") 


    
