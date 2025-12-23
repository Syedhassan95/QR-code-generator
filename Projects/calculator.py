while True:
    try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            print("Enter which operation you want to perform ")

            o = input("Enter operation ")

            match o:
                case "+":
                    print(f"the result is {a + b}")
    
                case "-":
                    print(f"the result is {a + b}")
            
                case "/":
                    print(f"the result is {a + b}")
        
                case "*":
                    print(f"the result is {a + b}")
    
                case default:
                    print("there are error" )
                    

    except Exception as e:
        print("error accured")


        



  



