



class Account:
	def __init__(self,cust_id,name,initial_bal = 0):
		self.id = cust_id
		self.name = name
		self.balance= initial_bal
	def get_balance(self):
		return self.balance


customer1 = Account("101","Gaurav")
print(customer1.id,customer1.name,customer1.balance)

print(customer1.get_balance())


		








































