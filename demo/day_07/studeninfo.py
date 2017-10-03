studenList=[]
while True:
	# 学生管理系统
	print('===========学生管理系统=======');
	print('1.添加学生信息');
	print('2.修改学生信息');
	print('3.显示学生信息');
	print('==============================');
	#studeninfo=[];
	key=input("请输入操作序号:")
	if key == '1':
		# 添加学生信息
		newName=input("请输入学生信息:");
		newAge=input("请输入学生年龄:");
		newPhone=input("请输入电话号码:");
		studeninfo={};
		studeninfo['name']=newName;
		studeninfo['age']=newAge;
		studeninfo['phone']=newPhone;
		studenList.append(studeninfo);
	elif key == '2':
		print("修改学生信息");
		stuId=input("请输入学生序号：");
		newName=input("请输入学生信息:");
		newAge=input("请输入学生年龄:");
		newPhone=input("请输入电话号码:");
		studenList[int(stuId)-1]['name']=newName;
		studenList[int(stuId)-1]['age']=newAge;
		studenList[int(stuId)-1]['phone']=newPhone;
	elif key == '3':
		print('序号	姓名	年龄	电话号码');
		i=1;
		for x in studenList:
			print("%d 	%s 	%s 	%s" %(i,x['name'],x['age'],x['phone']));
			i+=1;
