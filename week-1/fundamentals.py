# 1.Dictionaries.
activity_names = {0: 'Sleep', 1: 'Work', 2: 'Exercise'}
print(activity_names[1])

# dictionaries are mutable.
# .get(key, default) is the safe version of a lookup, instead of crushing on a missing key,it returns the specified default.

print(activity_names.get(5, 'Unknown'))

# the block of code below tracks the roder the dictionary entries appear in
counts = {}
# declaration of an empty dictionary
counts['Work'] = counts.get('Work', 0) + 1
counts['Work'] = counts.get('Work', 0) +1
counts['Sleep'] = counts.get('Sleep', 0) + 1
print(counts)