my_list = []

x = int(input("hur många tal: "))

while len(my_list) < x:
    my_list.append(int(input("sätt in dina tal här: ")))

print(my_list)    
print(sum(my_list)/len(my_list))