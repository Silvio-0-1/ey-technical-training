nums = {10, 20, 30, 40}

s = {10, 20, 30}
s2 = set()

s = {1, 2, 3}
s.add(4)
print(s)

s.update([5, 6])
print(s)


s.remove(3) # raises error if not found
s.discard(10) # does nothing if not found

s.pop() # remove random element
print(s) 
