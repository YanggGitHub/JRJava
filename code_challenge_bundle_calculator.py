base = [9,6,3]
input = 31
result = []

print("Bundle number:")
for x in base:
    print(str(x) + " ", end="")
print("\n")

for x in base:
    value = input % x
    if value == 0:
        for i in range(int(input/x)):
          result.append(x)
        break    
    elif value not in base:
        continue
    elif value in base:
        for i in range(int(input/x)):
          result.append(x) 
        result.append(value)          
        break       
        

print("bundle use:\n")
if result == []:
    print("no fit bundles")
else:    
    for x in result:
        print(str(x) + " ", end="")
print("\n")


