studenList=[]
newName='';
newPhone='';
newAge='';
def getInfo():
	global newAge;
	global newPhone;
	global newName;
	newName=input("请输入学生信息:");
	newAge=input("请输入学生年龄:");
	newPhone=input("请输入电话号码:");
def start():
	# 学生管理系统
	print('===========学生管理系统=======');
	print('1.添加学生信息');
	print('2.修改学生信息');
	print('3.删除学生信息');
	print('4.显示学生信息');
	print('5.退出');
	print('==============================');
def addStudentInfo():
	# 添加学生信息
	getInfo();
	studeninfo={};
	studeninfo['name']=newName;
	studeninfo['age']=newAge;
	studeninfo['phone']=newPhone;
	studenList.append(studeninfo);
def modifyStudenInfo():
	stuId=input("请输入学生序号：");
	getInfo();
	studenList[int(stuId)-1]['name']=newName;
	studenList[int(stuId)-1]['age']=newAge;
	studenList[int(stuId)-1]['phone']=newPhone;
def deleteStudentInfo():
	stuId=input("输入需要删除的学生序号");
	studenList.remove(studenList[int(stuId)-1]);
def listStudenInfo():
	print('序号	姓名	年龄	电话号码');
	i=1;
	for x in studenList:
		print("%d 	%s 	%s 	%s" %(i,x['name'],x['age'],x['phone']));
		i+=1;

def main():
	while True:
		start();
		key=input("请输入操作序号:")
		if key == '1':
			addStudentInfo();
			listStudenInfo();
		elif key == '2':
			modifyStudenInfo();
			listStudenInfo();
		elif key == '3':
			deleteStudentInfo();
			listStudenInfo();
		elif key == '4':
			listStudenInfo();
		elif key == '5':
			exit();
main();
