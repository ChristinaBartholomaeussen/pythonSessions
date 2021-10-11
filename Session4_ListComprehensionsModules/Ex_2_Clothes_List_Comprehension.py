# From 2 lists, using a list comprehension, 
# create a list containing:

# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

mylist = [(c, s) for c in colors for s in sizes]

# Output: [('Black', 's'), ('Black', 'm'), ('Black', 'l'), ('Black', 'xl'), ('White', 's'), ('White', 'm'), ('White', 'l'), ('White', 'xl')]

# If the tuple pair is in the following list, it should not be added to the comprehension generated list.

sold_out = [('Black', 'm'), ('White', 's')]

new_list = [(c, s) for c in colors for s in sizes if (c, s) not in sold_out]

print(new_list)