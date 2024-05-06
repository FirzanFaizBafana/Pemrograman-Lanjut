def print_squares(n):
    for i in range(n):
        print(i**2)


n = int(input("Masukkan nilai n: "))
print("Hasil:")
print_squares(n)

# part B

def print_odd_squares(n):
    for i in range(n):
        if i % 2 != 0:  
            print(i**2)


n = int(input("Masukkan nilai n: "))
print("Hasil:")
print_odd_squares(n)
