# Python-For-Everybody </br>
Goals (high level intended outcomes; for software, a Product Backlog) </br>
-Develop a basic understanding of Python and what Python is. </br>
-Learn how to program. </br>
-Understand fundamental programming concepts such as data structures.</br>
-Describe the basics of the Structured Query Language. </br>
-Create your own applications for data retrieval and processing. </br>
Boundaries / Scope (where the functions and responsibilities of the solution start and end / what it should do and what is left to other systems to do) </br>
-Complete Course 1 Programming for Everybody (Getting Started with Python) </br>
-Complete Course 2 Python Data Structures </br>
-Only using python and not other langues. </br>
-Task is completed when course is finished. </br>
Success criteria (set of conditions to be satisfied at completion; must be measurable and verifiable, like a test) </br>
-My own application for data retrieval and processing. </br>
-Weekly work log with screenshots and summaries to demonstrate activity to keep my work updated and ontime. </br>
-Utilize core programming tools such as functions and loops. </br> 
-Have a completed project by the end of the course that is ON TIME. </br>
Constraints (externally imposed limitations on system requirements, design, or implementation or on the process used to develop or modify a system) </br>
-Not paying for the course so I won't be able to obtain the certificate. </br>
-I don't know a single thing about programming so I'm learning everything from the beginning. </br>
-I can only work on project with wifi available. </br>
Assumptions (things that are accepted as true or as certain to happen, without proof) </br>
-The courses will be available for the duration of the semester. </br>
-I have a laptop to use python. </br>
-I will learn python. </br>
-I can skip the Installing Python unit because it's installed. </br>
-Might need additional time to complete sections because no previous knowledge. </br>
Stakeholders (individuals or organizations having a right, share, claim, or interest in a system or in its possession of characteristics that meet their needs and expectations) </br>
-Professor - for grade </br>
-Parents - just wanting to make them proud. </br>
-Florida- I'm on a full scholarship so I have to pass my classes. </br>
-Myself- I got this, even though I don't' know anything about computers, YET. </br>
-Perspective Employers - the basic understanding of python may be beneficial when running my family business Spalding Carpet Cleaners. </br>
Timelines (for software, a breakdown of high level goals like from the Product Backlog into time-bound smaller, more detailed tasks, like in Sprint Backlogs) </br>
-Chapter One - Why we Program? (3 hours) </br>
-Chapter Two: Variables and Expressions (3 hours) </br>
-Chapter Three: Conditional Code (3 hours) </br>
#-Chapter Five: Loops and Iteration (3 hours) </br>
Loops have iteration variables that change each time through a loop.
n=5    Have to initiate variable.
While n>0:    Have to set condition
	print(n)   prints variable every time it goes through loop
	n=n-1     iteration variable, if not it wouldn’t know what to do after entering 5
print(‘blastoff!’)   only prints once loop is completed, not in indentation 
print(n)        will print final variable of end after loop is completed since not in indentation
LOOP THAT WILL NOT WORK
n=5
While n>0:
	Print(‘Lather’)
	Print(‘Rinse”)
Print(‘Dry off’)
NO ITERATION VARIABLE
#Prof said breaks was bad practice so I didn’t include notes on breaks and continues.


Definite loop
for i in (5,4,3,2,1): green is iteration variable that iterates through the sequence
	print(i)   the purple is the (body) of code that is executed once for each value in the sequence
print(‘Blastoff!’) 
5
4
3
2
1
Blastoff!
friends=(‘Joseph’,’Glenn’,’Sally’)
for friend in friends:
	print(‘Happy New Year:’,friend)
print(‘Done!’)
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
print(‘Before’)
for thing in(9,41,12,3,74,15)
	print(thing)
print(‘After’)
before
9
41
12
3
74
15
After
Notice how Before and After are not in loop
Average in Loop
Count=0
Sum=0
Print(‘Before’,count,sum)
For value in (9,41,12,3,74,15):
	Count=count+1
	Sum=sum+value
	Print(count,suum,value)
Print(‘After’,count,sum,sum/count)
Before 00
9 9
50 41
62 12
65 3
139 74
154 15
After  154 25

#-Chapter Four: Functions (2 hours) </br>
-Functions start with the keyword def, followed by the name and then end with :
-Def defines the function, make sure to indent bondy of function.
-Functions in a program don’t actually run unless they’re “Called” by name
-Function examples: print() float()input()type()int()string()
Input() always gives back a string
Argument: Value we pass into function as its input when we call the function
-used to direct function to do different types of work
-Using global variables is BAD practice, instead use parameters
-Parameter: a variable which we use in the function def, a handle that allows the function to access variables outside the function.
Return values return a value to be used as the value of a function call in the calling expression.
Def greet()
	Return “hello”
Print(greet(),”glenn”)
print(greet(),”Sally”)

Hello Glenn
Hello Sally

Fruitful functions produce a result/return value.
-We can use more than one parameter, we got to add more arguments, match number and order of arguments and parameters.

-Chapter Seven: Files (3 hours) </br>
-Chapter Eight: Lists (3 hours)</br>
-Chapter Six: Strings (3 hours)</br>
-Chapter Nine: Dictionaries (3 hours)</br>
-Chapter Ten: Tuples (2 hours)</br>
-Graduation and work on independent program (2 hours) </br>
-Complete independent program (2 hours) </br>
# So far, I've used python for everybody as a review to reinforce material the professor has taught us in class. It jogs my memory over the weekend while I'm working on my exercises and integration project. It's quite simple material, so it better enables me to grasp the concepts I have a hard time understanding, like loops. 
