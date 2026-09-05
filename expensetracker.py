# import modules
from time import sleep
import json
from pathlib import Path
base_dir = Path.home() / "Documents" / "expense tracker"
base_dir.mkdir(parents=True, exist_ok=True)
file_path = base_dir / "data.json"
if file_path.exists():
    utilities_dict = json.loads(file_path.read_text(encoding="utf-8"))
else:
    utilities_dict = {"electricity": "0", "water": "0", "gas": "0"}
    file_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
# print out greeting message
print("_____                                  _____               _             ")
print("| ____|_  ___ __   ___ _ __  ___  ___  |_   _| __ __ _  ___| | _____ _ __ ")
print("|  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \   | || '__/ _` |/ __| |/ / _ \ '__|")
print("| |___ >  <| |_) |  __/ | | \__ \  __/   | || | | (_| | (__|   <  __/ | ")
print("|_____/_/\_\ .__/ \___|_| |_|___/\___|   |_||_|  \__,_|\___|_|\_\___|_|   ")
print("            |_|                                                            ")

print("\n")
# initial user interface
while True:
    answer = input("Welcome to the expense tracker. Would you like to view or edit your expenses if so, press 1 to view, 2 to edit and q to exit. \n")
    if answer == "1":
        print(f'Your electricity expenses: {utilities_dict.get('electricity')}')
        print(f'Your water expenses: {utilities_dict.get('water')}')
        print(f'Your gas expenses: {utilities_dict.get('gas')}')
    elif answer == "2":
        edit = input('Which expense would you like to edit? e for electricity, w for water, g for gas r to return\n')
        
        if edit == 'e':
            utilities_dict['electricity'] = input('enter your electricity expense: ')
            print('expense set! ')
        elif edit == 'w':
            utilities_dict['water'] = input('enter your water expense: ')
            print('expense set! ')
        elif edit == 'g':
            utilities_dict['gas'] = input('enter your gas expense: ')
            print('expense set! ')
        elif edit == 'r':
            sleep(1)
        else:
            print('invalid response.\n')
            continue

    elif answer == 'q':
        print('bye!')
        with open('data.json', 'w') as f:
            jfile_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
        break
    else:
        print('Invalid choice try again')
        continue
    return_input = input('Would you like to make any more changes? (y to return, n to quit):\n').strip().lower()
    if return_input == 'n':
        print('Bye!')
        file_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
        break
