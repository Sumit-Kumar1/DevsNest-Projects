from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if(answer == question):
        return True
    else:
        return False

def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    i = random.randint(1,4)
    valid  = QUESTIONS[ques]["answer"]
    if(i == valid):
        i = random.random.randint(1, 4)
    
    answer = f"option{valid}"


    print(f'\tQuestion 1: {QUESTIONS[ques]["name"]}' )
    print(f'\t\tOptions:')
    if i == 1:
        print(f'\t\t\tOption 1: {QUESTIONS[ques]["option1"]}')
    elif i == 2 :
        print(f'\t\t\tOption 2: {QUESTIONS[ques]["option2"]}')
    elif i == 3:
        print(f'\t\t\tOption 3: {QUESTIONS[ques]["option3"]}')
    else:
        print(f'\t\t\tOption 4: {QUESTIONS[ques]["option4"]}')

    print(f'\t\t\tOption {valid}: {QUESTIONS[ques][answer]}')
    ans = input('Your choice : ')
    return ans
    


def kbc():
    questions_answered = int(0)
    amount_won = int(0)
    lifeline = True
    print("----------Welcome to the Game--------\n")
    print("--INFO---\n1.There are 15 questions.\n2.You can use life line once which is 50-50 (Just type 'lifeline' in answer to use)\n3.To quit game at any question type 'quit'\n")
    while(questions_answered != 15):
        '''
            Rules to play KBC:
            * The user will have 15 rounds
            * In each round, user will get a question
            * For each question, there are 4 choices out of which ONLY one is correct.
            * Prompt the user for input of Correct Option number and give feedback about right or wrong.
            * Each correct answer get the user money corresponding to the question and displays the next question.
            * If the user is:
                1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
                2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
                3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
            * If the answer is wrong, then the user will return with the minimum reward.
            * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
                prompt again for the input of answer.
            * NOTE:
                50-50 lifeline can be used ONLY ONCE.
                There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
            * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
                instead of the minimum amount.
        '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

        print(f'\tQuestion 1: {QUESTIONS[questions_answered]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[questions_answered]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[questions_answered]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[questions_answered]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[questions_answered]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if(ans == "lifeline" and lifeline and questions_answered != 14):
            lifeline = False
            ans = lifeLine(questions_answered)
        elif(ans == "quit" or "Quit" or "Exit" or "exit"):
            if(questions_answered < 5):
                print("Total Price Won : Rs 0")
            elif (questions_answered >= 5 and questions_answered < 11):
                print("Total Price won: Rs 10,000")
            elif(questions_answered >= 11 and questions_answered < 15):
                print("Total Price Won: Rs 3,20,000")
            elif (questions_answered == 15):
                print("Total Price Won: Rs 1,00,00,000")
        else:
            print("You can't use lifeline")
            ans = input('your choice ( 1-4 ): ')
        
        if(ans == "quit" or "Quit" or "Exit" or "exit"):
            break

    # check for the input validations
    
        if isAnswerCorrect(QUESTIONS[questions_answered]["answer"], int(ans) ):
        # print the total money won.
        # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            amount_won += QUESTIONS[questions_answered]["money"]
            questions_answered += 1
            if(questions_answered == 5):
                print("Congratulations, You are on level 1.\nLifeLines left {}")
                print("Won prices till now: {}\n".format(amount_won))
            elif questions_answered == 11 :
                print("Congratulations, You are on 2nd Level")
                print("Won Price till Now: {}\n",format(amount_won))


        else:
        # end the game now.
        # also print the correct answer
            print('\nIncorrect !')
            if(questions_answered < 5):
                print("Total Price Won : Rs 0")
            elif (questions_answered >= 5 and questions_answered < 11):
                print("Total Price won: Rs 10,000")
            elif(questions_answered >= 11 and questions_answered < 15):
                print("Total Price Won: Rs 3,20,000")
            elif (questions_answered == 15):
                print("Total Price Won: Rs 1,00,00,000")
            break


    # print the total money won in the end.

kbc()
print("-----Thanks for playing my game--------")