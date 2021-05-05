import numpy as np 

def matrice(n):
    d = dict()
    conta = 0
    while conta <n:
        for el in range(n):
            if len(d) == n:
                break
            else:
                i = np.random.randint(0, 10)
                j = np.random.randint(0, 10)
                z = np.random.randint(1,31)
                if ((i,j) not in d): 
                    if (i ==j):
                        d[(i,j)] = z
                        conta+=1
                    elif i !=j:
                        d[(i,j)] = z
                        d[(j, i)] = z
                        conta+=2
    return d

print(matrice(10))
