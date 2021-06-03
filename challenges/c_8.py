if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().strip().split())
    
    lista = list(arr)
    lista = [n for n in lista if n != max(lista)]
    
    print(max(lista))