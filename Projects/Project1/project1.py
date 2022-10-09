# for presenting the questions in random order
import random

def shuffle_word(wrd):
    pw = random.sample(wrd,k=len(wrd))
    # print(pw)  ---> returns a list of randomized characters eg. ['A', 'E', 'T', 'H', 'F', 'R']
    return ''.join(pw)

def print_puzzle_questions(word,score):
    problem_word = shuffle_word(word)
    print('Arrange the letters to form a valid word: ')
    print(problem_word)
    user_ans = input()
    if user_ans.upper() == word:    #user_ans.upper() because the word is store in upper case (see line 23)
        print('Correct')
        score += 1
    else:
        print('Wrong')
        score -= 1
    return score

def main():
    score = 0
    words = ['FATHER', 'BREAK', 'COUNTRY']
    # random.sample randomizes the list elements and returns a list
    words = random.sample(words,k=len(words))
    # print(words)    ----> to check what random.sample(words,k=len(words)) returns
    
    for word in words:
        score = print_puzzle_questions(word,score)

    print("Net Score: ",score)

if __name__ == '__main__':
    main()
    
    

# Project1: https://drive.google.com/file/d/1uhsXZuC9HGrEmurk10xGVcuaeSRbEKIS/view
# Project1 Solution: disccused inn 27/09/2022 lecture


# random.choice([1,23,4,5,6])   ------> read about choice() of random module