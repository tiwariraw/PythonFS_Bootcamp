# Write a python script to print all Prime numbers between two given numbers (both values inclusive)

def main():
    print('Enter start and end values: ')
    s,e = int(input()),int(input())
    if s<2:
        s=2
    prime_in_range(s,e)
    
    
def prime_in_range(start,end):
    for i in range(start,end+1):
        flag=1
        for j in range(2,i):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i,end=' ')


main()


    