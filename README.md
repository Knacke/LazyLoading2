This is a program that implements lazy loading of variables. 
It takes a text file as input. See "script.txt" for an example of syntax. 




How to run: 

To run the program you need python3 installed.

To run the program run the command: 
python3 newcalculator.py script.txt (linux)
python newcalculator.py script.txt (windows)



About the program:

To handle lazy loading I've created a new variable class. Mainly because 
of how Python handels pass by reference. Note that the class overloads some operators (+-*)
This is to get the same syntax as the input.


I assume inputed numbers are given as integers and that commands are entered in a textfile.


