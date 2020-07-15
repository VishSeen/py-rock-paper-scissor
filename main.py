# ------------------------------ #
#       Rock Paper Scissor       #
# ------------------------------ #
# Option available are #
# 1 : Rock
# 2 : Paper
# 3 : Scissor

# ------------------------------- #
import random


# building the game UI
def ui_build(): 
	print("---------------------------------------------")
	print("|    Welcome to Rock Paper Scissor game.    |")
	print("---------------------------------------------")
	print("| Compete against the CPU.                  |")
	print("| In this game you will have 3 options :    |")
	print("| 1. Rock                                   |")
	print("| 2. Paper                                  |")
	print("| 3. Scissor                                |")
	print("---------------------------------------------")
	print("| Kindly enter a number to play.            |")
	print("---------------------------------------------")

def ui_restart():
	print("--------------------------------------------")
	print("|          RESTARTING GAME NOW             |")
	print("--------------------------------------------")

def ui_end():
	print("--------------------------------------------")
	print("|            ENDING GAME NOW               |")
	print("--------------------------------------------")

def ui_play_again():
	print("| Do you want to play again ?               |")
	print("| [Y]es or [N]o                             |")
	print("---------------------------------------------")

def ui_error():
	print("---------------------------------------------")
	print("|                 ERROR !!!                 |")
	print("| Input a number which is < 3 and > 1       |")


# game logic that calculates the winning and losing points
def start():
	cpu = random.randint(1, 3)

	user = input("| Choose now :")

	user_num = int(user)
	cpu_num = int(cpu)

	while(user_num > 3):
		ui_error()
		break
	else:
		if(user_num > cpu_num or user_num == 1 and cpu_num == 3):
			print("---------------------------------------------")
			print("| You WIN. Cpu entered : " + str(cpu_num))
			print("---------------------------------------------")

		elif(user_num == cpu_num):
			print("---------------------------------------------")
			print("| It is a DRAW " + str(cpu_num))
			print("---------------------------------------------")

		else:
			print("---------------------------------------------")
			print("| You LOST. Cpu entered : " + str(cpu_num))
			print("---------------------------------------------")


# game restart UI and logic
def restart():
	ui_play_again()

	play_again = input()

	if(str(play_again) == "y" or str(play_again) == "Y" or str(play_again) == "yes"):
		ui_restart()
		start()
	else:
		ui_end()
		pass


# program lifecycle
if __name__ == "__main__":
	ui_build()
	start()