cal = True
while cal:
		try:
			r = eval(input("Enter the radius in (cm):"))
		except NameError:
			print("Only digits accepted!!")
			
		else:
			area = 3.142 * ( r ** 2)
			print(f"The area of the circle is {area :.3f}cm")
			cal = False