# Final Project
# CS 111, Hayes & Reckinger
# Code for CS-Life Game, based on day in the life of a CS student

import turtle
import random
import time

def successfully_game_completed_screen(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('win screen.gif')

def lose_screen() :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('lose screen.gif')

def tuesday_3_video_game(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('tuesday 3 option 2.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage -= random.randint(10,15)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage+=random.randint(15,20)
    elif difchosen==1:
        current_intellect_percentage += random.randint(10,15)
        current_health_percentage -= random.randint(15,25)
        current_sleep_percentage -= random.randint(20,30)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==2:
        current_intellect_percentage += random.randint(5,10)
        current_health_percentage -= random.randint(25,35)
        current_sleep_percentage -= random.randint(30,35)
        current_happiness_percentage+=random.randint(1,5)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_4)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def tuesday_3_attend_class(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('tuesday 3 option 1.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(5, 10)
        current_happiness_percentage-=random.randint(1,5)
    elif difchosen==1:
        current_intellect_percentage += random.randint(5,10)
        current_sleep_percentage -= random.randint(10,20)
        current_happiness_percentage-=random.randint(5,10)
    elif difchosen==2:
        current_intellect_percentage += random.randint(1,5)
        current_sleep_percentage -= random.randint(20,25)
        current_happiness_percentage-=random.randint(10,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_4)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def tuesday_3(x,y):
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('tuesday 3.gif')
    attend_class = turtle.Turtle()
    video_game = turtle.Turtle()
    turtle.addshape('Attend class.gif')
    turtle.addshape('Play Warzone.gif')
    attend_class.penup()
    attend_class.hideturtle()
    video_game.penup()
    video_game.hideturtle()
    attend_class.shape('Attend class.gif')
    video_game.shape('Play Warzone.gif')
    video_game.goto(-91, -313)
    attend_class.goto(82, -313)
    attend_class.showturtle()
    video_game.showturtle()
    video_game.onclick(tuesday_3_video_game)
    attend_class.onclick(tuesday_3_attend_class)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def tuesday_1_wake_up(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('tuesday 1 option 1.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(15,20)
        current_happiness_percentage -= random.randint(1,5)
    elif difchosen==1:
        current_intellect_percentage += random.randint(10,15)
        current_health_percentage += random.randint(10,15)
        current_sleep_percentage += random.randint(10,15)
        current_happiness_percentage -= random.randint(1,5)
    elif difchosen==2:
        current_intellect_percentage += random.randint(5,10)
        current_health_percentage += random.randint(5,10)
        current_sleep_percentage += random.randint(5,10)
        current_happiness_percentage -= random.randint(5,10)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_2)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()



def tuesday_1_sleep(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    randomnum = random.randint(1,100)
    if randomnum <= 85:
        s.bgpic('tuesday 1 option 2.gif')
        if difchosen==0:
            current_intellect_percentage += random.randint(10,15)
            current_health_percentage -= random.randint(1,5)
            current_sleep_percentage += random.randint(20,25)
            current_happiness_percentage+=random.randint(1,5)
        elif difchosen==1:
            current_intellect_percentage += random.randint(5,10)
            current_health_percentage -= random.randint(5,15)
            current_sleep_percentage += random.randint(10,20)
            current_happiness_percentage+=random.randint(1,5)
        elif difchosen==2:
            current_intellect_percentage += random.randint(1,5)
            current_health_percentage -= random.randint(15,20)
            current_sleep_percentage += random.randint(1,10)
            current_happiness_percentage+=random.randint(1,5)
        next_1 = turtle.Turtle()
        turtle.addshape('NEXT.gif')
        next_1.shape('NEXT.gif')
        next_1.hideturtle()
        next_1.penup()
        next_1.goto(-3, -310)
        next_1.showturtle()
        next_1.onclick(monday_2)
    else:
        s.bgpic('bedroom monday 1 option 2.gif')
        if difchosen==0:
            current_intellect_percentage -= random.randint(15,20)
            current_health_percentage -= random.randint(10,15)
            current_sleep_percentage += random.randint(25,30)
            current_happiness_percentage-=random.randint(1,5)
        elif difchosen==1:
            current_intellect_percentage -= random.randint(20,25)
            current_health_percentage -= random.randint(15,25)
            current_sleep_percentage += random.randint(15,25)
            current_happiness_percentage-=random.randint(5,10)
        elif difchosen==2:
            current_intellect_percentage -= random.randint(25,35)
            current_health_percentage -= random.randint(20,30)
            current_sleep_percentage += random.randint(10,15)
            current_happiness_percentage-=random.randint(10,15)
        next_1 = turtle.Turtle()
        turtle.addshape('NEXT.gif')
        next_1.shape('NEXT.gif')
        next_1.hideturtle()
        next_1.penup()
        next_1.goto(-3, -310)
        next_1.showturtle()
        next_1.onclick(monday_2)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def tuesday_1() :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('Bedroom monday 1.gif')
    sleep = turtle.Turtle()
    wake_up = turtle.Turtle()
    turtle.addshape('Sleep.gif')
    turtle.addshape('Wake up.gif')
    wake_up.penup()
    wake_up.hideturtle()
    sleep.penup()
    sleep.hideturtle()
    sleep.shape('Sleep.gif')
    wake_up.shape('Wake up.gif')
    sleep.goto(-91, -313)
    wake_up.goto(82, -313)
    sleep.showturtle()
    wake_up.showturtle()
    wake_up.onclick(tuesday_1_wake_up)
    sleep.onclick(tuesday_1_sleep)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_5_party(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 5 option 1.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(1,15)
        current_health_percentage -= random.randint(5,15)
        current_sleep_percentage += random.randint(20,40)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(5,15)
        current_health_percentage -= random.randint(10,15)
        current_sleep_percentage += random.randint(10,40)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(10,15)
        current_health_percentage -= random.randint(10,20)
        current_sleep_percentage += random.randint(10,30)
        current_happiness_percentage+=random.randint(10,20)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    text.write('END OF DAY!', font = ('Times New Roman', 25, 'bold'))
    count_day += 1
    if count_day == 6 :
        next_1.onclick(successfully_game_completed_screen)
    else :
        next_1.onclick(game_start_easy)
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_5_sleep(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 5 option 3.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(1,10)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(20,40)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage += random.randint(1,10)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(30,40)
        current_happiness_percentage+=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage += random.randint(1,5)
        current_health_percentage += random.randint(10,20)
        current_sleep_percentage += random.randint(20,50)
        current_happiness_percentage+=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    text.write('END OF DAY!', font = ('Times New Roman', 25, 'bold'))
    count_day += 1
    if count_day == 6 :
        next_1.onclick(successfully_game_completed_screen)
    else :
        next_1.onclick(game_start_easy)
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_5_study(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 5 option 2.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(10,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(20,30)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage += random.randint(10,20)
        current_health_percentage += random.randint(10,20)
        current_sleep_percentage += random.randint(20,40)
        current_happiness_percentage+=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage += random.randint(10,25)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(10,50)
        current_happiness_percentage+=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    text.write('END OF DAY!', font = ('Times New Roman', 25, 'bold'))
    count_day += 1
    if count_day == 6 :
        next_1.onclick(successfully_game_completed_screen)
    else :
        next_1.onclick(game_start_easy)
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_5(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 5.gif')
    party = turtle.Turtle()
    study = turtle.Turtle()
    sleep = turtle.Turtle()
    turtle.addshape('Sleep on time.gif')
    turtle.addshape('Study Late.gif')
    turtle.addshape('Party.gif')
    party.penup()
    party.hideturtle()
    study.penup()
    study.hideturtle()
    sleep.penup()
    sleep.hideturtle()
    sleep.shape('Sleep on time.gif')
    party.shape('Party.gif')
    study.shape('Study Late.gif')
    sleep.goto(-183, -313)
    study.goto(0, -313)
    party.goto(168, -313)
    sleep.showturtle()
    party.showturtle()
    study.showturtle()
    party.onclick(monday_5_party)
    study.onclick(monday_5_study)
    sleep.onclick(monday_5_sleep)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_4_work_out(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 4 option 2.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(1,5)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(5,10)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(1,10)
        current_health_percentage += random.randint(10,20)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage+=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(1,10)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(15,25)
        current_happiness_percentage+=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_5)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_4_hang_out(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 4 option 1.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(1,5)
        current_health_percentage += random.randint(1,5)
        current_sleep_percentage -= random.randint(10,15)
        current_happiness_percentage+=random.randint(10,20)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(1,10)
        current_health_percentage += random.randint(1,5)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage+=random.randint(5,10)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(1,15)
        current_health_percentage += random.randint(1,5)
        current_sleep_percentage -= random.randint(15,25)
        current_happiness_percentage+=random.randint(1,10)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_5)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_4(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 4.gif')
    hangout= turtle.Turtle()
    workout = turtle.Turtle()
    turtle.addshape('Hang out with friends.gif')
    turtle.addshape('Work Out and Dinner.gif')
    workout.penup()
    workout.hideturtle()
    hangout.penup()
    hangout.hideturtle()
    hangout.shape('Hang out with friends.gif')
    workout.shape('Work Out and Dinner.gif')
    workout.goto(163, -313)
    hangout.goto(-166, -313)
    hangout.showturtle()
    workout.showturtle()
    workout.onclick(monday_4_work_out)
    hangout.onclick(monday_4_hang_out)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_3_assignments(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 3 option 1.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage -= random.randint(1,5)
        current_sleep_percentage -= random.randint(5,10)
        current_happiness_percentage-=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage += random.randint(10,20)
        current_health_percentage -= random.randint(1,5)
        current_sleep_percentage -= random.randint(5,20)
        current_happiness_percentage-=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage += random.randint(5,20)
        current_health_percentage -= random.randint(1,5)
        current_sleep_percentage -= random.randint(5,20)
        current_happiness_percentage-=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_4)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()

def monday_3_insta(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 3 option 3.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(5,10)
        current_health_percentage -= random.randint(15,20)
        current_sleep_percentage -= random.randint(1,5)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(10,15)
        current_health_percentage -= random.randint(10,20)
        current_sleep_percentage -= random.randint(5,10)
        current_happiness_percentage+=random.randint(15,20)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(10,20)
        current_health_percentage -= random.randint(15,20)
        current_sleep_percentage -= random.randint(5,15)
        current_happiness_percentage+=random.randint(15,25)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_4)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()

def monday_3_binge(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 3 option 2.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(5,10)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(5,10)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(10,15)
        current_health_percentage += random.randint(10,20)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage+=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(10,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(15,25)
        current_happiness_percentage+=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_4)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()

def monday_3(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 3.gif')
    binge = turtle.Turtle()
    insta = turtle.Turtle()
    study = turtle.Turtle()
    turtle.addshape('Binge-Watch.gif')
    turtle.addshape('Scroll Insta.gif')
    turtle.addshape('study.gif')
    binge.penup()
    binge.hideturtle()
    insta.penup()
    insta.hideturtle()
    study.penup()
    study.hideturtle()
    binge.shape('Binge-Watch.gif')
    insta.shape('Scroll Insta.gif')
    study.shape('study.gif')
    study.goto(-183, -313)
    insta.goto(228, -313)
    binge.goto(0, -313)
    study.showturtle()
    insta.showturtle()
    binge.showturtle()
    study.onclick(monday_3_assignments)
    binge.onclick(monday_3_binge)
    insta.onclick(monday_3_insta)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()



def monday_2_lunch(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 2 option 1.gif')
    if difchosen==0:
        current_intellect_percentage -= random.randint(5,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(5,10)
        current_happiness_percentage+=random.randint(10,15)
    elif difchosen==1:
        current_intellect_percentage -= random.randint(15,20)
        current_health_percentage += random.randint(10,20)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage+=random.randint(5,15)
    elif difchosen==2:
        current_intellect_percentage -= random.randint(15,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage -= random.randint(15,25)
        current_happiness_percentage+=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    if count_day%2!=0:
        next_1.onclick(monday_3)
    elif count_day%2==0:
        next_1.onclick(tuesday_3)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()
    


def monday_2_skip_lunch(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 2 option 2.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage -= random.randint(5,15)
        current_sleep_percentage -= random.randint(5,15)
        current_happiness_percentage-=random.randint(1,5)
    elif difchosen==1:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage -= random.randint(15,20)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage-=random.randint(1,10)
    elif difchosen==2:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage -= random.randint(15,25)
        current_sleep_percentage -= random.randint(15,20)
        current_happiness_percentage-=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    if count_day%2!=0:
        next_1.onclick(monday_3)
    elif count_day%2==0:
        next_1.onclick(tuesday_3)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()

def monday_2(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('monday 2.gif')
    lunch = turtle.Turtle()
    study = turtle.Turtle()
    turtle.addshape('Have delicious lunch.gif')
    turtle.addshape('Skip lunch and study.gif')
    lunch.penup()
    lunch.hideturtle()
    study.penup()
    study.hideturtle()
    lunch.shape('Have delicious lunch.gif')
    study.shape('Skip lunch and study.gif')
    lunch.goto(-150, -313)
    study.goto(150, -313)
    study.showturtle()
    lunch.showturtle()
    lunch.onclick(monday_2_lunch)
    study.onclick(monday_2_skip_lunch)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_1_wake_up(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('classroom monday 1 option 1.gif')
    if difchosen==0:
        current_intellect_percentage += random.randint(20,25)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(15,20)
        current_happiness_percentage-=random.randint(1,5)
    elif difchosen==1:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage += random.randint(15,20)
        current_sleep_percentage += random.randint(10,20)
        current_happiness_percentage-=random.randint(1,10)
    elif difchosen==2:
        current_intellect_percentage += random.randint(15,20)
        current_health_percentage += random.randint(5,20)
        current_sleep_percentage += random.randint(5,20)
        current_happiness_percentage-=random.randint(1,15)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    next_1 = turtle.Turtle()
    turtle.addshape('NEXT.gif')
    next_1.shape('NEXT.gif')
    next_1.hideturtle()
    next_1.penup()
    next_1.goto(-3, -310)
    next_1.showturtle()
    next_1.onclick(monday_2)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def monday_1_sleep(x, y) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    randomnum = random.randint(1,100)
    if randomnum <= 85:
        s.bgpic('classroom monday 1 option 2.gif')
        if difchosen==0:
            current_intellect_percentage += random.randint(15,25)
            current_health_percentage -= random.randint(15,20)
            current_sleep_percentage += random.randint(20,25)
            current_happiness_percentage-=random.randint(1,5)
        elif difchosen==1:
            current_intellect_percentage += random.randint(15,20)
            current_health_percentage -= random.randint(10,15)
            current_sleep_percentage += random.randint(15,25)
            current_happiness_percentage-=random.randint(1,10)
        elif difchosen==2:
            current_intellect_percentage += random.randint(10,15)
            current_health_percentage -= random.randint(15,25)
            current_sleep_percentage += random.randint(10,15)
            current_happiness_percentage-=random.randint(1,15)
        next_1 = turtle.Turtle()
        turtle.addshape('NEXT.gif')
        next_1.shape('NEXT.gif')
        next_1.hideturtle()
        next_1.penup()
        next_1.goto(-3, -310)
        next_1.showturtle()
        next_1.onclick(monday_2)
    else:
        s.bgpic('bedroom monday 1 option 2.gif')
        if difchosen==0:
            current_intellect_percentage-=random.randint(10,15)
            current_health_percentage -= random.randint(20,25)
            current_sleep_percentage += random.randint(25,30)
            current_happiness_percentage-=random.randint(1,5)
        elif difchosen==1:
            current_intellect_percentage-=random.randint(10,20)
            current_health_percentage -= random.randint(15,20)
            current_sleep_percentage += random.randint(20,25)
            current_happiness_percentage-=random.randint(1,10)
        elif difchosen==2:
            current_intellect_percentage-=random.randint(15,25)
            current_health_percentage -= random.randint(10,15)
            current_sleep_percentage += random.randint(25,30)
            current_happiness_percentage-=random.randint(1,15)
        next_1 = turtle.Turtle()
        turtle.addshape('NEXT.gif')
        next_1.shape('NEXT.gif')
        next_1.hideturtle()
        next_1.penup()
        next_1.goto(-3, -310)
        next_1.showturtle()
        next_1.onclick(monday_2)
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def make_status_bar(percentage, start_x, start_y, color) :
    status_bar = turtle.Turtle()
    status_bar.hideturtle()
    length = 150
    width = 25
    status_bar.width(3)
    status_bar.speed(5000)
    status_bar.penup()
    status_bar.setheading(0)
    status_bar.penup()
    status_bar.goto(start_x, start_y)
    status_bar.pendown()
    status_bar.pencolor('black')
    status_bar.forward(length)
    status_bar.right(90)
    status_bar.forward(width)
    status_bar.right(90)
    status_bar.forward(length)
    status_bar.right(90)
    status_bar.forward(width)
    status_bar.right(90)
    status_bar.fillcolor(color)
    status_bar.begin_fill()
    status_bar.forward((percentage/100)*length)
    status_bar.right(90)
    status_bar.forward(width)
    status_bar.right(90)
    status_bar.forward((percentage/100)*length)
    status_bar.right(90)
    status_bar.forward(width)
    status_bar.right(90)
    status_bar.end_fill()
    status_bar.penup()
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(start_x - 10, start_y - ((4*width)/3))
    text.pencolor('white')
    text.speed(5000)
    if color == "yellow" :
        text.write("Happiness", align = "right", font = ("Arial", 18, "bold"))
    if color == "red" :
        text.write("Health", align = "right", font = ("Arial", 18, "bold"))
    if color == "green" :
        text.write("Intellect", align = "right", font = ("Arial", 18, "bold"))
    if color == "blue" :
        text.write("Sleep", align = "right", font = ("Arial", 18, "bold"))
    

def monday_1() :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen, count_day
    s.clearscreen()
    s.bgpic('Bedroom monday 1.gif')
    if current_intellect_percentage >= 100 :
        current_intellect_percentage = 100
    if current_health_percentage >= 100 :
        current_health_percentage = 100
    if current_sleep_percentage >= 100 :
        current_sleep_percentage = 100
    if current_happiness_percentage >= 100 :
        current_happiness_percentage = 100
    make_status_bar(current_health_percentage, 200, 290, "red")
    make_status_bar(current_intellect_percentage, 200, 255, "green")
    make_status_bar(current_happiness_percentage, 200, 220, "yellow")
    make_status_bar(current_sleep_percentage, 200, 185, "blue")
    sleep = turtle.Turtle()
    wake_up = turtle.Turtle()
    turtle.addshape('Sleep.gif')
    turtle.addshape('Wake up.gif')
    wake_up.penup()
    wake_up.hideturtle()
    sleep.penup()
    sleep.hideturtle()
    sleep.shape('Sleep.gif')
    wake_up.shape('Wake up.gif')
    sleep.goto(-91, -313)
    wake_up.goto(82, -313)
    sleep.showturtle()
    wake_up.showturtle()
    wake_up.onclick(monday_1_wake_up)
    sleep.onclick(monday_1_sleep)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(-80, 300)
    text.pencolor('white')
    days_lst = ['MONDAY', 'TUESDAY', 'WEDNESDAY', "THURSDAY", 'FRIDAY']
    if count_day <= 5 :
        text.write(days_lst[count_day - 1], font = ('Times New Roman', 30, 'bold'))
    if current_happiness_percentage <= 0 or current_health_percentage <= 0 or current_intellect_percentage <= 0 or current_sleep_percentage <= 0 :
        lose_screen()


def game_start_easy(x, y) :
    global difchosen
    global current_happiness_percentage
    global current_health_percentage
    global current_intellect_percentage
    global current_sleep_percentage
    global count
    global count_day
    difchosen = 0
    s.clearscreen()
    if count_day == 1 :
        s.bgpic('instructions.gif')
        loading=turtle.Turtle()
        turtle.addshape('loading.gif')
        loading.hideturtle()
        loading.shape('loading.gif')
        loading.penup()
        loading.goto(-720,-310)
        loading.showturtle()
        name=open('names.txt')
        name=name.readlines()
        name_lst=list()
        for i in name:
            name_lst.append(i[:-1])
        randomnum=random.randint(0,len(name_lst)-1)
        txt=turtle.Turtle()
        txt.hideturtle()
        txt.pencolor('White')
        txt.penup()
        txt.goto(0,-50)
        txt.pendown()
        txt.write('YOUR NAME IS '+name_lst[randomnum].upper(),font=('Arial',17,'bold'),align='center')
        for i in range(-720,0,10):
            loading.goto(i,-310)
            time.sleep(0.1)
    if count_day%2!=0 and count<=5:
        monday_1()
        count+=1
    elif count_day%2==0 and count<=5:
        tuesday_1()
        count+=1
    

def game_start_medium(x, y) :
    global difchosen
    global current_happiness_percentage
    global current_health_percentage
    global current_intellect_percentage
    global current_sleep_percentage
    global count
    global count_day
    difchosen = 1
    current_health_percentage = random.randint(80, 90)
    current_intellect_percentage = random.randint(70, 90)
    current_happiness_percentage = random.randint(70, 90)
    current_sleep_percentage = random.randint(80, 90)
    s.clearscreen()
    if count_day == 1 :
        s.bgpic('instructions.gif')
        loading=turtle.Turtle()
        turtle.addshape('loading.gif')
        loading.hideturtle()
        loading.shape('loading.gif')
        loading.penup()
        loading.goto(-720,-310)
        loading.showturtle()
        name=open('names.txt')
        name=name.readlines()
        name_lst=list()
        for i in name:
            name_lst.append(i[:-1])
        randomnum=random.randint(0,len(name_lst)-1)
        txt=turtle.Turtle()
        txt.pencolor('White')
        txt.penup()
        txt.goto(0,-50)
        txt.pendown()
        txt.write('YOUR NAME IS '+name_lst[randomnum].upper(),font=('Arial',17,'bold'),align='center')
        for i in range(-720,0,10):
            loading.goto(i,-310)
            time.sleep(0.1)
    if count == 1:
        game_start(current_health_percentage, current_intellect_percentage, current_happiness_percentage, current_sleep_percentage)
    if count_day%2!=0 and count<=5:
        monday_1()
        count+=1
    elif count_day%2==0 and count<=5:
        tuesday_1()
        count+=1


def game_start_hard(x, y) :
    global difchosen
    global current_happiness_percentage
    global current_health_percentage
    global current_intellect_percentage
    global current_sleep_percentage
    global count
    global count_day
    difchosen = 2
    current_health_percentage = random.randint(50, 60)
    current_intellect_percentage = random.randint(50, 60)
    current_happiness_percentage = random.randint(50, 60)
    current_sleep_percentage = random.randint(70, 80)
    s.clearscreen()
    if count_day == 1 :
        s.bgpic('instructions.gif')
        loading=turtle.Turtle()
        turtle.addshape('loading.gif')
        loading.hideturtle()
        loading.shape('loading.gif')
        loading.penup()
        loading.goto(-720,-310)
        loading.showturtle()
        name=open('names.txt')
        name=name.readlines()
        name_lst=list()
        for i in name:
            name_lst.append(i[:-1])
        randomnum=random.randint(0,len(name_lst)-1)
        txt=turtle.Turtle()
        txt.pencolor('White')
        txt.penup()
        txt.goto(0,-50)
        txt.pendown()
        txt.write('YOUR NAME IS '+name_lst[randomnum].upper(),font=('Arial',17,'bold'),align='center')
        for i in range(-720,0,10):
            loading.goto(i,-310)
            time.sleep(0.1)
    if count == 1:
        game_start(current_health_percentage, current_intellect_percentage, current_happiness_percentage, current_sleep_percentage)
    if count_day%2!=0 and count<=5:
        monday_1()
        count+=1
    elif count_day%2==0 and count<=5:
        tuesday_1()
        count+=1


def game_start(health_start_percentage, intellect_start_percentage, happiness_start_percentage, sleep_start_percentage) :
    global current_health_percentage, current_happiness_percentage, current_intellect_percentage, current_sleep_percentage, count, difchosen
    s.clearscreen()
    make_status_bar(health_start_percentage, 200, 290, "red")
    make_status_bar(intellect_start_percentage, 200, 255, "green")
    make_status_bar(happiness_start_percentage, 200, 220, "yellow")
    make_status_bar(sleep_start_percentage, 200, 185, "blue")


def difficulty_screen(x, y) :
    prompt = turtle.Turtle()
    prompt.hideturtle()
    prompt.shape('prompt page.gif')
    prompt.penup()
    prompt.goto(-135, 125)
    prompt.showturtle()
    difficulty = turtle.Turtle()
    easy = turtle.Turtle()
    medium = turtle.Turtle()
    hard = turtle.Turtle()
    turtle.addshape('Easy.gif')
    turtle.addshape('Medium.gif')
    turtle.addshape('Hard.gif')
    turtle.addshape('Difficulty.gif')
    difficulty.shape('Difficulty.gif')
    difficulty.hideturtle()
    easy.hideturtle()
    medium.hideturtle()
    hard.hideturtle()
    difficulty.penup()
    easy.penup()
    medium.penup()
    hard.penup()
    easy.shape("Easy.gif")
    medium.shape("Medium.gif")
    hard.shape("Hard.gif")
    difficulty.goto(-135, 220)
    easy.goto(-190, 170)
    medium.goto(-175, 120)
    hard.goto(-190, 70)
    difficulty.showturtle()
    easy.showturtle()
    medium.showturtle()
    hard.showturtle()
    easy.onclick(game_start_easy)
    medium.onclick(game_start_medium)
    hard.onclick(game_start_hard)


count=1
count_day = 1

t = turtle.Turtle()
size = 720
s = turtle.getscreen()
s.setup(size + 10, size + 10)
s.screensize(size, size)


s.bgpic("title screen.gif")

play = turtle.Turtle()
turtle.addshape("play.gif")
play.shape("play.gif")
play.hideturtle()
play.penup()
play.goto(-67, -48)
play.showturtle()

current_health_percentage = random.randint(90, 100)
current_intellect_percentage = random.randint(80, 100)
current_happiness_percentage = random.randint(80, 100)
current_sleep_percentage = random.randint(90, 100)


turtle.addshape("prompt page.gif")

play.onclick(difficulty_screen)

turtle.mainloop()
s.tracer(False)

def new_screen(x, y) :
    s.clearscreen()

turtle.mainloop()