import datetime

currentDT = datetime.datetime.now()

print(currentDT.strftime('%a'))
print(currentDT.strftime('%H:%M'))




now = currentDT.strftime('%H:%M')
two = currentDT.strftime('%a')
three = '16:29Thu'

if three == now + two:
    print('hej')