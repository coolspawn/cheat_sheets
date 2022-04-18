# calculate qty of bst for given n
def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res


def catalan(n):
    c = binomial_coeff(2 * n, n)
    return c // (n + 1)


def bst_count(n):
    count = catalan(n)
    # for all DT:
    # count = count * n!
    return count


# checks
count = bst_count(5)
print(count)
