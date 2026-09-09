# ERRORS

-The following errors were encountered when building:

1.When attempting to print a value larger than the available items defined in the dictionary:

        ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)
    Cell In[2], line 1
    ----> 1 print(activity_names[5])
    
    KeyError: 5


      Traceback (most recent call last)
    Cell In[5], line 11
          7 print(counts)
          8 
          9 activity_names = ['Bad day', 'Okay day', 'Good day', 'Great day']
         10 
    ---> 11 output = {key: list(set(val1).intersection(test_activity_names.keys())) for key, val1 in counts.items()}
         12 
         13 for key, val in output.items():
         14     output[key] = [item for k in val for item in activity_names[k]]
    
    TypeError: 'int' object is not iterable

2.The above error was obtained when the block of code below was run:

    counts = {}
    for item in data:
    <!-- first bug was calling data and not week_data  -->
        counts[item] = counts.get(item, 0) + 1
    
    print(counts)
    
    activity_names = ['Bad day', 'Okay day', 'Good day', 'Great day']
    
    output = {key: list(set(val1).intersection(test_activity_names.keys())) for key, val1 in counts.items()}
    
    for key, val in output.items():
        output[key] = [item for k in val for item in activity_names[k]]
    
    print(output)    