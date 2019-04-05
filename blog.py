items_dict= {'1':'Mocha Oreo Milkshake', '2':'Apple Carrot Milkshake','3':'Mint Brownie Milkshake','4':'Classic Vanillla Milkshake',
			   '5':'Capsicum Cabbage Sandwich','6':'Carrot Sandwich','7':'Grilled Tomato Cheese Sandwich','8':'PBJ Sandwich'}


class BlogManager:
	def __init__(self,profile_no,profile_name,email_id):
		self.profile_no=profile_no
		self.profile_name=profile_name
		self.email_id=email_id
		

	def access(self,profile_no):
		print("What would you like to cook today ?\n\n\
			1.Milkshakes\n\
			2.Sandwiches\n")

		choice1 = int(input("Enter your option: "))

		if choice1 == 1:
			print(" MOCHA OREO MILKSHAKE\n\n\
					INGREDIENTS\n\n\
					3 cups vanilla ice cream.\n\
					6 Oreo cookies, broken into chunks.\n\
					3/4 cup strong brewed coffee, cooled.\n\
					chocolate syrup, for garnish\n\
					Cool Whip.\n\
					mini Oreos, for garnish.\n\
					INSTRUCTIONS\n\n\
					Blend all apart garnish ingridients for 20 - 30 seconds\n\
					Garnish and serve chilled\n\n\
					APPLE CARROT MILKSHAKE\n\n\
					INGREDIENTS\n\n\
					2 apples , peeled and cut into chunks\n\
					1 carrot , par boiled\n\
					5 almonds , water soaked\n\
					1 1/2 glass milk\n\
					sugar , as per required\n\
					almond flakes, for garnish\n\
					INSTRUCTIONS\n\n\
					Blend all apart garnish ingridients for 20 - 30 seconds\n\
					Garnish and serve chilled\n\n\
					MINT BROWNIE MILKSHAKE\n\n\
					INGREDIENTS\n\n\
					 1/2 cup milk\n\
					 3 scoops chocolate mint chip ice cream\n\
					 1 brownie\n\
					 Whipped cream , for garnish\n\
					 Green food coloring optional\n\
					 Sprinkles and extra brownie pieces , for garnish\n\
					INSTRUCTIONS\n\n\
					Blend all apart garnish ingridients for 20 - 30 seconds\n\
					Garnish and serve chilled\n\n\
					CLASSIC VANILLA MILKSHAKE\n\n\
					INGREDIENTS\n\n\
					1 1/2 cup vanilla ice cream\n\
					1 cup whole milk\n\
					1/2 tsp vanilla extract\n\
					whipped cream (optional)\n\
					INSTRUCTIONS\n\n\
					Blend all apart garnish ingridients for 20 - 30 seconds\n\
					Garnish and serve chilled\n\
					")
			
	
		elif choice1 == 2:
			print("CAPSICUM CABBAGE SANDWICH\n\n\
					INGREDIENTS\n\
					2 cups cabbage ,finely chopped\n\
					1 cup capsicum , finely chopped\n\
					1 tbsp APF\n\
					5 tbsp milk\n\
					Butter for greasing\n\
					salt , as required\n\
					INSTRUCTIONS\n\
					Mix all ingredients and place a spoonful on a slice of bread and spread it .\n\
					Cook on hot tawa\n\
					Serve with ketchup\n\
					CARROT SANDWICH\n\n\
					INGREDIENTS\n\
					2 cups carrot , grated\n\
					green chillies few , chopped\n\
					butter for greasing\n\
					salt , as required\n\
					INSTRUCTIONS\n\
					Mix all ingredients and place a spoonful on a slice of bread and spread it .\n\
					Cook on hot tawa\n\
					Serve with ketchup\n\
					GRILLED TOMATO CHEESE SANDWICH\n\n\
					INGREDIENTS\n\
					sliced tomatoes\n\
					processed cheese , grated\n\
					butter for greasing\n\
					salt , as required\n\
					INSTRUCTIONS\n\
					Mix all ingredients and place  on a slice of bread and spread it .\n\
					Grill\n\
					Serve with ketchup\n\
					PBJ SANDWICH\n\
					INGREDIENTS\n\
					Peanut Butter\n\
					jam , of your choice\n\
					butter for greasing\n\
					INSTRUCTIONS\n\
					Mix all ingredients and place  on a slice of bread and spread it .\n\
					Grill\n\
					")

		

	def receivecopy(self,profile_no,delivery_address):
		self.delivery_address=delivery_address
		
		print("Enjoy!!you will receive the copy in 24 working hours")
		

	def deliverdish(self,profile_no,delivery_address):
		self.delivery_address=delivery_address

		count = int(input("Enter the number of items you want to buy: "))

		items = []

		for i in range(count):
			print("Choose what would you like to have today from below options : \n\n\
				1. Mocha Oreo Milkshake\n\
				2. Apple Carrot Milkshake\n\
				3. Mint Brownie Milkshake\n\
				4. Classic Vanillla Milkshake\n\
				5. Capsicum Cabbage Sandwich\n\
				6. Carrot Sandwich\n\
				7. Grilled Tomato Cheese Sandwich\n\
				8. PBJ Sandwich")

			choice2=input("Enter your choice:")
		
			items.append(items_dict[choice2])

			print(items)

			print("-"*50)

			print("Your order is confirmed tracking details will be sent to your registered email id")

