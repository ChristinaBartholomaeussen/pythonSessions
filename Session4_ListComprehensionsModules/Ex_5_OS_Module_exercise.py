# os_exercise.py
# Do the following task using the os module

# 1. create a folder and name the folder 'os_exercises.'                                                  
# 2. In that folder create a file. Name the file 'exercise.py'                                                                            
# 3. get input from the console and write it to the file.                                                 
# 4. repeat step 2 and 3 (name the file something else).                                                  
# 5. read the content of the files and and print it to the console.

import os

os.mkdir('os_exercises')
os.chdir('os_exercises')
myfile = open('exercise.py','w')
input1 = input()
myfile.write(input1)
myfile.close()

f = open('exercise.py', 'r')
print(f.readlines())

