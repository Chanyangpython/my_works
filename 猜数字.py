import random
import yanzheng
import admin
import history
import zidingyi

#以下为查看激活状态
yanzheng.yz()

#已激活后运行的代码
print("您已输入产品密钥，所以可直接开始游戏。")
renpin = random.randint(1,100)
if renpin > 50:
	print(f"今日人品：{renpin},又是好运的一天！")
elif renpin == 50:
	print(f"今日人品：{renpin},可以啦！")
else:
	print(f"今日人品：{renpin},建议重开，运气太差啦！")


#历史记录
history.jilu()

#游戏主循环，下次记得重构

your = '是否游玩自定义模式？（yes/no)'
an = input(your)
if an == 'yes':
	fn = '请输入第一个数字：'
	fm = int(input(fn))
	ln = '输入第二个数字'
	lm = int(input(ln))
	zidingyi.yourself(first_number=fm,last_number=lm)

second = "\n请选择难易程度：“H”（困难），“M”（普通），“E”（简单）"
second += "\n按任意键退出，游戏内按E退出"

active = True

while active:

	choose = input(second)
	if choose == 'H':
		admin.admH()

	elif choose == 'M':		
		admin.admM()
		
	elif choose == 'E':		
		admin.admE()
		
	else:
		active = False