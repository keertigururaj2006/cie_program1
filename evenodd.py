numbers=list(map(int,input("Enter the number").split()))

even_count=0
odd_count=0
prime_count=0
for n in numbers:
    if n%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
        
        if n>1:
            for i in range (2,int(n*0.5)+1):
                if n%i==0:
                    break
                else:
                    prime_count=prime_count+1            
        
        print("Even numbers: ",even_count)
        print("Odd Numbers: ",odd_count)
        print("Prime Numbers: ",prime_count)