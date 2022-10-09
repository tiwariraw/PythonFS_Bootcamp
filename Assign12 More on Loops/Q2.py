# Write a python script to check whether a given number is Prime or not
    
def main():
    n = int(input('Enter a number: '))
    if n<=1:
        print('Non-Prime')
    else:
        bool1 = is_prime(n)
        if bool1 == True:
            print('Prime')
        else:
            print('Non-Prime')


def is_prime(n):
    flag = 1                    # range(2,n//2+1)      <-------optimization(till n//2)
    for i in range(2, n):      # 2 to n-1 ( range() includes beg value but excludes end value )
        if n % i == 0:
            flag = 0
            break
    if flag == 1:
        return True
    return False
    

main()
