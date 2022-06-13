# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:38:27 2022

@author: kevin
"""


print("Hello World")


print("Hello python")
print("Hello world")

qq_number = "1234567"
qq_password = "123"

print(qq_number)
print(qq_password)

price = 8.5
weight = 7.5
money = price * weight
print(money)
#   money=4
money = money - 5 if money - 5 > 0 else money

print(money)
print(type(money))

# concatenated string
First_name = "Xue"
Last_name = "Kevin"

Full_name = First_name + " " + Last_name
print(Full_name)

print("_"*23)
''' 输入电话号
Tel = str(input("What's your telephone number?"))
print("Your telephone number " + Tel + str(type(Tel)))
'''
student_no=201207010246
print("我的名字叫 %s, 请多多关照。"%Full_name)
print("我的学号是%06d" %student_no)
print("苹果单价 %.02f 元/斤，购买%.02f斤，需要支付 %.02f元"%(price,weight,money))
print("_"*23)

import keyword

print(keyword.kwlist)

#if 语句
age=23
#age = input("How old are you?")

if age>18:
    print("You can enter the room")
else:
    print("You are not over 18 years old, Thanks for your patronage!")

holiday_name = "平安夜"

if holiday_name == "情人节":
    print("Gift is Rose. \n")
    print("Movie")
elif holiday_name == "平安夜":
    print("Gift is an apple.")
    print("Meal.")
elif holiday_name == "Birthday":
    print("Cake is the gift.")
else:
    print("Every day is festival.")

import random

print(random.randint(12,20))
i=1
while i<=5:
    print("这是第%d次"%i)
    i+=1
result=0
while i<100:
    if i % 2 == 0:
        print(i)
    i+=1
    result += i
print("Result = %d"%result)

i=1
while i<=5:
    j=i
    while j:
        print("*\n")
        j-=1
    print("")
    i+=1

row=1
while row<=5:
    print("*"*row)
    row+=1


#九九乘法表
row = 1
while row<=9:
    col = 1
    while col <= row:
        product = row*col
        print("%d * %d = %d\t" % (row, col, product))
        col += 1
    print("")
    row += 1

def print_Line(times):
    if times<=0:
        breakpoint()
    while times>0:
        print("*"*30)
        times -= 1

print_Line(3)


'''能够打印5行任意内容的分割线
'''

def print_line(char,times):
    print(str(char*times)+"\n")

print_line("Good",20)

def print_lines(char,times):
    row = 5
    while row>0:
        print(char*times)
        row-=1
    row = 5
    print("")
    while row>0:
        row -= 1
        while times>0:
            print(char*times)
            times-=1

print_lines("Great", 10)
print("")

#列表操作
name_list = ["zhangsan", "lisi", "wangwu"]
for i in name_list:
    print(i,end=("\t"))




#列表操作
name_list = ["zhangsan", "lisi", "wangwu"]
print(len(name_list))
print(name_list.count("zhangsan"))
for i in name_list:
    print(i)
name_list.sort(reverse="True")

'''
#元组
info_tuple = ("Zhangsan",18,1.75)
i = info_tuple.count(18)
print(i)
'''



