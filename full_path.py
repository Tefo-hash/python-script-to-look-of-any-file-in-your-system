import os

sure = input("are you sure about the name of the file y(yes)or n(no) : ")

true = True

while true:

	if sure == 'y':
		true = False

	elif sure == 'y':
		true = False
	
	else:
		print("Hint : write your answer in lowercase :)")
		print()
		sure = input("Please Enter a correct value y(yes) or n(no) : "  )
		true = True

file = input("Now please enter the name of the file : ")
path = "c:\\"

for current_path, dir_name, filename in os.walk(path):
	for i in filename:
		if sure == 'y':
			if file == i:
				print()
				print("the path of file :", current_path)
				print("filename : ", i)
				break
		else:
			if file in i:
				print()
				print("the path of file :", current_path)
				print("filename : ", i)
				print()
				
			



