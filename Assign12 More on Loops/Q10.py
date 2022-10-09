# Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

def main():
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    hcf = calc_hcf(n1,n2)
    if hcf==1:
        print('Co-Prime')
    else:
        print('Not Co-Prime')
    
    
def calc_hcf(n1,n2):
    hcf=1
    smallest = n1 if n1<n2 else n2
    for i in range(1, smallest+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf
    
    
main()