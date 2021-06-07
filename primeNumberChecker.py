'''
Program to check if a given number is PRIME or COMPOSITE

Definition of a prime number:
    Whole numbers greater than 1, that have only two factors – 1 and the number itself.
    eg: 1,2,3,5,7 ect

Definition of a composite number:
    Composite numbers can be defined as the whole numbers that have more than two factors.
    eg: 6,8,10,12 ect

'''
 
def main():	
    num = int(input('Enter a whole number\n'))
         
    if num > 1: 
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
         
            # If num is divisible by any number between    
            # 2 and n / 2, it is not prime
    
            if (num % i) == 0:
    
                print(f"{num}, is a COMPOSITE number")
                break
        else:
    
            print(f"{num}, is a PRIME number")
    
    x = input('Try again? Type yes or no\n').lower()
    if x == 'yes':
    	 main()
    else:
    	print('Done')	

main()