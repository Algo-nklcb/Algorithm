def seperate_number(num):
    place_values = []
    while num != 0:
        tmp = num % 10
        place_values.append(tmp)
        num //= 10
    return place_values


num = int(input())
answer = 0
for n in range(1, num+1):
    place_values = seperate_number(n)
    if len(place_values) == 1:
        answer += 1
    else:
        d = int(place_values[0]) - int(place_values[1])
        curr = place_values[1]
        is_AP = True
        for digit in place_values[2:]:
            if int(curr) - int(digit) != d:
                is_AP = False
                break
        if is_AP:
            answer += 1
print(answer)
