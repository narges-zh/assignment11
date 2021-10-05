weight = float(input("please enter youre weight :"))
height = float(input("please enter your height:"))
BMI=weight/(height*height)

if BMI<18.5 :
    print("youre BMI is" , BMI , "youre underweight")

    if 18.5<=BMI<24.9 :
        print("youre BMI is " , BMI , "youre normal")

        if 25<BMI<29.9 :
            print("youre BMI is " , BMI , "youre overweight")

            if 30<BMI<34.9 :
                print("youre BMI is" , BMI , "youre obese")

                if BMI>=35 :
                    print("youre BMI is" , BMI , "youre extremly obese")


