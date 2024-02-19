document.write("External <br>")

//case sensitive
var a=10
var A=20
var _a=30
var $a=40
var a1=50

document.write(a+'<br>')
document.write(A+'<br>')
document.write(_a+'<br>')
document.write($a+'<br>')
document.write(a1+'<br>')

// dynamically typed language

var a='Hello'
document.write(a+'<br>')

// Datatypes - numbers(with or without decimal)

var a=10
var b=10.00
document.write(typeof(a)+'<br>')
document.write(typeof(b)+'<br>')

// String - sequence of characters (single quotes or double quotes)

// boolean - true or false
document.write(a==b+'<br>')

// undefinded
var x;
document.write(typeof(x)+'<br>')
x=10
document.write(typeof(x)+'<br>')

// Operators
// Arithmatic Operator
var a=10
var b=20
document.write(a+b +'<br>')

// Addition, Substraction, Multiplication, Division
// modulus(remainder)

var a=10
var b=20
document.write(a%b +'<br>')

// increment, decrement

var a=10
var b=10
a++
document.write(a+'<br>') // 11
b--
document.write(b+'<br>') // 9

// comaparison Operator

var c=10
var d=20
var m=(d<=c)
var n=d>c
document.write(m+'<br>')
document.write(n+'<br>')

// ==  - only check value is same or not
var d=10
var e=10
var n=(d==e)
document.write(n+"<br>")

// ==  - cheeck whether datatype is also same or not
var d=10
var e='10'
var n=(d===e)
document.write(n+"<br>")

// Logical Operator

// AND --- T+T=T, T+F=F, F+T=F , F+F=T

var d=10
var e=30
document.write((d<e && d==20)+'<br>')

// OR --- T+T=T, T+F=T, F+T=T , F+F=F

var d=10
var e=30
document.write((d<e || d==20)+'<br>')

//logical not --- !(True)=False likewise

var d=10
var e=30
document.write(!(d<e || d==20)+'<br>')

// Assignment Operator
// =, += ,-=, *=, /=

var a=10
a+=20  //a=a+10
document.write(a+'<br>')

// if statement

// var a=10
// if (a>10)
// {
//     document.write('a is greater than 10'+'<br>')
// }
// else if (a==10)
// {
//     document.write("a is equal to 10 "+'<br>')
// }
// else
// {
//     document.write("a is less than 10"+'<br>')
// }

// // check if a number is odd or even
// a=11
// if (a%2==0)
// {
//     document.write(" a is even"+'<br>')
// }
// else{
//     document.write("a is odd"+'<br>')
// }

// Switch statement
// switch (expression)

var grade= 'C'
var result;
switch(grade)
{
    case 'A':
        result='Your grade is A'
        break
    case 'B':
        result='Your grade is B'
        break
    case 'C':
        result='Your grade is C <br>'
        break
    default:
        result="Invalid"
        break
}
document.write(result)

// Loop
// For loop
// syntax
// for(initialization, condition, increment/decrement)
// {
//    code to execute
// }

// for(var i=0;i<5;i++)
// {
//     // document.write('Helloworld <br>')
//     document.write(i+"<br>")
// }

// print numbers from 20-40 using for loop
// find sum of first 1-10 numbers using for loop
// print all even numbers from 1-20

// while loop
// while(condition)

// var i=1;
// while(i<=10)
// {
//     document.write(i+"<br>");
//     i++;
// }

// check a number is prime or not using while loop


// do while
var i=1;
do{
    document.write(i+"<br>");
    i++;
}
while(i<=5)


// Function
// Function Functionname()

// function newfunction()
// {
//     document.write('Good Morning <br>')
// }
// newfunction()
function newfunc(name, place)
{
    document.write(name +'<br>'+place +"<br>")
}

newfunc('Joe','zzz')
newfunc('Joe','zzz')
newfunc('Joe','zzz')

// find sum of 2 num using function
// find cube of a num using function(event)

function hello()
{
    return 'Helloworld'
}
document.write(hello())

// Array
var a = ['abc','def','ghi','xyz']
document.write(a+'<br>')
// access an item
document.write(a[0]+'<br>')
//replace an item
a[1]='uvw'
document.write(a+'<br>')
//add items to array
a[4]='jkl'
document.write(a+'<br>')
// length of array
document.write(a.length+'<br>')

// 3. array last element 

