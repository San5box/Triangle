import math
import numpy as np
a=1
while (a<=1):
    a=a-1
    try: 
        x = int(input("A :"))
        z = int(input("B :"))
        y = int(input("C :"))
   
        ary = np.array([x,z,y])
        arrSorrt = np.sort(ary)
    
        if arrSorrt[0] > 0 and arrSorrt[2] <= 200 :
            for i in ary :
                ans = sum(ary)
            try:
            
                s = ans / 2
                result = math.sqrt((s*(s-x)*(s-z)*(s-y)))
           
                if result > 0 :
                    if arrSorrt[0] == arrSorrt[1] and arrSorrt[0] == arrSorrt[2] :
                        print("Equilateral")
                    elif arrSorrt[0] == arrSorrt[1] or arrSorrt[0] == arrSorrt[2] or arrSorrt[1] == arrSorrt[2] :
                        print("Isosceles")
                    else :
                        print("Scalene")

                else :
                    print("Not a tringle")
            except ValueError:
                print("Not a tringle")
        else : 
            print("Out of lenght")
    except ValueError:
        print("Error type input")
    print("==================================")
