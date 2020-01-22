scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier', 'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']

sorted(scientists, key=lambda name: name.split()[-1])
# 'Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 'Antoine Lavoisier', 'Carl Linnaeus', 'Dmitri Mendeleev', 'Isaac Newton', 'Alfred Wegener']


last_name = lambda name: name.split()[-1]