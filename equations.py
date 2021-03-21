def exponent (x):
    e=1
    counter=1
    denominator=1.0
    numerator=x
    for i in range(1, 100):
        e+=numerator/denominator
        counter+=1
        denominator*=counter
        numerator*=x
    return e  

def absolute (x):
    if x<0:
        x=-x
    return x

def Ln (x):
    ln=0
    epsilon=0.001
    while True:
        if x<=0:
            ln=0
        else:
            ln0=ln
            ln=ln+2*((x-exponent(ln))/(x+exponent(ln)))
            if absolute(ln0-ln)<epsilon:
                break
    return ln

def XtimesY (x, y):
    if x<=0:
        a=0.0
    else:
        result=exponent(y*Ln(x))  
        a=float('%0.6f' % result)
    return a

def sqrt (x, y):
    if y<=0 or x==0:
        sqrt=0.0
    else:
        sqrt=XtimesY(y, 1/x)
        sqrt=float('%0.6f' % sqrt)
    return sqrt

def calculate (x):
    final_result=exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
    final_result=float('%0.6f' % final_result)
    return final_result

                                                            
    
    



    













       


       


















