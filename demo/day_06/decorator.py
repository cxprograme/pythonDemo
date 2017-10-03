#-*-coding:utf-8-*-
def log(fun):
	# arg可变参数,kw是关键参数
	def wrapper(*args,**kw):
		print("call %s():" % fun.__name__);
		return fun(*args,**kw);
	return wrapper;
@log
def now():
	print('2017-09-20');

now();
