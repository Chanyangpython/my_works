def jilu():
	jilu = '是否查询游戏记录（YES/NO）'
	answer_10 = input(jilu)
	if answer_10 == 'YES':
		try:
			with open('recording.txt') as file_object:
				contents = file_object.read()
		except FileNotFoundError:
			print("您还没有历史记录")
		else:
			print(contents)