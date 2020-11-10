print("Following Exceptions can be handle here")
print("1.ZeroDivision Error")
print("2.TypeError")
print("3.ValueError")
print("4.NameError")
print("5.IOError")
print("6.IndexError")
print("Any other number to exist")
while(1):
    choice = int(input("Enter your choice from above list related to error you want to handle:"))
    try:
        if(choice == 1):
            a = int(input("Enter integer number1:"))
            b = int(input("Enter integer number2:"))
            c = a/b
            print("Division of",a,"by", b, "gives value",c)
            print("No error occur")
        elif(choice == 2):
            d = int(input("Enter Integer value:"))
            m = input("Enter any type of data you want:")
            f = d + m
            print("Addition of %s & %s gives %s",(d, m, f))
            print("No error occur")
        elif(choice == 3):
            n = float(input("Enter your value as float:"))
            print("Your Entered value is", n,"Which is corect")
            print("No error occur")
        elif(choice == 4):
            rash = input("Enter value to be printed:")
            print(rashmi)
            print("No error occur")
        elif(choice == 5):
            import sys
            def what():
                print("We try to open file fun.txt")
                f = open("fun.txt", 'r')
                print("No error occur")
            what()
        elif(choice == 6):
                mood = ['happy', 'sad', 'good']
                for j in range(4):
                    print(mood[j])
        else:
            break
    except ZeroDivisionError as e:
        print("Hey, Division by Zero to any number cant be Takes place")
        print("It gives ZeroDivisionError")
    except TypeError as e:
        print("Addition is unsupported operator for enter two values",d ,"&", m)
        print("python will give TypeError to you")
    except ValueError as e:
        print("Hey You entered wrong Input. It must be float")
        print("python will give ValueError to you")
    except NameError as e:
        print("This is not your fault I took wronge variable which is not exist in program to print")
        print("python will give NameError to you")
    except IOError as e:
        print("Input/Output Operation on a file must be Fail")
        print("python will giveIOError to you")
    except IndexError as e:
        print("You are Trying to acces indes wich is out of range")
        print("python will give you IndexError to you")
    finally:
        print("Yes..!! We successfully handle error")