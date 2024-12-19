#convert all functions below into python

# Write a method that accepts a name from the user and then returns it. Here’s the javascript:
# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };
def getName():
    name = input("What is your name? \n") 
    # print(f"Your name is {name}")
    return name

# getName()
# Write a method that reverses a string. Here’s the javascript:
# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverseIt():
    string = 'a man, a plan, a canal, frenemies!'
    reverse = ''
    count = 0
    for character in string:
        reverse += string[len(string) - (count +1)]
        count +=1
    print(reverse)
# reverseIt()

#Swapt the value of two variablesconst swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swapEm():
    a = 10
    b = 30
    temp = 0

    temp= b
    b=a
    a=temp
    print(f'a is now {a}, and b is now {b}')

# swapEm()

# mult all numbers in an array and return the final productconst multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;

def multiplyArray(ary):
    if len(ary) == 0:
        print(1)
    total=1
    
    for num in ary:
        total *= num
    # print(total)
    return total 

# multiplyArray([5,2,3])   


# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
    if(x%(3*5) == 0):
        print('fizzbuzz')
    elif(x%3 == 0):
        print('fizz')
    elif(x%5 == 0):
        print('buzz')
    else:
        print('archer')

# fizzbuzzer(15)
# fizzbuzzer(3)
# fizzbuzzer(5)
# fizzbuzzer(4)


#Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:


# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nthFibonacciNumber():
    fibs = [0, 1]
    num = input("Which fibonnaci number do you want?" )

    while len(fibs) < int(num):
        length = len(fibs)
        nextFib = fibs[length - 2] + fibs[length - 1]

        fibs.append(nextFib)
    
    print(fibs[len(fibs)-1], 'is the fibonacci number at position', num)

# nthFibonacciNumber()

#method that search an array/list for a value and returns tur/false depending on if it is pressent

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };
testArray = [5, 'moot', '42.5', 5]

def searchArray(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return True
    return False


# print(searchArray(testArray, '42.5'))

#Check if palindromeconst isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def isPalindrome(str): 
    
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str) -1 -i]:
            return False
        
    else:
        return True
    
# print(isPalindrome('Test'))


# Check if duplicates
# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def hasDupes(arr):
    obj={}
    for i in range(len(arr)):
        if arr[i] in obj:
            return True
        else:
            obj[arr[i]] = True;
    return False
        
# print(hasDupes(testArray))