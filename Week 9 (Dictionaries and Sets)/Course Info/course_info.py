################################################################################
# Author: Karteikay Dhuper
# Date: April 11th 2021
# Description This program displays information about a user specified course
# form a nested dictionary
################################################################################

def get_course_data():
    # initilization of nested dictionary
    courseDictionary = {'CS101':{'instructor': 'Haynes','room': '3004', 'time': '8:00 a.m.'},
                        'CS102':{'instructor': 'Alvarado', 'room': '4501', 'time': '9:00 a.m.'},
                        'CS103':{'instructor': 'Rich', 'room': '6755', 'time': '10:00 a.m.'},
                        'NT110':{'instructor': 'Burke', 'room': '1244', 'time': '11:00 a.m.'},
                        'CM241':{'instructor': 'Lee', 'room': '1411', 'time': '1:00 p.m.'}, }

    return courseDictionary

def main():

    course = input("Enter a course number: ")
    if course in get_course_data(): # checks if user inputted course is in the dictionary
        print(f"The details for course {course} are:")
        courseInfo = get_course_data().get(course) # courseinfo returns value in nested dictionary for that specific course name
        for key,value in sorted(courseInfo.items()):
            print(f'{key.title().rjust(12)}:' , value) # prints key and value information of everything in that course
    else:
        print(f"{course} is an invalid course number.")

if __name__ == '__main__':
    main()
