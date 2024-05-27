"""
Returns a list of prims <=n
"""
def prime(n):
    prime_list = []
    for i in range(n):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

"""
Returns 
- a tuple (a,b) where a^2 + b^2 = p, and b>a
- False if the input is not the sum of 2 squares
"""
def get_sum_square(p):
    for a in range(1,p):
        b = p-(a**2)
        if b <=0:
            return False
        if int(b**.5) == b**.5:
            return (a,int(b**.5))
    return False

"""
Returns a dictionary of all primes <=n that are the sum of two squares
of the form {prime:(a,b)} where a^2 + b^2 = prime. b>a
"""
def square_sum_prime(n):
    square_sum_primes = []
    square_sums = []
    prime_list = prime(n)
    for p in prime_list:
        if p%4 == 1:
            square_sum_primes.append(p)
            square_sums.append(get_sum_square(p))

    return dict(zip(square_sum_primes, square_sums))

"""
Returns a dictionary of all integers c <=n that are pythag triples:
i.e:
    a dictionary of the form {c: (a,b)} 
such that:
    c = a^2 + b^2

* note I know these are normally of the form c^2 = a^2 + b^2, but this makes 
    it consistent with the format for square sum primes
"""
def pythag_triples(n):
    square_sum_cs = []
    square_sums = []

    squares = [i**2 for i in range(1,int(n**.5))]
    for c in squares:
        sum = get_sum_square(c)
        if sum != False:
            square_sum_cs.append(c)
            square_sums.append(sum)

    return dict(zip(square_sum_cs, square_sums))

