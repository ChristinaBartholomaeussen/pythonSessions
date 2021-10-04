# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the lenght of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Ib', 'Per', 'Christina', 'Allan']

# Reversed
sortedl = sorted(l, reverse=True)
#print(sortedl)

# the lenght of the name.
sorted2 = sorted(l, key=len)
# print(sorted2)

# based on the last letter in the name.
def return_last(names):
    return names[-1]

sorted3 = sorted(l, key=return_last)
#print(sorted3)



# with the names where the letter ‘a’ is in the name first

def a_in(s):
    if 'a' in s.lower():
        return True
    return False

lista = sorted(l, key=a_in)

print(lista1)

