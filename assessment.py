"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Three main design advantages are you can store data data lives close to its functionality (Encapsulation), structured don't need to know info a method uses internally (Abstraction), and 
   easy to make different, interchangeable types with Polymorphism. 

   You can use the class as a blueprint and make many instances based on that class which stores data.
   It is structured in a hierchy you have parent classes and children classes. Children classes can inherit from 
   the parent class and use their methods or attributes.
   It has it's own smarts when you create an instance and then call an attribute 
   it is smart enough to search for the attribute starting with the instance and if it not there it will 
   go up the heirchy and search for the attribute on a class level.
   If it the attribute exists in the class level it is smart enough to bring it back to use for that instance. 


2. What is a class?
    Type of thing, like String (str) or File (file)
    It provides a template to use when making an instance. 

3. What is an instance attribute?
   It is an attribute on the object not the class. 

4. What is a method?
   Method is a function in a class. 

5. What is an instance in object orientation?
    An individual occuence of a class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Class attribute is an attribute on the class. 
   Instance attribute is an attribute on the instance or object. 

   You would use a class attribute as a blue print if you want to apply on the instances made in the future. Class attribute is attribute not specific but general and shared. 
   You would use an instance attribute if you wanted to override the class attribute set or because it is only specific to the object and not to the class.  


   example is 
   Class Melons:
        #attributes are shared the same in the class of Melons#
        self.weight = 0.0
        self.color = None 

    When you create an instance of this class melons you can override the class attribute of self.weight =0.0 to self.weight of 5.
"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address 



class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question 
        self.correct_answer = correct_answer


    def ask_and_evaluate(self):
      answer = raw_input(self.question)

      if self.correct_answer == answer:
        return True
      else:
        return False


class Exam(object):

    def __init__(self, name):
        self.questions = []
        self.name = name


    def add_question(self, question, correct_answer):
        q = Question(question, correct_answer)
        self.questions.append(q)
        # print question
        # q = {'question':question, 'correct_answer': correct_answer}
        # print q
        # questions.append(q)
        # print questions 
        # q[word_question] = answer 
        # questions = questions.add(question, correct_answer)

    def administer(self):
      score = 0
      for question in self.questions:
        results = question.ask_and_evaluate()
        if results == True:
          score = score + 1


      print score
      percentage_score = float(score)/ len(self.questions)
      return percentage_score

    


def take_test(exam, student):
  # score = .adminster()
  # print score 
  score = exam.administer()
  student.score = score 
  print student.score



def example():
  s = Student("Gracie", "Durham", "631")
  e = Exam("Midterm")
  e.add_question("Whats your name?", "Grace")
  e.add_question("Whats your favorite food?", "Crab Legs")
  take_test(e, s)


example()


# class Quiz(Exam):

#   # def __init__(self):
#   #   super(Quiz, self) __init__(self, "Quiz")
#   exam.administer()
#   score = 0
#     for question in self.questions:
#       results = question.ask_and_evaluate()
#       if results == True:
#         score = score + 1


#   print score
#   percentage_score = float(score)/ len(self.questions)
#   if percentage_score > .50:
#     return True 
      
# I got a little stuck on this last one 
#I know this is a child sub class and I need to inherit from the parent class Exam 
#I got stuck on the execution of it 
#I started with the super method and it did not work 
#So I moved on to passing the parent class Exam and then trying to access the method administer 
#then changing the code to state if score > .50 then they passed and true else they did not pass 






































