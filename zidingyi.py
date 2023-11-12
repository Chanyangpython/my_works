import random
import sys

def yourself(first_number,last_number):
	number = random.randint(first_number,last_number)
	print(f"数字为{first_number}-{last_number}")
	first = "\n感谢使用，按E退出，按任意键开始。"
	first += "\n你准备好了吗？"
	message = input(first)

	if message == 'E':
		print("\n感谢使用")
		sys.exit()
	else:
		print("\n我想了一个数字，想猜猜吗？")

	active = True

	guess_number = 1

	while active:

		answer = "\n请写出你的数字(按E退出)"
		text = int(input(answer))

		if text < number:
			print("哈哈哈，猜小了，想再试试吗？")
			guess_number = guess_number + 1	
		elif text > number:
			print("哈哈哈，猜大了，想再试试吗？")
			guess_number = guess_number + 1
		elif text == 'E':
			active = False
		else:
			print(f"您猜了{guess_number}次。")
			with open('recording.txt','a') as file_object:
				file_object.write(f"自定义:{guess_number}\n")
			if guess_number < 10:
				print("您真棒！")
			elif guess_number == 10:
				print("差一点哦！")
			else:
				print("还要多加练习哦")
			text_2 = input("真不错，猜对了，想再试试吗？(按E退出)")
			if text_2 == 'E':
				print("感谢使用")
				sys.exit()
			else:
				break
	