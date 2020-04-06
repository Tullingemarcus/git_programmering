myList = [6,5,6,2,2]

seen = []
for number in myList:
    if number in seen:
        print(seen)
    else:
        seen.append(number)