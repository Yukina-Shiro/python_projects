#outputs numbers from 1 to 100
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    else:
        return num

for n in range(1,100):
    print(fizz_buzz(n))

#I just earned the Halo Badge on Codédex! 