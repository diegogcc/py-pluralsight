from itertools import islice, count
from filtering import is_prime


hundred_primes = islice((x for x in count() if is_prime(x)), 100)
h = list(hundred_primes)
print(h)
print(sum(islice((x for x in count() if is_prime(x)), 100)))

# ----------------------------------------------------------------------------------

any([False, False, True]) #  True
all([False, False, True]) #  False

any(is_prime(x) for x in range(525, 540)) #  False
any(is_prime(x) for x in range(0, 10)) #  True

all(name == name.title() for name in ['London', 'New York', 'Sydney']) # True

# ----------------------------------------------------------------------------------

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

for item in zip(sunday, monday):
    print(item)

# (12, 13)
# (14, 14)
# (15, 14)
# (15, 14)
# (17, 16)
# (21, 20)
# (22, 21)
# (22, 22)
# (23, 22)
# (22, 21)
# (20, 19)
# (18, 17)

tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print('min={:4.1f}, max={:4.1f}, average={:4.1f}'.format(min(temps), max(temps), sum(temps) / len(temps)))

# min= 2.0, max=13.0, average= 9.0
# min= 2.0, max=14.0, average=10.0
# min= 3.0, max=15.0, average=10.7
# min= 7.0, max=15.0, average=12.0
# min= 9.0, max=17.0, average=14.0
# min=10.0, max=21.0, average=17.0
# min=11.0, max=22.0, average=18.0
# min=12.0, max=22.0, average=18.7
# min=10.0, max=23.0, average=18.3
# min= 9.0, max=22.0, average=17.3
# min= 8.0, max=20.0, average=15.7
# min= 8.0, max=18.0, average=14.3

# ----------------------------------------------------------------------------------

from itertools import chain

temperatures = chain(sunday, monday, tuesday)
print(list(temperatures)) 
# [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18, 13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17, 2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

all(t > 0 for t in temperatures)
# True