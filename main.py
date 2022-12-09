import tkinter as tk
from tkinter import messagebox

bg = '#FFFFFF'
bbg = 'white'
fg = '#000000'
window = tk.Tk()
window.configure(bg=bg)
window.title("Викторина по информатике | Неделя науки")
window.geometry("700x400")

rightans = tk.IntVar(window, 0)
wrongans = tk.IntVar(window, 0)
result = tk.IntVar(window, 2)
def right():
    rightans.set(rightans.get() + 1)
def wrong():
    wrongans.set(wrongans.get() + 1)
def cresult():
    if rightans.get() >= 0 and rightans.get() <= 2:
        result.set(result.get())
    elif rightans.get() >= 3 and rightans.get() <= 5:
        result.set(result.get() + 1)
    elif rightans.get() >= 6 and rightans.get() <= 8:
        result.set(result.get() + 2)
    elif rightans.get() >= 9 and rightans.get() <= 10:
        result.set(result.get() +3)

title = tk.Label(window, text='Викторина по информатике\nпо теме "Базовые алгоритмические структуры"', font="Calibri 24", bg=bg, fg=fg)
title.pack()
description = tk.Label(window, text="Добро пожаловать на викторину! Она сделана на Python. Вам дается 10 вопросов, \n за каждый вы получаете баллы «верно» и «неверно».\n От вашего балла зависит ваша оценка...\n Удачи!", font="Calibri 12",bg=bg, fg=fg)
description.pack()
button = tk.Button(window, text="Начать", command=lambda: q1(right, wrong),bg=bbg, fg=fg)
button.pack()
wrong_countertext = tk.Label(window,text=f'Неправильных ответов:', font='Calibri 12', bg=bg, fg=fg)
right_countertext = tk.Label(window,text=f'Правильных ответов: ', font='Calibri 12', bg=bg, fg=fg)
wrong_counter = tk.Label(window, textvariable=wrongans, font='Calibri 12', bg=bg, fg=fg)
right_counter = tk.Label(window, textvariable=rightans, font='Calibri 12', bg=bg, fg=fg)
wrong_countertext.place(x=100, y=260)
right_countertext.place(x=100, y=230)
wrong_counter.place(x=320, y=260)
right_counter.place(x=320, y=230)

def q1(right, wrong):
    question1 = tk.Label(window, text="1. Определите значение переменной b после выполнения фрагмента алгоритма\na=14                                \nb=4                                  \na=a/2-b                          \nb=(a*b)/2                       \nb=a+b                             ",bg=bg,fg=fg)
    answer1 = tk.Entry(bg=bbg,fg=fg)
    button1 = tk.Button(window, text="Продолжить", command=lambda: tr1(q2, right, wrong), bg=bbg,fg=fg)
    description.destroy()
    button.destroy()
    question1.pack()
    answer1.pack()
    button1.pack()

    def tr1(q2, right, wrong):
        if answer1.get().lower() == "9":
            messagebox.showinfo("Верно!","Вы умеете считать!")
            question1.destroy()
            answer1.destroy()
            button1.destroy()
            right()
            q2(right, wrong)
        else:
            messagebox.showerror("Неверно!", "Сначала a/2-b=3, потом b=(3*4)/2=6, и под конец мы складываем b=a+b, что получается b=9")
            wrong()
            question1.destroy()
            answer1.destroy()
            button1.destroy()
            q2(right, wrong)
def q2(right, wrong):
    question2 = tk.Label(window, text='2. Чему будет равно значение переменной "c" после выполнения программы?\na=28                                \nb=7                                 \nc=a % b + a//b             ', bg=bg, fg=fg)
    answer2 = tk.Entry(bg=bbg, fg=fg)
    button2 = tk.Button(window, text="Продолжить", command=lambda: tr2(q3, right, wrong), bg=bbg,fg=fg)
    question2.pack()
    answer2.pack()
    button2.pack()

    def tr2(q3, right, wrong):
        if answer2.get().lower() == "4":
            messagebox.showinfo("Верно!", "Ответом на вопрос была цифра 4")
            right()
            question2.destroy()
            answer2.destroy()
            button2.destroy()
            q3(right, wrong)
            
        else:
            messagebox.showerror("Неверно!", "% - знак остатка от деления. 28 % 7 будет равно 0\n28//7 (деление нацело) = 4\nc=0+4=4")
            wrong()
            question2.destroy()
            answer2.destroy()
            button2.destroy()
            q3(right, wrong)
