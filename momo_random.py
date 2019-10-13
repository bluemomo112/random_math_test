import time,math,random,winsound
from multiprocessing import Process
import turtle

def count_dowm(limit_time):
    t = turtle.Turtle()
    for i in range(limit_time):
        # print(kwargs)
        t.write(str(i),font=("Arial",20,"normal"))
        time.sleep(1)
        t.clear()

def get_input():
    screen=turtle.Screen()
    screen.numinput("输入答案窗口","请输入答案:")

if __name__ == '__main__':

    # questions_time = int(input("请输入您希望做的题目数量："))
    # max = int(input("请输入您希望做的题目的最高位数："))
    # limit_time = int(input("请输入您希望做的每题的限制时间："))

    questions_time=10
    max=10
    limit_time=10

    questions_type = ['+', '-', '*', '/']
    defualt_question = "题目{}:{} {} {} = ? "
    score = 0
    ans_fini = False

    for i in range(questions_time):
        print("第",i,"题")
        a=random.randint(0,max)
        b = random.randint(0,max)
        qType=random.choice(questions_type)

        if qType=="+":
            right_ans=a+b
        elif qType=="-":
            right_ans=a-b
        elif qType=="*":
            right_ans=a*b
        else:
            b = random.randint(1,max) if b ==0 else b
            right_ans=a/b
        question = defualt_question.format(i, a, qType, b)
        print(question)

        p1 = Process(target=count_dowm,args=(limit_time,))
        p1.start()

        user_ans = int(input("请输入您的答案："))
        while user_ans != right_ans and p1.is_alive()==True:
            user_ans = int(input("请输入您的答案："))

        if user_ans==right_ans:
            score+=1
            print("回答正确，目前分数为：",score)
        else:
            print("时间耗尽，该题不得分")


















