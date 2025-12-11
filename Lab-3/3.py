#std_dev
values = [46, 69, 32, 60, 52, 41]
N = len(values)

mean = sum(values)/N

sq_dev = [(v-mean)**2 for v in values]
std_sq_dev = sum(sq_dev)/(N-1)

print("Standard square Deviation: ", std_sq_dev)
