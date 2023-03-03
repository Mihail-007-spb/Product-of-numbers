"""Task:
Write a script that will find and display the minimum
positive integer q such that the product of the digits of this number will
be exactly equal to the number n. In the absence of such a number q, the script should
display the message "The desired number q does not exist!".
For example, for the number 70, the desired number will be 257."""



"""Задача:
Напишите скрипт, который будет находить и выводить на экран минимальное
положительное целое число q такое, что произведение цифр этого числа будет
в точности равняться числу n. В случае отсутствия такого числа q скрипт должен
выводить на экран сообщение «Искомого числа q не существует!».
Например, для числа 70 искомым числом будет 257."""




num = 70

ls1 = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for a1 in range(1, 10):
                for b1 in range(1, 10):
                    for c1 in range(1, 10):
                        q = a * b * c * a1 * b1 * c1
                        if q == num:
                            ls1.append(f'{a}{b}{c}{a1}{b1}{c1}')
ls3 = []
if len(ls1) != 0:
    for g in ls1:
        h = g.replace('1', '')
        ls3.append(h)
        ls7 = [int(i) for i in ls3 if int(i) > 10]
    print('Возможные комбинации:', set(ls7))
    print('Вот ответ:', min(ls7))
else:
    print('Искомого числа не существует!')