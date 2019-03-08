#Find the next bigger number with the same digits You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

#12 ==> 21 513 ==> 531 2017 ==> 2071

#If no bigger number can be composed using those digits, return -1:

#9 ==> -1 111 ==> -1 531 ==> -1

def next_bigger(n):
    digits = list(str(n))
    i =len(digits)-1
    while digits[i] <= digits[i-1]:
        i-=1
        if i <= 0: return -1
    j=i
    while digits[j] != min(filter(lambda x: x > digits[i-1],digits[i:])): j+=1
    digits[i-1],digits[j]=digits[j], digits[i-1]
    digits[i:] = sorted(digits[i:])
    return int(''.join(digits))
