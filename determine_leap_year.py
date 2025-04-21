year=2024
if (year%4==0 and year%100!=0) or year%400==0:
    #1.赋值用==   2.if else for后面要跟:表示语句开始      3.取余用%
    print("year是闰年")
else:
    print("year不是闰年")
