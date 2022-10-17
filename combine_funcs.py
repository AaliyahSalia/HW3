from operator import add

def   combine_funcs(op):
    def   combined(f, g):
        def   val(x):
            return   op(f(x), g(x))
        return   val
    return   combined

add_func = combine_funcs(add)

#add_func is used for combine_funcs.

h = add_func(abs, neg)
print(h(-5))

#add - function add(...)
#combine_funcs - combine_funcs(op)
#add_func - combined(f, g) [parent = f1]
#h = val(x) [parent = f2]

#f1: combine_funcs
#op - add(...)
#combined - combined(f,g) [parent=f1]
#Return value - combined(f, g) [parent=f1]

#f2: combined [parent = f1]
#f = 5
# g = -5
#val = val(x) [parent=f2]
#Return Value = val(x) [parent=f2]