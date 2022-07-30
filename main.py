from classes import storage_1, storage_2, shop_1, Request

while True:
	print("Текущие площади:")
	print(f"storage_1:{storage_1}")
	print(f"storage_2:{storage_2}")
	print(f"shop_1:{shop_1}")

	user_text = input("Введите команду:\n")
	if user_text == "стоп":
		break
	else:
		try:
			req = Request(user_text)
			req.move()
		except Exception as e:
			print("error")