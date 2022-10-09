# Write a python script to reverse a number.

# M1                                               #Reversing positive and negative numbers both
n = int(input('Enter a number: '))                 # n = int(input('Enter a number: '))
rev = 0                                            # n__abs = abs(n)
while n:                                           # rev = 0
    rev = rev*10 + n%10                            # while n_abs:
    n = n//10                                      #   rev = rev*10 + n_abs%10    
print(rev)                                         #   n_abs = n_abs//10 
                                                   # if n>=0:
                                                   #    print(rev)
                                                   # else:
                                                   #    print(-rev)
                                                   

# # M2
n = input('Enter a number: ')       #taking string input
n = n[::-1]                         #reversing the string
rev = int(n)                        #convert str to int
print(n)
