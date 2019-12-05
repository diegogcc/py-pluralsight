words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

l1 = set()
for word in words:
    l1.add(len(word))              # {1, 2, 3, 4, 6, 8, 9, 10}

l2 = {len(word) for word in words} # {1, 2, 3, 4, 6, 8, 9, 10}

l1 == l2 # True




from math import factorial
f = {factorial(x) for x in range(10)} # ~~~ {40320, 1, 2, 362880, 6, 720, 5040, 24, 120}