def q3(right, wrong):
    question3 = tk.Label(window, text="Вы создали программу на Python. Ваш алгоритм выглядит так:", bg=bg, fg=fg)
    question3e = tk.Label(window, text='a=int(input())                  \nif a>1:                               \nb=(a**2+a)/2\nprint(b)                           ', bg=bg, fg=fg)
    question3_1 = tk.Label(window, text="Какой результат будет у переменной b, если переменная a равна 18?", bg=bg, fg=fg)
    answer3 = tk.Entry(bg=bbg, fg=fg)
    button3 = tk.Button(window, text="Продолжить", command=lambda: tr3(q4, right, wrong), bg=bbg, fg=fg)
    question3.pack()
    question3e.pack()
    question3_1.pack()
    answer3.pack()
    button3.pack()

    def tr3(q4, right, wrong):
        if answer3.get().lower() == "171":
            messagebox.showinfo("Верно!","Вы можете заменить компьютер!")
            right()
            question3.destroy()
            question3e.destroy()
            question3_1.destroy()
            answer3.destroy()
            button3.destroy()
            q4(right, wrong)
        else:
            messagebox.showerror("Неверно!","Удивлен, что вы знаете язык программирования, но не знаете сам синтаксис")
            wrong()
            question3.destroy()
            question3e.destroy()
            question3_1.destroy()
            answer3.destroy()
            button3.destroy()
            q4(right, wrong)
def q4(right, wrong):
    question4 = tk.Label(window, text="4. Вычислите значение y и определите, что выведет программа на экран\nx=12                               \nif x<10:                           \ny=210               \nelse:                                \ny=x/4               \nprint(y)                            ", bg=bg, fg=fg)
    answer4 = tk.Entry(bg=bbg, fg=fg)
    button4 = tk.Button(window, text="Продолжить", command=lambda: tr4(q5, right, wrong), bg=bbg, fg=fg)
    question4.pack()
    answer4.pack()
    button4.pack()

    def tr4(q5, right, wrong):
        if answer4.get().lower() == "3":
            messagebox.showinfo("Верно!", "Вы молодец!")
            right()
            question4.destroy()
            answer4.destroy()
            button4.destroy()
            q5(right, wrong)
        else:
            messagebox.showerror("Неверно!", "Сначала мы выясняем, если x<10. Но x=12, поэтому условие переходит в else: y=x/4=3")
            wrong()
            question4.destroy()
            answer4.destroy()
            button4.destroy()
            q5(right, wrong)
def q5(right, wrong):
    question5 = tk.Label(window, text="5. Как еще можно назвать управляющую переменную цикла for?", bg=bg, fg=fg)
    answer5 = tk.Entry(bg=bbg, fg=fg)
    button5 = tk.Button(window, text="Продолжить", command=lambda: tr5(q6, right, wrong), bg=bbg, fg=fg)
    question5.pack()
    answer5.pack()
    button5.pack()

    def tr5(q6, right, wrong):
        if answer5.get().lower() == "параметр":
            messagebox.showinfo("Верно!", "Также она может называться счётчиком")
            right()
            question5.destroy()
            answer5.destroy()
            button5.destroy()
            q6(right, wrong)
        elif answer5.get().lower() == "счётчик" or answer5.get().lower() == "счетчик":
            messagebox.showinfo("Верно!", "Также она может называться параметром")
            right()
            question5.destroy()
            answer5.destroy()
            button5.destroy()
            q6(right, wrong)
        else:
            messagebox.showerror("Неверно!", "Её называют либо параметром, либо счётчиком.\n\nЛибо автор программы просто не предусмотрел ваш вариант.")
            wrong()
            question5.destroy()
            answer5.destroy()
            button5.destroy()
            q6(right, wrong)
def q6(right, wrong):
    question6 = tk.Label(window, text="6. С помощью какой логической операции можно записать в условии математическое соотношение\n1<=N<=100", bg=bg, fg=fg)
    answer6 = tk.Entry(bg=bbg, fg=fg)
    button6 = tk.Button(window, text="Продолжить", command=lambda: tr6(q7, right, wrong), bg=bbg, fg=fg)
    question6.pack()
    answer6.pack()
    button6.pack()

    def tr6(q7, right, wrong):
        if answer6.get().lower() == "and":
            messagebox.showinfo("Верно!", "")
            right()
            question6.destroy()
            answer6.destroy()
            button6.destroy()
            q7(right, wrong)
        else:
            messagebox.showerror("Неверно!", "and можно использовать как оператор для этой задачи. Например:\nif N>=1 and N<=100:")
            wrong()
            question6.destroy()
            answer6.destroy()
            button6.destroy()
            q7(right, wrong)
