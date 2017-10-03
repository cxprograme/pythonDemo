import math;
# 一元二次方程
# def calformula(a,b,c):
# 	d=math.sqrt(b**2-4*a*c);
# 	x1=(-b+d)/(2*a);
# 	x2=(-b-d)/(2*a);
# 	return x1,x2;

# print(calformula(2, 3, 1));

# 默认参数 默认参数为不可变量
# def fun(x,n=2):
# 	sum=1;
# 	while n>0:
# 		sum=sum*x;
# 		n=n-1;
# 	return sum;

# print (fun(4,3));
# 
def info(name,address,age=6,classes='hundsun'):
	print('name:',name);
	print('address:', address);
	print('age:',age );
	print('class:',	 classes);
info('cx','南通');
