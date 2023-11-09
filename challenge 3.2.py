#3.2 Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA(cumulative grade point average) in descending order.Each student object has the following attributes: name (string),roll_number(string),and cgpa (float). Test the function witg different input lists of studentsc
class Student:
  def _init_(self,name,
roll_number,cgpa):

    self.name = name

    self.roll_number =
roll_number 

     self.cgpa = cgpa



def
sort_students(student_list):

  sorted_students =
sorted(student_list,
key=lambda student:
student.cgpa,reverse=True)     

  return sorted_students



# Example usage:

student1 = Student("Alice",
"S123",3.7)                  

student2 = student("Bob",
"S124",3.9)

student3 = student("Charlie",
"S125",3.5) 

student4 = student("David",
"S126",3.8)                  



student =[student1, student 2, student3, student4]


sorted_students =
sorted_students(student)



# print the sorted list
of sorted_students by CGPA inpu
descending order

for student in
sorted_students:

  print(f"Name:
{student.name}, Roll Number: 
{student.roll_number}, CGPA:
{student.cgpa}")



                   




  
    
    