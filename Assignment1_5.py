m1 = int(input("Enter marks of 1st subject: "))
m2 = int(input("Enter marks of 1st subject: "))
m3 = int(input("Enter marks of 1st subject: "))

avg = (m1+m2+m3)/3

if(avg >= 90 and avg <= 100):
    print("A")
elif(avg >= 80 and avg <= 89):
    print("B")
elif(avg >= 70 and avg <= 79):
    print("C")
elif(avg >= 60 and avg <= 69):
    print("D")
else:
    print("F")
