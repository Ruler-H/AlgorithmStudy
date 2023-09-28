def factorial(n):
    '''
        팩토리얼 구하는 함수
        n = 구하려는 n!
    '''
    factorial_num = 1
    for i in range(2, n+1):
        factorial_num *= i
    
    return factorial_num