// add items to array using methods
a.push('aaa','bbb',12)
document.write(a+'<br>')

// delete element in array
a.splice(0,2)//(index,no of elements)
document.write(a+'<br>')

a.pop()
document.write(a+'<br>')

a.sort()
document.write(a+'<br>')

a.reverse()
document.write(a+'<br>')

// 4.using for loop print all values in an array


// string
a='Helloworld'
// document.write(a[0])   //H

// concat()
str1="Welcome"
document.write(str1.concat(a)+"<br>")
// document.write(str1.toUppercase()+"<br>")
document.write(str1.slice(1,4)+"<br>")
document.write(str1.slice(2,5)+"<br>")

// Math object
var a=10
document.write(Math.abs(a)+"<br>")
document.write(Math.sqrt(a)+"<br>")
// document.write(str1.pow(a,3)+"<br>") // 10*10*10   =10^3
document.write(Math.round(10.9999)+"<br>")
document.write(Math.min(100,28,444,33,2)+"<br>")
document.write(Math.max(100,28,444,33,2)+"<br>")

// JS Objects

emp={id:100,name:'ammu',age:10,place:"TVM"}
document.write(emp["name"])
// or
document.write(emp.age)

// Class 76

// Date Object

var date = new Date()//get current date and time
document.write(date + '<br>')

var dat = date.getDate();//30
document.write(dat + '<br>')

var mnth = date.getMonth()+1;//0-11
document.write(mnth + '<br>')

var yr = date.getFullYear()
document.write(yr + '<br>')
document.write(dat+'/'+mnth+'/'+yr)

// time
 
var time = new Date()
var hr = time.getHours();
var min = time.getMinutes();
document.write(hr+':'+min)

// Popup box
//alert
// alert('Hello')

// var a=10
// if (a>=20)
// {
//     alert('It"s greater')
// }
// else{
//     alert('It"s lesser')
// }

// function msg()
// {
//     alert('Welcome')
// }

// // Confirm()
// confirm('Are you sure?')

// var a;
// var c = confirm('Are you sure?')
// if (c == true)
// {
//     a = 'Pressed ok'
// }
// else {
//     a = 'pressed cancel'
// }
// document.write(a)

// // Prompt()

// prompt('Enter your name')

// function prom()
// {
//     var p = prompt('Enter your name')
//     alert('My name is '+p)
// }

// Regular Expression
// Syntax
//  /pattern/modifiers
// var p = /javascript/i
// Javascript is a pattern to search
// i is a modifier(case insensitive)

// search()-returns index position
// else -1
// var x = 'Javascript is easy'
// var y = x.search(/Is/i)
// document.write(y)

// test()-returns true if there is match else false
// var y = /Easssy/i
// var x = 'Javascript is easy'
// var z = y.test(x)
// document.write(z)

//match()-return arrays containing matches else return null
// var x = 'Javascript is easy is is'
// var y = /i/g //g:global-find all matching char in string
// var res = x.match(y)
// document.write(res)

//find any digits btw 0-5
// var x = 'Javascript4 is2 eas0y'
// var y = /[0-5]/g
// var res = x.match(y)
// document.write(res)

// find any of one value - |
// var x = 'Javascript4 is2 eas0y is is'
// var y = /[z|z]/g
// var res = x.match(y)
// document.write(res)


// find any character except a and s
// var x = 'Javascript4 is 2 eas0y'
// var y = /[^as]/g
// var res = x.match(y)
// document.write(res)

// Metacharacters
// var x = 'Javascript4 is2 eas0y'
// var y = /\d/g
// var res = x.match(y)
// document.write(res)

// var x = 'Javascript4 is2 eas0y'
// // var y = /\ba/ //beginning of word
// var y = /y\b/ // end of word
// var res = x.match(y)
// document.write(res)

// var x = 'Javascript4 @ #!is2 eas0y'
// // var y = /\w/g //word char(include nos and char)
// var y = /\W/g //@#!
// var res = x.match(y)
// document.write(res)

// Exception Handling
// try - test a block of code errors
// catch - handle errors
// throw - create custom errors
// finally - always execute

// try{
//     alert('Welcome')
//     throw Error()
// }
// catch{
//     document.write('error')
//     // alert('Error messsage')
// }
// finally{
//     document.write('Always execute') 
// }

//  Class-77

console.log('hello world')

// document.getElementById('one').innerHTML="Welcome to JS"