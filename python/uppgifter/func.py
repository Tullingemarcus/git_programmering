

varde = []

x = int(input("hur många tal vill du ta medelvärde av:"))

def med(varde):
    return sum(varde) / len(varde)

while len(varde) < x:
    varde.append(int(input()))

print('medelvärdet är:', med(varde))