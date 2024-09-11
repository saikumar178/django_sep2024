import math

number = int(input('Enter the number: '))

# Check if the square root of the number is an integer
if math.sqrt(number) == int(math.sqrt(number)):
    print('Number is a perfect square.')
else:
    print('Number is not a perfect square.')

# root=math.sqrt(N)
# floor_of_root=floor(root)
#if(floor_of_root*floor_of_root==N)
##   print('perfect sq')
