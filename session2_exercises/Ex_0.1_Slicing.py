#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
words = ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
print(words[0:5])

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
print(words[0:2])

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
print(words[-2:])

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
print(words[-2:-1])

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#0 , 2, 4
print(words[::2])

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
words.reverse()
print(words)


tuplewords = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
print(tuplewords[1: -1])

#'Hello World Huston we are here' -> 'World Huston we'
stringwords = 'Hello World Huston we are here'
liste = list(stringwords.split(" "))
print(liste[1:4])