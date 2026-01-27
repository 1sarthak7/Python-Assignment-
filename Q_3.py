courses = ("Math", ("Algebra", "Geometry"), "Science")

print("Main subjects:")
print(courses[0])   
print(courses[2])   

print("Subtopics under Math:")
print(courses[1])   

more_courses = ("Computer Science", "Physics")
all_courses = courses + more_courses

print("After adding more courses:")
print(all_courses)