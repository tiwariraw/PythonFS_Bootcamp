# WPS to check whether two given strings are identical, first comes after second or second comes after first in dictionary order.
def main():
    s1 = input('Enter first string: ').strip()
    s2 = input('Enter second string: ').strip()
    match (s1,s2):
        case (s1,s2) if s1 == s2:
            print('Identical')
        case (s1,s2) if s1 > s2:
            print(f'{s2} comes before s1 ')
        case (s1,s2) if s1 < s2:
            print(f'{s1} comes before s2')


if __name__ == '__main__':
    main()