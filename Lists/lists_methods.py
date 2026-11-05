# list.append modifies a list by adding an item to the end.abs

x = 34

x.append(30)

# lists.pop() - removes the last item in a list.

# searching lists, do so using list.index(itemName)
# the method above can return an error if the said item does not yet exist and to fix this we use the 'in' operator.

# len(list_name)
# used to find the total length of a list


# okay accessing items in a nested list, you do this by chaining square brackets, so the first pair will pick a sub-list and the next will pick an element inside it
# say I had a list and I wanted to access the last nested list, its 4th item, this is how it would look like:

listName[-1][3]

# slicing works at each level independently
list_name[:2]
# this will return the first 2 rows in the nested list
list_name[0][1:]
# this will return row 0, column 1 onward

# to loop through nested lists, use the code block below:

for row in list_name:
    # each row is a list
    for value in row:
        # each value here is an int
        print(value)

# when position is needeD:

for r in range(len(list_name)):
    for c in range(len(list_name[r])):
        print(r, c, list_name[r][c])


