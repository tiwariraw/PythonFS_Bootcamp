# Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
 
# output:
# 12 ---> 1100
# 25 ---> 11001

# M1 (iterative approach)
n = int(input('Enter n: '))
list1 = []
while n:
    list1.append(n%2)
    n=n//2
for i in reversed(list1):     #doesn't modifies the list
    print(i,end=' ')
# OR (in place of line 13 and 14, write line 16,17,18)
# list1.reverse()          #list is reversed permanently
# for i in list1:
#       print(i,end=' ')


# M2 (recursive approach)
def main():
    n = int(input('Enter n: '))
    d2b(n)

def d2b(n):
    if n==0:
        return
    d2b(n>>1)
    print(n&1,end=' ')

main()


# M3
n = int(input('Enter n: '))
s=''
while n:
    s = str(n%2)+s         #string concatenation
    n=n//2
print(s)

