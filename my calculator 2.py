#simple calculator
import time
print("my first calculator")
num1=float(input("enter first number : "))
num2=float(input("enter second number : "))
print("Operator choose:1.plus,2.minus,3.multiply,4.divided,5.percentage")
op=float(input())
if op<6:
	if op==1:
		print(num1,"+",num2,"=",num1+num2)
	elif op==2:
		print(num1,"-",num2,"=",num1-num2)
	elif op==3:
		print(num1,"*",num2,"=",num1*num2)
	elif op==4:
		print(num1,"/",num2,"=",num1/num2)
	elif op==5:
		xx=num2/100*num1
		print(num1,"%",num2,"=",num1-xx)
else:
	print("Error ! please check your Operators")
print()
print()
time.sleep(0.4)
print("               ধন্যবাদ আপনার দিনটি শুভ হোক")