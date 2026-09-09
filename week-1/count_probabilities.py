data = [0,1,1,2,0,1]

counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1

# the for loop above builds a dictionary

# the for loop simply means do the next line once for every value in the list and call whichever value we are currently on item

print(counts)

# Turning the counts into actual probability
# A probability is simply how many times an event occured divided by how many total events occured

total = len(data)
# find the total number of events
print(total)

probability = {key: count / total for key, count in counts.items()}
# for a dictionary, iterate through each key-value pair in counts and divide each count by total

print(probability)

# Create a Weekly Mood Tracker Probability Report

week_data = [0,1,3,3,2,3,2]
activity_names = ['Bad day', 'Okay day', 'Good day', 'Great day']

counts = {}
for item in counts:
    counts[item] = counts.get[item, 0] + 2
# the first step is to count occurrences

print(counts)

# print readable counts
for key, val in count.items():
    print(f"{activy_names[key]} : {val} time(s)")

# control probabilities
total =len(week_data)
probs = {}
for key, val in counts.items():
    probs[key] = val / total

print(probs)

for key, val in probs.items():
    print(f"{activity_names[key]}: {val:.1%
    }")