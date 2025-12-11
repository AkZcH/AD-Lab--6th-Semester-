#Central Tendency: Mean, Median, Mode

value = [0, 1, 2, 3, 4, 5]
freq  = [37, 96, 58, 54, 18, 7]

cum_freq = []
total = 0
for f in freq:
    total += f
    cum_freq.append(total)


mean = sum([v*f for v,f in zip(value,freq)]) / total

def valAtPos(pos):
    for i, cf in enumerate(cum_freq):
        if pos <= cf:
            return value[i]

if total%2 == 0:
    median = valAtPos(total//2) + valAtPos(total//2 + 1)
    median = median/2
else:
    median = valAtPos((total+1)//2)

max_i = 0
for i,f in enumerate(freq):
    if f > freq[max_i]:
        max_i = i
mode = value[max_i]

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
