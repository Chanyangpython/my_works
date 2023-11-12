def yz():
	while True:
		try:
			with open('pawd.txt') as yanzheng:
				miyao = yanzheng.read()
				if miyao == 'QAZ1W-SXE2D-CRF3V-TGB4Y':
					break
				else:
					while True:
						third = '请输入产品密钥，例如："QD5RF-EFGD5-EDJCI-DFE5D"'
						forth = input(third)
						if forth == 'QAZ1W-SXE2D-CRF3V-TGB4Y':
							print("感谢购买")
							with open('pawd.txt','w') as password:
								password.write("QAZ1W-SXE2D-CRF3V-TGB4Y")
								break
						else:
							print("请输入正确的产品密钥。")
					
		except FileNotFoundError:
			print("由于您是首次使用该软件，所以请输入产品密钥。")
			while True:
				third = '请输入产品密钥，例如："QD5RF-EFGD5-EDJCI-DFE5D"'
				forth = input(third)
				if forth == 'QAZ1W-SXE2D-CRF3V-TGB4Y':
					print("感谢购买")
					with open('pawd.txt','w') as password:
						password.write("QAZ1W-SXE2D-CRF3V-TGB4Y")
					break
				else:
					print("请输入正确的产品密钥。")