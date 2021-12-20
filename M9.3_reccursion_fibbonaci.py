def caching_fibonacci(n):
    cache ={}
    def fibonaci(n):
        if n in cache: return cache[n]
        else:
            if n <= 1:
                return 1
            else:
                cache[n]=(fibonaci(n-1) + fibonaci(n-2))
                return cache[n]
    return fibonaci(n)


print(caching_fibonacci(20))

    # ИЛИ ТАК

def fib(n):
    cache = {}
    def _fib(n):
        if n not in cache:
            if n in [0, 1]:
                return 1
            cache[n] = _fib(n-1) + _fib(n-2)
        return cache[n]
    return _fib(n)


if __name__ == "__main__":
    print(
        fib(20)
    )