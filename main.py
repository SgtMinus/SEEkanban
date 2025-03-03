import math
N = 84032429242009
e = 2581907
C = '''
54879925681459
72167008182929
17828219756166
17814399744948
37136636080011
77223434260215
4272415279426
73759271926435
74021335775875
16903113250201
77520052156956
41247980943013
'''
result=''
n = math.floor(math.sqrt(N))+1

i = 0
while True:
    i+=1
    t = n + i
    print(f"t{i} = n + {i} = {t}")
    w = t*t-N
    print(f"w{i} - t{i}^2 - N = {t*t} - {N} = {w}")
    w_sqrt = math.sqrt(w)
    if w_sqrt%1 !=0:
        continue
    else:
        w_sqrt = int(w_sqrt)
        print(f"sqrt(w) = {w_sqrt}")
        break
    
p = t+w_sqrt
q = t-w_sqrt
phi = round((p-1)*(q-1))
d = pow(e,-1,phi)
print(f"p = t + sqrt(w) = {t} + {w_sqrt} = {p}")
print(f"q = t - sqrt(w) = {t} - {w_sqrt} = {q}")
print(f"phi = (p-1) * (q-1) = {p-1}*{q-1} = {phi}")
print(f"d = e^(-1) mod phi = {e}^(-1) mod {phi} = {d}")

for i, c in enumerate(C.split()):
    m = pow(int(c),d,N)
    part = m.to_bytes(4, byteorder='big').decode('cp1251')
    print(f"m{i} = C[{i}]^d mod N = {c}^{d} mod {N} = {m}, text - {part}")
    result+=part
print(result)
