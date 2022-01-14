import allindexs
def prime_checker(number) :
    if number==1 :
        print('Neither prime nor composite')
    else:
         
        list=[]   
        for i in range(2,number):
            a= number % i
            list.append(str(a))    

        if '0' in list:
          print("It's not a prime number.")
          print(f"It is divisible by the following number/s  \n{','.join(allindexs.allindexs(list,'0'))}")

        else:
          print("It's a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)



