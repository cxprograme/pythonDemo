# 可变参数
# def fun(*num):
# 	sum=0;
# 	for x in num:
# 		sum=sum+x*x;
# 	return sum;

# print(fun(*[1,2,3]));
# print(fun(1,2));
# 
# 关键字参数
# def fun(name,age,**kw):
# 	print('name:',name,'age',age,'other',kw);
# 	return kw;
# print(fun('cx',18,address='nantong')['address']);
# 


# 命名关键字 ，限制传入参数
# def fun(name,age,*,job,city):
# 	print(name,age,city,job);

# fun('cx',18,job='it',city='nantong')
# 
# 
def move(n, a, buffer, c):
    if(n == 1):
        print(a,"->",c)
        return
    move(n-1, a, c, buffer)
    move(1, a, buffer, c)
    move(n-1, buffer, a, c)
move(4, "a", "b", "c")