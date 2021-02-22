import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)

    prompt = "#%s: %s x %s = " % (questionNumber+1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*','Incorrect!')],
                      timeout=4, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # 1 second pause to see result (Correct or incorrect)

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))



