def factorial(n):
    '''
        팩토리얼 구하는 함수
        n = 구하려는 n!
    '''
    factorial_num = 1
    for i in range(2, n+1):
        factorial_num *= i
    
    return factorial_num

def unique_check(relation):
    '''
        아규먼트의 요소들의 유일성을 체크해서 bool 자료형으로 리턴하는 함수
    '''
    rel_set = set(relation)

    return len(relation) == len(rel_set)

def minimal_check(candi_list, relation):
    '''
        candi_list 아규먼트 리스트 요소인 리스트 중에
        요소가 모두 relation에 포함된 요소만 가지고 있는
        리스트가 있는지 확인한 후
        있다면 => False
        없다면 => True
        를 Return
    '''
    for i in candi_list:
        
        is_contain = True
        for j in i:
            if j not in relation:
                is_contain = False
                break
        if is_contain:
            return False
    return True