# Create a file and call it lyrics.txt (it does not need to have any content)
# Create a new file and call it songs.docx and in this file write 3 lines of text to it.
# open and read the content and write it to your terminal window. 
#* you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

#file1 = open("lyrics.txt", "x")
#file2 = open("songs.docx", "w")
#file2.write("Welcome. \n This is my first file writing project. \n Thank you")

# read()
f = open("songs.docx", "r")
print(f.read())

f = open("songs.docx", "r")
print(f.readlines())

f = open("songs.docx", "r")
for line in f:
    print(f.readline())

