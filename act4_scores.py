num = int(input("How many students?"))

scores = []
total = 0 

for i in range(num):
    score = float(input("Enter score: "))
    scores.append(score)
    total = total + score

average = total / num
highest = max(scores)

print("\nTotal:", total)
print("Average:", round(average, 2))
print("Highest Score:", highest)