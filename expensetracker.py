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
    utilities_dict = {"electricity": 0, "water": 0, "gas": 0}
    file_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
# print out greeting message
art = """
░█▀▀░█░█░█▀█░█▀▀░█▀█░█▀▀░█▀▀░░░▀█▀░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄
░█▀▀░▄▀▄░█▀▀░█▀▀░█░█░▀▀█░█▀▀░░░░█░░█▀▄░█▀█░█░░░█▀▄░█▀▀░█▀▄
░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░░▀░░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀
"""
print(art)
# initial user interface
while True:
    choice = input("\nWelcome to the expense tracker. Would you like to view or edit your expenses if so, press 1 to view, 2 to edit, 3 to see total and q to exit. \n")
    if choice == '1':
        print(f'Your electricity expenses: {utilities_dict.get('electricity')}')
        print(f'Your water expenses: {utilities_dict.get('water')}')
        print(f'Your gas expenses: {utilities_dict.get('gas')}')
    elif choice == '2':
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
            continue
        else:
            print('invalid response.\n')
            continue
    elif choice == '3':
        print('Total of your expenses are: ', utilities_dict.get('electricity') + utilities_dict.get('water') + utilities_dict.get('gas'))
    elif choice == 'q':
        print('bye')
        with open('data.json', 'w') as f:
            file_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
        break
    else:
        print('invalid response.\n')
        continue
    return_input = input('Would you like to make any more changes? (y to return, n to quit): ').strip().lower()
    if return_input == 'n':
        print('Bye! \n')
        file_path.write_text(json.dumps(utilities_dict), encoding="utf-8")
        break
