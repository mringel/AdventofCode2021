with open('input.txt', 'r') as f:
  lines = f.readlines()

soundings = []

for line in lines:
  soundings.append(int(line.rstrip('\n')))

#print(soundings)

answer = 0

# elist = enumerate(soundings)


for i in range(len(soundings)-1):
  if soundings[i+1] > soundings[i]:
    answer+=1

print(answer)