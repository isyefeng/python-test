#****************************************************************************************************#
# time:2019.6.25
#test tipoc
#****************************************************************************************************#

tip = '*--------------------------------------------*\r\n'

#****************************************************************************************************#
	
class User():
	def __init__(self, first_name, last_name, hello = 'hello!'):
		self.first_name = first_name
		self.last_name = last_name
		self.hello = hello
		self.login_attempts = 0
	
	def descride_user(self):
		print('First name:' + self.first_name + 
		'\nLast name:' + self.last_name)
	
	def greet_user(self):
		print(self.hello)

	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0
	
	
#继承，括号内需要添加父类的名字
class Admin(User):
	def __init__(self, first_name, last_name, hello = 'hello'):
		super().__init__(first_name, last_name, hello)
		self.privileges = ['can add post','can delete post','can ban user']
		
	def dsp_admin_privilege(self):
		print('Admin privilege has:')
		for buf in self.privileges:
			print('-' + buf)

			
#在一个类当中实例化另一个类
class Privilees():
	def __init__(self):
		self.privileges =  ['can add post','can delete post','can ban user']
	
	def dsp_admin_privilege(self):
		print('Admin privilege has:')
		for buf in self.privileges:
			print('-' + buf)

class AdminRoot(User):
	def __init__(self, first_name, last_name, hello = 'hello'):
		super().__init__(first_name, last_name, hello)
		self.root = Privilees()



	




















