def cyc(g1,g2,g3):
     def get(n):
         def num(x):
             if n==0:
                 return x
             else:
                 return cyc(g2,g3,g1)(n-1)(g1(x))
         return num
     return get

def add_one(x):
    return x+1
def times_two(x):
    return x*2
def add_three(x):
    return x+3

mycyc = cyc(add_one,times_two,add_three)

h = mycyc(0)
print(h(5))
print()

h =mycyc(2)
print(h(1))
print()

h=mycyc(3)
print(h(2))
print()

h=mycyc(4)
print(h(2))
print()

h=mycyc(6)
print(h(1))

