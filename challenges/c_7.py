if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    contenedor = [[xn, yn, zn] for xn in range(x+1) for yn in range(y+1) for zn in range(z+1) if x+y+z != n]
    
    print(contenedor)