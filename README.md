# IntroToProg-Python-Mod7

**Andrei Arevalo**  
2/17/2021  
Foundations in Programming, Python  
Assignment07  

# Pickling and Exceptions in Python

## Introduction
In this assignment we are tasked with creating demonstration examples of error handling within Python and pickling data. The format of this assignment is different than previous assignments in that this week we are asked to create the examples and demonstrations ourselves. This is much more open ended than previous weeks and it was on us to decide what examples to use. This was a good method of learning as it requires us to go and research on our own about different ways to create the demonstrations. In the introduction video, the professor opens up that it’s on us to determine the number of examples and demonstrations. I chose to use 3 examples for this HW assignment.  

## Creating the Script
### 1.
The purpose of this program is to create examples of how Pickling and Exceptions work in Python. The format of this assignment is different than previous assignments in that this week we are asked to create the examples and demonstrations ourselves. This is much more open ended than previous weeks and it’s on us to decide what examples to use.(Figure 1) ![figure 1](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure01.png)  
### 2.	
At the top of the script is the title block, which shows information about the script and keeps track of revision history in case the file needs to be revised in the future. The author and date are also included in this title block. In addition below the title block is a summary of the assignment with the task outlined. The goal of this assignment was to create a program that demonstrates the use of pickling and structured error handling. (Figure 2) ![figure 2](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure02.png)  
### 3. 
At the beginning of the script, I introduce the definition of an exception in Python. (http://docs.python.org/3/tutorial/errors.html) An exception is an error detected during the execution of a sequence of code. There are different types of exceptions, for example diving by zero, naming something incorrectly, or declaring a type incorrectly. (Figure 3) ![figure 3](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure03.png)  
### 4.
The next part of the script introduces the first example in the main script which defines a function that attempts to divide 1 by 0. This is mathematically undefined, which means the program should typically stop and read an error that the division cannot happen. Instead, with the use of the “try” and “except”, the code walks through the function and tries it, and if it fails with a specific error a printer message occurs. This is important because the error message must match what is listed in the “except” part of the code. Another important note here is that because we are using “try”, the code doesn’t immediately end when the error is created.  (Figure 4) ![figure 4](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure04.png)  
### 5. 
In the demonstration code we added a note to print the type of error that occurs in the code. As expected, because the equation is mathematically undefined, the type of error that occurs is a division by zero error. (Figure 5) ![figure 5](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure05.png)  
### 6. 
In the next example, we ask the user to input a number. If the input is not a number, an error message should be displayed telling the user that the number is not valid. Similar to the previous example and demonstration, because we are using the “try” feature, the code doesn’t stop if an error occurs. Instead, we use the “except” to display the “Oops...” text when the “Value Error” is created. If the input is a number, the following print line is displayed to the user showing them what number they entered. This is important because the code jumps from line 36 to line 40 if the error message is displayed; otherwise it goes sequentially from line 36 to 37.  (Figure 6) ![figure 6](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure06.png)  
### 7. 
The output of the above code is shown below. When a number is entered, the following message is displayed. (Figure 7) ![figure 7](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure07.png)  
### 8.
The output of the above code in figure 6 is shown below. When something other than a number is entered, the following message is displayed.(Figure 8)   ![figure 8](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure08.png)  
### 9.
The next section of code deals with pickling in Python. (http://www.tutorialspoint.com/python-pickling). The pickling module within Python us used for serializing and de-serializing python object structures. This is useful in scenarios where you want to transfer data from one system to another and then store it in a file or database. (Figure 9) ![figure 9](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure09.png)  
### 10.
The following example goes through a list of items needed to create a snowman, and then pickles it into a binary list which is stored in a txt file, and then loads it back into a list for the user to read. The import elements of the pickling module are the “dump” element and “load” element. In the “dump, the list is moved into a binary equivalent list and stored in a text file. This is then loaded back into the program using the “load” element. In general these are useful for transferring data between systems. (Figure 10) ![figure 10](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure10.png)  
### 11.
Below is the output of the printed messages when using the pickling feature within Python.  (Figure 11) ![figure 11](https://github.com/Arevalohm123/IntroToProg-Python-Mod7/blob/main/Figure11.png)  
## Summary
In this assignment we are tasked with creating demonstration examples of error handling within Python and pickling data. The format of this assignment is different than previous assignments in that this week we are asked to create the examples and demonstrations ourselves. This is much more open ended than previous weeks and it was on us to decide what examples to use. This was a good method of learning as it required us to go and research on our own about different ways to create the demonstrations. If I were to do this assignment again I would have included examples from the textbook for the class; I was unable to do so for this homework assignment because we were to look at the web for examples. 
