# Write a python script to display all prime numbers within a range.
# start = 15
# end = 45

def main():
    print('Enter start and end value: ')
    s,e = int(input()),int(input())
    if s<2:
        s=2
    prime(s,e)
    

def prime(start,end):
    for i in range(start,end+1):
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            print(i,end=' ')
        


if __name__ == '__main__':
    main()

