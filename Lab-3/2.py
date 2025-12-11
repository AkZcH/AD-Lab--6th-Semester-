heights = [
    (59.95, 61.95),
    (61.95, 63.95),
    (63.95, 65.95),
    (65.95, 67.95),
    (67.95, 69.95),
    (69.95, 71.95),
    (71.95, 73.95),
    (73.95, 75.95),
]

freq = [5, 3, 15, 40, 17, 12, 7, 1]
total_players = sum(freq)

#percentage below 65.95:
below_6595 = freq[0] + freq[1] + freq[2]
perc_a = (below_6595 / total_players) * 100

#percentage between 61.95 and 65.95:
btwn_6195_6595 = freq[1] + freq[2]
perc_b = ( btwn_6195_6595 / total_players) * 100

#number of players between 61.95 and 71.95:
btwn_6195_7195 = freq[1] + freq[2] + freq[3] + freq[4] + freq[5]

print("percentage below 65.95: ", perc_a, "%")
print("percentage between 61.95 and 65.95: ", perc_b, "%")
print("number of players between 61.95 and 71.95 :", btwn_6195_7195)
