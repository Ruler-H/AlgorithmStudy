
def factorial(num):
    '''
    팩토리얼 구하는 함수
    '''
    factorial_num = 1
    for i in range(2, num+1):
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

def prime_mul_measure(prime_mul):
    '''
    소수 곱으로 이루어진 수에서
    약수 중 작은 수를 Return
    '''
    max_iter = int(prime_mul ** 0.5)
    prime_array = [True for i in range(max_iter + 1)]

    for i in range(2, max_iter + 1):
        if prime_array[i] == True:
            j = 2
            if prime_mul % i == 0:
                return i
            while i * j <= max_iter:
                prime_array[i * j] = False
                j += 1

class TrieNode:
    '''Trie 자료구조에서 사용되는 Node'''
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.length = []

class Trie:
    '''Trie 자료구조'''
    def __init__(self):
        self.head = TrieNode(None)

    def insert(self, word):
        '''Trie 자료구조에 String Data를 삽입'''
        cur_node = self.head
        word_length = len(word)
        for w in word:
            cur_node.length.append(word_length)
            if w not in cur_node.children:
                cur_node.children[w] = TrieNode(None)
            cur_node = cur_node.children[w]
        cur_node.data = word

    def search(self, query):
        '''Trie 자료구조 내에 해당 query 조건에 맞는 데이터의 수를 반환'''
        cur_node = self.head
        for q in query:
            if q == '?':
                return cur_node.length.count(len(query))
            elif q not in cur_node.children:
                return 0
            else:
                cur_node = cur_node.children[q]
        if cur_node.data:
            return 1
        else:
            return 0