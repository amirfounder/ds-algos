def fibonacci_with_memo(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_with_memo(n-1, memo) + fibonacci_with_memo(n-2, memo)
    return memo[n]


if __name__ == '__main__':
    result = fibonacci_with_memo(50, {})
    print(result)
