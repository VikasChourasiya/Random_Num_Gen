def randome_num_gen(start,end):
    num = set(map(str,range(start,end+1)))
    return num.pop()

n = randome_num_gen(0,10)
k = int(n)
s = 0
 
for i in range(1000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k += 2
     
print(s)
