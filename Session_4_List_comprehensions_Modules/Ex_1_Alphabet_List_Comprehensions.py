# 1. Create a list of capital letters in the english alphabet
# Min løsning 
alp = [chr(i) for i in range(ord('A'), ord('Z'))] # Printer alfabetet
uni = [i for i in range(ord('A'), ord('Z'))] # Printer unicode


# Claus' løsning
apl1 = [chr(i) for i in range(65, 91)]

# Create a list of capital letter from the english aplhabet, 
# but exclude 4 with the Unicode code point of either 
# 70, 75, 80, 85.

list01 = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]

# Create a list of capital letter from from the 
# english aplhabet, 
# but exclude every second between F & O

list02 = [chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]

# Udskriv lige tal mellem 1 - 10

list03 = [i for i in range(1, 10) if i % 2 == 0]

# Læg mærke til placeringen af if/else, hvis der er else med kontra
# overstående kun med if
list04 = [i if i%2 == 0 else 'Non-even' for i in range(1, 10)]


# Nested for loop 
li = []
for i in range(3):
    for j in range(2):
        li.append((i, j)) # Printer tuples

li01 = [(i, j) for i in range(3) for j in range(2)] # printer tuples med comprehension

