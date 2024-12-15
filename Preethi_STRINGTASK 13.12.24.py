#PROBLEM--1

def merge_alternately(word1, word2):
   
    merged = [char1 + char2 for char1, char2 in zip(word1, word2)]
    
    return ''.join(merged) + word1[len(word2):] + word2[len(word1):]

print(merge_alternately("abc", "pqr"))  
print(merge_alternately("ab", "pqrs"))

#PROBLEM--2

def can_place_flowers(flowerbed, n):
    count = 0
    i = 0
    length = len(flowerbed)
    while i < length:
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1  
            count += 1
            i += 1 
        if count >= n:
            return True
        i += 1  
    return count >= n

print(can_place_flowers([1, 0, 0, 0, 1], 1))  
print(can_place_flowers([1, 0, 0, 0, 1], 2))  



