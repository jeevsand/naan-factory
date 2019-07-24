##FUnction principles:
 #they only do one job
 #should be unitary
 #should do the above so they are testable
 #do not print inside functions... you return
 #need to be called to run

#Unit tests : are tests that test 1 function

#TDD: Test driven development
#write your tests according to specs
#Then follow the errors and iterate until test pass

def say_hello():
    return 'hello'

print (say_hello())

def say_hello_personal(name_arg):
    return 'hello ' + name_arg.capitalize()

def full_name_hello(arg1,arg2):
    return 'hello '+arg1.capitalise()+ ' '+arg2.capitalise()

print (say_hello_personal('Isabella'))

##Testing
#has two main section: Setup and Evaluatation
#You give it controlled input and test for expected outcomes

#Test 1: say_hello functions
#Spec: when call should return string 'hello'
setup_results = say_hello()
print(setup_results == 'hello')

#Test 2: testing say hello personalize functions
say_hello_personal('Isabella')=='Hello Isabella'


#Test 3: testing function full_name_hello
print("calling function full_name_hello() with Isabella Jones, expect 'hello Isabella Jones' to be printed")
print(full_name_hello('isabella', 'jones')== 'hello Isabella Jones')