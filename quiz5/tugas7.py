def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1  # Mengembalikan -1 jika tidak ada angka yang dapat dibagi oleh divisor

vals = [101, 4, 12, 24]
print(pembagi_indeks1(vals, 2))  

vals = [100, 66, 55, 64, 41, 35, 18, 64]
print(pembagi_indeks1(vals, 5))  
