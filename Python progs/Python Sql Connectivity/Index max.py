m = [1,5,5,5,5,1]
max = m[0]
indexOfMax = 0
for i in range(1,len(m)):
    if m[i]>max:
        max = m[i]
        indexOfMax = i

print(indexOfMax)
