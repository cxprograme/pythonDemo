# -*- coding: utf-8 -*-
# 切片
import os;
# print(list(range(100)[:10]));
# print (list(range(100)[::5]));
# 
# 
# 迭代
# d={'a',1,'b',2,'c',3};
# for k,v in d.items():
# 	print('key:',k,'value:',v);
# val=[x*x for x in range(1,11)];
# print(val);



# val1=[x*x for x in range(1,11) if x%2==0];
# print(val1);

# val2=[m+n for m in 'ABC' for n in 'def'];
# print(val2);

# print([d for d in os.listdir()]);

# L1 = ['Hello', 'World', 18, 'Apple', None];

# print ( [s.lower() for s in ['Hello', 'World', 18, 'Apple', None] if isinstance(s,str)] );

# for s in L1:
#  if isinstance(s,str):
#  	print(s.lower());
#  	
def fbi(max):
	n,a,b=0,0,1;
	while n < max:
		print(b);
		a,b=b,a+b;
		n=n+1;
	return 'done';
fbi(6);