def q7(right, wrong):
    question7 = tk.Label(window, text="7. Какой цикл используется в программах, если количество повторов заранее неизвестно?\nВ ответ запишите ключевое слово оператора цикла", bg=bg, fg=fg)
    answer7 = tk.Entry(bg=bbg, fg=fg)
    button7 = tk.Button(window, text="Продолжить", command=lambda: tr7(q8, right, wrong), bg=bbg, fg=fg)
    question7.pack()
    answer7.pack()
    button7.pack()

    def tr7(q8, right, wrong):
        if answer7.get().lower() == "while":
            messagebox.showinfo("Верно!", "В pygame, например, можно использовать 'while True' для цикла работы программы")
            right()
            question7.destroy()
            answer7.destroy()
            button7.destroy()
            q8(right, wrong)
        else:
            messagebox.showerror("Неверно!", "Цикл, который можно задать, не зная количество повторов является while")
            wrong()
            question7.destroy()
            answer7.destroy()
            button7.destroy()
            q8(right, wrong)
def q8(right, wrong):
    question8 = tk.Label(window, text="8. Сколько раз будет выполнен этот цикл?\ni=4                                \nwhile i<12:                   \n     print('Привет!')\ni+=1              ", bg=bg, fg=fg)
    answer8 = tk.Entry(bg=bbg, fg=fg)
    button8 = tk.Button(window, text="Продолжить", command=lambda: tr8(q9, right, wrong), bg=bbg, fg=fg)
    question8.pack()
    answer8.pack()
    button8.pack()

    def tr8(q9, right, wrong):
        if answer8.get().lower() == "8":
            messagebox.showinfo("Верно!", "Привет!\nПривет!\nПривет!\nПривет!\nПривет!\nПривет!\nПривет!\nПривет!")
            right()
            question8.destroy()
            answer8.destroy()
            button8.destroy()
            q9(right, wrong)
        else:
            messagebox.showerror("Неверно!", "Цикл исполниться 8 раз, так как мы начинаем с 4, и заканчиваем цикл на 12.")
            wrong()
            question8.destroy()
            answer8.destroy()
            button8.destroy()
            q9(right, wrong)
def q9(right, wrong):
    question9 = tk.Label(window, text="9. Чему будет равно значение переменной 'a' после выполнения фрагмента программы?\na=10                                \nfor i in range(1,5):          \na-=i                    ", bg=bg, fg=fg)
    answer9 = tk.Entry(bg=bbg, fg=fg)
    button9 = tk.Button(window, text="Продолжить", command=lambda: tr9(q10, right, wrong), bg=bbg, fg=fg)
    question9.pack()
    answer9.pack()
    button9.pack()

    def tr9(q10, right, wrong):
        if answer9.get().lower() == "0":
            messagebox.showinfo("Верно!", "Нет слов одни эмоции")
            right()
            question9.destroy()
            answer9.destroy()
            button9.destroy()
            q10(right, wrong)
            
        else:
            messagebox.showerror("Неверно!", "Программа обнулит полностью значение a")
            wrong()
            question9.destroy()
            answer9.destroy()
            button9.destroy()
            q10(right, wrong)
def q10(right, wrong):
    question10 = tk.Label(window, text="10. Сколько раз будет распечатано число 5 в результате исполнения фрагмента алгоритма?\nfor i in range(5):              \nfor i in range(5):    \n  print(5,end='')", bg=bg, fg=fg)
    answer10 = tk.Entry(bg=bbg, fg=fg)
    button10 = tk.Button(window, text="Продолжить", command=lambda: tr10(end, right, wrong), bg=bbg, fg=fg)
    question10.pack()
    answer10.pack()
    button10.pack()

    def tr10(end, right, wrong):
        if answer10.get().lower() == "25":
            messagebox.showinfo("Верно!", "Это был последний вопрос!")
            right()
            question10.destroy()
            answer10.destroy()
            button10.destroy()
            end()
            
        else:
            messagebox.showerror("Неверно!", "Программа распечатает число 5 всего 25 раз. Считайте, что эти range перемножаются))")
            wrong()
            question10.destroy()
            answer10.destroy()
            button10.destroy()
            end()
def end():
    cresult()
    endtitle = tk.Label(window,text="Поздравляем!", font="Calibri 16", bg=bg, fg=fg)
    endsubtitle = tk.Label(window,text="Вы прошли викторину.", font="Calibri 14", bg=bg, fg=fg)
    endsubtitle2 = tk.Label(window, text="Результаты:", font="Calibri 14", bg=bg, fg=fg)
    endtext = tk.Label(window,text="Ваша оценка:", font="Calibri 14", bg=bg, fg=fg)
    endtext.place(x=100, y=170)
    resultl = tk.Label(window, textvariable=result, font='Calibri 14', bg=bg, fg=fg)
    resultl.place(x=220, y=170)
    endtitle.pack()
    endsubtitle.pack()
    endsubtitle2.pack()

window.mainloop()
