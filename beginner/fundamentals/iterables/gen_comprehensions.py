million_squares = (x*x for x in range(1, 1000001))

sum(x*x in range(1000001))
# Result is ready in less than a second and consumes an INSIGNIFICANT ammount of memory 