# for presenting the questions in random order
import random

def main():
    questions = {
        'YMRGSI': 'MYSIRG',
        'ARUASHB': 'SAURABH',
        'TPNOHY': 'PYTHON',
        'KLUETSO': 'TELUSKO',
        'OJNAGD': 'DJANGO',
        'OKUDSU': 'SUDOKU',
        'IODUG': 'GUIDO',
        'EMORDNILAP': 'PALINDROME',
        'MIROPT': 'IMPORT',
        'ANMODR': 'RANDOM'
    }
    score = puzzle_game(questions)
    print(f'Net Score is: {score}')


def puzzle_game(questions):
    """
    Game to guess the correct word from given jumbled words
    :param
    questions: dictionary of question and answers
    :return:
    score: total score
    """
    score = 0
    while True:
        for _ in range(5):
            print('Arrange the letters to form a valid word')
            print(random.choice(list(questions.keys())))
            user_ans = input().upper()
            if user_ans in list(questions.values()):
                score += 1
                print('Correct')
            else:
                score -= 1
                print('Wrong')
        choice = input("Press 'y' to play the round again else 'q' to quit: ")
        if choice.lower() == 'q':
            break
    return score


if __name__ == '__main__':
    main()
    
    
# Project1 using list

# import random

# def main():
#     questions = ['YMRGSI', 'ARUASHB', 'TPNOHY', 'KLUETSO', 'OJNAGD', 'OKUDSU', 'IODUG', 'EMORDNILAP', 'MIROPT',
#                  'ANMODR']
#     answers = ['MYSIRG', 'SAURABH', 'PYTHON', 'TELUSKO', 'DJANGO', 'SUDOKU', 'GUIDO', 'PALINDROME', 'IMPORT', 'RANDOM']
#     score = puzzle_game(questions, answers)
#     print(f'Net Score is: {score}')


# def puzzle_game(questions, answers):
#     """
#     Game to guess the correct word from given list of jumbled words
#     :param
#     questions: list of question
#     answers:  list of answers
#     :return:
#     score: total score
#     """
#     score = 0
#     while True:
#         for _ in range(5):
#             print('Arrange the letters to form a valid word')
#             print(random.choice(questions))
#             user_ans = input().upper()
#             if user_ans in list(answers):
#                 score += 1
#                 print('Correct')
#             else:
#                 score -= 1
#                 print('Wrong')
#         choice = input("Press 'y' to play the round again else 'q' to quit: \n")
#         if choice.lower() == 'q':
#             break
#     return score


# if __name__ == '__main__':
#     main()