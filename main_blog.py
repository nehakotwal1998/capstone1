from blog import BlogManager

profiles = {}

profile_no = 1

print("-"*50)

print("Welcome to Orenilla")


while True:
	print("Hi there! What plans for today ?\n\n\
		   1.Create Profile\n\
		   2.Access Recipes\n\
		   3.Receive Copy\n\
		   4.Delivery of Dish\n\
		   5.Exit\n")

	choice = int(input("Enter your option: "))

	if choice == 1 :  
		profile_name=input("Enter a Profile name:")
		email_id=input("Enter a gmail id:")

		profiles[profile_no] = BlogManager(profile_no,profile_name,email_id)
		print(profiles)

		print(f"Profile created successfully! Your Profile number is {profile_no}")



		profile_no += 1

	elif choice == 2:
		profile_num=int(input("Enter your profile_no:"))

		if profile_num in profiles.keys() :
			recipe=profiles[profile_num].access(profile_no)
			print(recipe)


		else :
			print("\n\n OOPS!! You are missing on lot. Create an Account NOW ;)")




	elif choice == 3:

		profile_num=int(input("Enter your profile_no:"))
		print("You can get a copy of our Recipes You just have to pay Rs.100 to the delivery guy :) ")
		delivery_address=input("Enter the delivery address:")

		if profile_num in profiles.keys() :
			booklet=profiles[profile_num].receivecopy(profile_no,delivery_address)
			print(booklet)

		else :
			print("\n\n OOPS!! You are missing on lot .Create an Account NOW ;)")
        


	elif choice == 4:

		profile_num=int(input("Enter your profile_no:"))
		print("Wohoo we are ready for serving orders now ")
		delivery_address=input("Enter the delivery address:")

		if profile_num in profiles.keys() :
			deliveryy=profiles[profile_num].deliverdish(profile_no,delivery_address)
			print(deliveryy)


	else:
		break





		

