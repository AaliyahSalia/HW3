def foo(f):
    def foo2(g):
        def foo(h):
            return h
        return g
    return f


h = int(input("Please enter a number: "))
print(foo(h))
