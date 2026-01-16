class MathOps:
    def add(self, *args):
        return sum(args)

m = MathOps()

print(m.add(2))
print(m.add(2, 3))
print(m.add(2, 3, 4))