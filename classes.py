from abc import ABC, abstractmethod


class Storage(ABC):
	@abstractmethod
	def add(self, name, count):
		"""увеличивает запас items"""
		pass

	@abstractmethod
	def remove(self, name, count):
		""" уменьшает запас items"""
		pass

	@abstractmethod
	def get_free_space(self):
		"""вернуть количество свободных мест"""
		pass

	@abstractmethod
	def get_items(self):
		"""возвращает сожержание склада в словаре {товар: количество}"""
		pass

	@abstractmethod
	def get_unique_items_count(self):
		""" возвращает количество уникальных товаров."""
		pass


class Store(Storage):
	def __init__(self, items: dict, capacity=100):
		self.__items = items
		self.__capacity = capacity
	@property
	def capacity(self):
	    return self.__capacity
	@capacity.setter
	def capacity(self, count):
		self.__capacity = count
	def add(self, name, count):
		"""увеличивает запас items с учетом лимита capacity"""
		if name in self.__items.keys():
			if self.get_free_space() >= count:
				print("Товар добавлен")
				self.__items[name] += count
				return True
			else:
				print("Недостаточно места на складе!")
				return False
		else:
			if self.get_free_space() >= count:
				print("Товар добавлен")
				self.__items[name] = count
				return True
			else:
				print("Недостаточно места на складе!")
				return False

	def remove(self, name, count):
		""" уменьшает запас items но не ниже 0"""
		if self.__items[name] >= count:
			print("Такое количество товара на складе есть")
			self.__items[name] -= count
			return True
		else:
			print ("Недостаточно места на складе!")
			return False

	def get_free_space(self):
		"""вернуть количество свободных мест"""
		current_space = 0
		for value in self.__items.values():
			current_space += value
		return self.__capacity - current_space

	def get_items(self):
		"""возвращает сожержание склада в словаре {товар: количество}"""
		return self.__items

	def get_unique_items_count(self):
		""" возвращает количество уникальных товаров."""
		return len(self.__items.keys())

	def __str__(self):
		st = "\n"
		for key, value in self.__items.items():
			print(f"{key}:{value}")
		return st




class Shop(Store):
	def __init__(self, items: dict, capacity=20):
		super().__init__(items, capacity)

	def add(self, name, count):
		if self.get_unique_items_count() >= 5:
			print ("Слишком много товаров")
			return False
		else:
			super().add(name, count)


class Request:
	def __init__(self, storage, request_str):
		req_list = request_str.split()
		action = req_list[0]
		self.__count = int(req_list[1])
		self.__item = req_list[2]
		if action == "Доставить":
			self.__from = req_list[4]
			self.__to =req_list[6]
		elif action == "Забрать":
			self.__from = req_list[4]
			self.__to == None
		elif action == "Привезти":
			self.__to = req_list[4]
			self.__from == None

	def move(self):
		if self.__to and self.__from:
			if eval(self.__to).add(self.__item, self.__count):
				eval(self.__from).remove(self.__item, self.__count)
		elif self.__to:
			eval(self.__to).add(self.__item, self.__count)
		elif self.__from:
			eval(self.__from).remove(self.__item, self.__count)


storage_1 = Store(items={"Телефон": 10,"Компьютер": 10,"Телевизор": 20})
storage_2 = Store(items={"Телефон": 10,"Компьютер": 10,"Приставка": 10})
shop_1 = Shop(items={"Телефон": 3,"Компьютер": 4,"Телевизор": 2})