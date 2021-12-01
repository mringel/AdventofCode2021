with open('input.txt', 'r') as f:
  lines = f.readlines()

soundings = []

for line in lines:
  soundings.append(int(line.rstrip('\n')))

answer = 0

for i in range(len(soundings)-3):
  firstSum = soundings[i] + soundings[i+1] + soundings[i+2]
  secondSum = soundings[i+1] + soundings[i+2] + soundings[i+3]
  if secondSum > firstSum:
    answer+=1

print(answer)