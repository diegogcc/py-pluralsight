words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

l1 = []
for word in words:
    l1.append(len(word))            # [3, 9, 1, 4, 8, 2, 4, 2, 3, 10, 6, 6, 9]

l2 = [len(word) for word in words]  # [3, 9, 1, 4, 8, 2, 4, 2, 3, 10, 6, 6, 9]

l1 == l2  # True




from math import factorial
f = [factorial(x) for x in range(10)]  # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]