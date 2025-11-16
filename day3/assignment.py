name = input("enter your name  ")
score = int(input("enter your score  "))

departments = ("choose your departments: \n law\n medicine and surgery\n food and nutrition\ncomputer science\n home management\n"
"nursing \naccounting\nbusiness admin\nlinguistics\nfashion designing")
print(departments)

departments = input("")

if departments == "law" :
    if score > 300:
       print("congrats u made it")
    elif score <= 300:
        print("oops! u failed try harder next time") 

elif departments =="medicine and surgery":
            if score >= 350:
                print("congrats u made it")
            elif score <= 350:
                print("oops! u failed read harder next time")

elif departments =="food and nutrition":
            if score >= 280:
                print("congrats u made it")
            elif score <= 280:
                print("oops! u failed, see u next time")
        
elif departments =="computer science":
            if score >= 290:
                print("congrats u made it")
            elif score <= 290:
                print("oops! u failed read harder next time")

elif departments =="home management":
            if score >= 270:
                print("congrats u made it")
            elif score <= 270:
                print("oops! u failed try harder next time")
        
elif departments =="nursing":
            if score >= 330:
                print("congrats u made it")
            elif score <= 330:
                print("oops! u failed read harder next time")

elif departments =="accounting":
            if score >= 250:
                print("congrats u made it")
            elif score <= 250:
                print("oops! u failed see you next time")

elif departments =="business admin":
            if score >= 220:
                print("congrats u made it")
            elif score <= 220:
                print("oops! u failed read harder next time")

elif departments =="linguistics":
            if score >= 400:
                print("congrats u made it")
            elif score <= 400:
                print("oops! u failed try harder next time")

elif departments =="fashion designing":
            if score >= 200:
                print("congrats u made it")
            elif score <= 200:
                print("oops! u failed read harder next time")
            else: 
             print("invalid departments choose again")
    