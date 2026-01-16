nums = [10, 11, 12, 13, 17, 20, 23]

prime = []
for i in nums:
    is_prime = True
    for j in range (2, int(i**0.5)+1):
        if (i%j ==0):
            is_prime = False
            break
    if (is_prime):
            prime.append(i)
print(prime)
