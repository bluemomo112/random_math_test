import time,math,random,winsound
from multiprocessing import Process
# import turtle
from easygui import *

'''
倒数计时程序
'''

def count_dowm(limit_time):
    for i in range(limit_time):
        # winsound.Beep(500,100)
        time.sleep(1)
    winsound.Beep(1500, 500)

'''
利用gui的input来获取用户输入，因为如果利用主程序的input，将导致主程序堵塞。
而利用gui，则可以在主程判断是否已经到时间or输入完毕。
强制kill掉线程来完成继续主程序。
input无法被用在子线程中
本地文件储存分数信息（否则无法记录，会一直被覆盖）
'''
def get_input(question, right_ans):
    # t = turtle.Screen()
    # ans = t.numinput(question, "请输入该题答案：")
    ans=enterbox(question,"请输入该题答案")
    print("您输入的答案为：",ans,"正确答案为：",right_ans)

    try:
        ans=float(ans)
        with open("score.txt", "r") as f:
            score = int(f.read())

        if ans == right_ans:
            score += 1
            print("回答正确，当前分数为：", score)
            with open("score.txt", "w") as f:
                f.write(str(score))
        else:
            print("回答错误，该题不得分")

    except (ValueError,TypeError):
        print("请输入数字哦！该题错误，不得分。")



if __name__ == '__main__':

    questions_time = int(input("请输入您希望做的题目数量："))
    max = int(input("请输入您希望做的题目的最大数："))
    limit_time = int(input("请输入您希望做的每题的限制时间："))

    with open("score.txt", "w") as f:
        f.write(str(0))

    questions_type = ['+', '-', '*', '/']
    defualt_question = "题目 {} : {} {} {} = ? "

    '''
    随机题目
    '''

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

        '''
        开启计时程序
        '''
        p1 = Process(target=count_dowm,args=(limit_time,))
        p1.start()

        '''
        开启答题程序
        '''

        p2=Process(target=get_input,args=(question,right_ans,))
        p2.start()

        count_dowm_time=limit_time

        '''
        如果countdown程序还在运行的话，证明该题还有时间
        '''
        while p1.is_alive():
            print("剩余时间：",count_dowm_time)
            time.sleep(1)
            count_dowm_time-=1
            '''
            接着判断是否用户已经回答（如果回答，p2程序应该因为完成而中断了
            '''
            if p2.is_alive()==False:
                #如果完成输入，则kill掉计时线程，退出循环
                p1.terminate()
                break
        #如果退出时用户还未输入
        if p2.is_alive():
            print("时间已耗尽，该题不得分")
            p2.terminate()
        time.sleep(1.5)

















