# are the same as lists only that these use square brackets instead of parentheses.
# are immutable

# tuple assignment can be used to rearrange tje order in a list
# swapping literally, when you want to move the last item to the first and vice versa without affecting the other items, the following is done:

list_name[0],list_name[-1]=list_name[-1],list_name[0]

# so what happens here is that python evaluates the right side first then assigns left-to-right so a temp variable is not needed.

# to guard the empty case when the input is not guaranteed,
if len(list_name) >=2:
    # the write out the swap code here
    list_name[0],list_name[-1]=list_name[-1],list_name[0]


# FOR ROTATION, where the entire order is reversed:
list_name=list_name[1:] + list_name[:1]
# the first item will go to the end in this case
list_name=list_name[-1] + list_name[:-1]
# for this one, the last item will go to the front

# this OG list will however remained unchained for an ampty list