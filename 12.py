from tkinter import messagebox, simpledialog, Tk, Menu, filedialog
import pyperclip
from collections import Counter
import random


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


def get_task():
    task = simpledialog.askstring('Task', 'What would you like to do?\n\n'
                                          '1. Encrypt a message\n'
                                          '2. Decrypt a message\n'
                                          '3. Encrypt a text file\n'
                                          '4. Decrypt a text file\n'
                                          '5. Character Frequency Analysis\n'
                                          '6. Generate Random Password\n'
                                          '7. Exit')
    return task


def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message


def show_message_box(title, message):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()


def save_to_file(data):
    file_path = filedialog.asksaveasfilename(title='Save File', defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(data)
        show_message_box('Save', 'File saved successfully.')
    else:
        show_message_box('Save', 'Save operation canceled.')


def copy_to_clipboard(data):
    pyperclip.copy(data)
    show_message_box('Copy', 'Message copied to clipboard.')


def encrypt_message():
    message = get_message()
    if message:
        encrypted = swap_letters(message)
        show_message_box('Encryption Result', f'Ciphertext of the secret message is:\n\n{encrypted}')
        copy_to_clipboard(encrypted)
    else:
        show_message_box('Message Error', 'No secret message entered.')


def decrypt_message():
    message = get_message()
    if message:
        decrypted = swap_letters(message)
        show_message_box('Decryption Result', f'Plaintext of the secret message is:\n\n{decrypted}')
        copy_to_clipboard(decrypted)
    else:
        show_message_box('Message Error', 'No secret message entered.')


def encrypt_file():
    file_path = filedialog.askopenfilename(title='Select Text File')
    if file_path:
        with open(file_path, 'r') as file:
            message = file.read()
        if message:
            encrypted = swap_letters(message)
            show_message_box('Encryption Result', 'File encrypted successfully.')
            save_to_file(encrypted)
        else:
            show_message_box('File Error', 'The selected file is empty.')
    else:
        show_message_box('File Error', 'No text file selected.')


def decrypt_file():
    file_path = filedialog.askopenfilename(title='Select Encrypted Text File')
    if file_path:
        with open(file_path, 'r') as file:
            message = file.read()
        if message:
            decrypted = swap_letters(message)
            show_message_box('Decryption Result', 'File decrypted successfully.')
            save_to_file(decrypted)
        else:
            show_message_box('File Error', 'The selected file is empty.')
    else:
        show_message_box('File Error', 'No encrypted text file selected.')


def character_frequency_analysis():
    message = get_message()
    if message:
        frequency = Counter(message)
        analysis_result = "Character Frequency Analysis:\n\n"
        for char, count in frequency.items():
            analysis_result += f"{char}: {count}\n"
        show_message_box('Character Frequency Analysis', analysis_result)
    else:
        show_message_box('Message Error', 'No secret message entered.')


def generate_random_password():
    message = get_message()
    if message:
        random_password = ''.join(random.sample(message, len(message)))
        show_message_box('Random Password', f'Generated Password:\n\n{random_password}')
        copy_to_clipboard(random_password)
    else:
        show_message_box('Message Error', 'No secret message entered.')


root = Tk()
root.withdraw()  # Hide the root window

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Encrypt Message', command=encrypt_message)
file_menu.add_command(label='Decrypt Message', command=decrypt_message)
file_menu.add_command(label='Encrypt Text File', command=encrypt_file)
file_menu.add_command(label='Decrypt Text File', command=decrypt_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Character Frequency Analysis', command=character_frequency_analysis)
edit_menu.add_command(label='Generate Random Password', command=generate_random_password)

while True:
    task = get_task()

    if task == '1':
        encrypt_message()

    elif task == '2':
        decrypt_message()

    elif task == '3':
        encrypt_file()

    elif task == '4':
        decrypt_file()

    elif task == '5':
        character_frequency_analysis()

    elif task == '6':
        generate_random_password()

    elif task == '7':
        break

root.mainloop()
