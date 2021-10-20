lNum = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = []

for i in range(len(lNum) - 1):
    if lNum[i] < lNum[i + 1]:
        answer.append(lNum[i + 1])

print(answer)