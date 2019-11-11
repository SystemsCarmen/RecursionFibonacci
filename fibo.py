 def fibo(n):
    if n<=0:
        return 1
    return (fibo(n-1) + fibo(n-2))