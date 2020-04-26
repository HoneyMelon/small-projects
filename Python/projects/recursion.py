def deliver_presents(houses):
    """
    @param houses: list
    """
    if len(houses) == 1:
        print('Delivering to:', houses[0])
        return
    mid = len(houses) // 2
    first_half = houses[:mid]
    second_half = houses[mid:]
    deliver_presents(first_half)
    deliver_presents(second_half)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def rec_sum(n):
    if n <= 1:
        return 1
    return n + rec_sum(n - 1)


def sum_list(list):
    if len(list) == 0:
        return 0
    head_of_list = list[0]
    rest = list[1:]
    return head_of_list + sum_list(rest)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def to_base(n, base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    return to_base(n // base, base) + digits[n % base]


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def sum_series(n):
    if n <= 0:
        return 0
    return n + sum_series(n - 2)


def harmonic_sum(n):
    if n <= 1:
        return 1
    return 1 / n + harmonic_sum(n - 1)


def geometric_sum(n):
    if n < 0:
        return 0
    return 1 / (pow(2, n)) + geometric_sum(n - 1)


def power(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    elif a == 0:
        return 0
    return a * power(a, b - 1)


def gcd(n, k):
    bigger = max(n, k)
    smaller = min(n, k)
    if smaller == 1:
        return 1
    if smaller == 0:
        return bigger
    return gcd(smaller, bigger % smaller)


def max_of_list(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 0:
        return 0
    max_list = max_of_list(list[1:])
    if list[0] > max_list:
        return list[0]
    return max_list


def _print_pattern(n, m, flag):
    print(n)
    if (n <= 0 and flag is False) or flag is True:
        if n == m:
            return
        _print_pattern(n + 5, m, True)
    else:
        _print_pattern(n - 5, m, False)


def print_pattern(n):
    _print_pattern(n, n, False)


def do_something_iterative(n):
    a = 1
    b = 1
    print(a)
    print(b)
    while n > 0:
        c = a + b
        print(c)
        a = b
        b = c
        n = n - 1


def do_something_recursive(n):
    print(1)
    print(1)
    _do_something_recursive(n, 1, 1)


def _do_something_recursive(n, a, b):
    if n <= 0:
        return
    else:
        c = a + b
        print(c)
        _do_something_recursive(n - 1, b, c)


def do_something_iterative2(n, k):
    r = 1
    for j in range(1, k + 1):
        r = r * (n + 1 - j) / j
    print(r)


def _do_something_recursive2(r, j, n, k):
    if j > k + 1:
        print(r)
        return
    r = r * (n + 1 - j) / j
    _do_something_recursive2(r, j + 1, n, k)


def do_something_recursive2(n, k):
    _do_something_recursive2(1, 1, n, k)


def main():
    #test_houses = ['Anna\'s', 'Jimmy\'s', 'Kevin\'s']
    #deliver_presents(test_houses)
    #print(factorial(4))
    #print(rec_sum(10))
    #print(sum_list([1, 2, 3]))
    #print(fibonacci(6))
    #print(to_base(2835, 16))
    #print(sum_of_digits(25))
    #print(sum_series(10))
    #print(harmonic_sum(7))
    #print(geometric_sum(7))
    #print(power(2, 3))
    #print(gcd(12, 17))
    #print(max_of_list([1, 5, 87, 45, 13, 70]))
    #print_pattern(16)
    #do_something_iterative(10)
    #do_something_recursive(10)
    do_something_iterative2(8, 3)
    do_something_recursive2(8, 3)


if __name__ == '__main__':
    main()
