# ascii a = 97

n = int(input())

word = input()
answer = 0

for ind, char in enumerate(word):
    answer += (ord(char)-96)*(31**ind)

print(answer % 1234567891)