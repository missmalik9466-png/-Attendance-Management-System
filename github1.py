present =0
halfday=0
shortattendence=0
overtime=0
absent=0
for p in range(1,3):
    print("day=",p)
    for i in range(1,3):
        print("user = ", i)
        a=int(input("enter the morning time:"))
        b= int(input("enter the leaving time:"))
        if  a<0 or b>24 or b<a:
            print("not possible")
        elif a <= 8 and b ==18:
            print("present")
            present+=1
        
        elif a>=8 and b ==13 or a>=13 and b==18 :
            print("half day")
            halfday+=1
            
        elif a==b or a==0 or b==0:
            print("absent")
            absent+=1
           
        elif a>=8 and b<13 or  a>=13 or b<=18:
            print("short attdendence")
            shortattendence+=1
            
        elif a<=8 and b>18:
            print("overtime")
            overtime+=1
            
        else:
            print("invalid")


        print("present", present)
        print("halfday", halfday)
        print("absent", absent)
        print("shortattendence", shortattendence)
        print("overtime", overtime)

    
print("TOTAL present", present)
print("TOTAL halfday", halfday)
print("TOTAL absent", absent)
print("TOTAL shortattendence", shortattendence)
print("TOTAL overtime", overtime)
