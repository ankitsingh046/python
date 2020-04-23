import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad')
main_application.wm_iconbitmap('icon.ico')


# main menu ---------------------------------start

main_menu = tk.Menu(main_application)

# file icons
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# edit icon
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

edit = tk.Menu(main_menu, tearoff=False)


# View icon
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


# color theme

light_default_icon = tk.PhotoImage(file='icons/light_default.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, dark_icon, monokai_icon)
color_dict = {
    'Light default': ('#000000', '#ffffff'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Monokai': ('#d3b774', '#474747')
}

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)


# main menu-----------------------------------End-------------------------


# toolbar ---------------------------------start--------------------------

tool_bar = tk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# Font Family box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(
    tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

# Font-Size box
font_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, textvariable=font_var,
                         width=10, state='readonly')
font_size['values'] = tuple(range(8, 81, 2))
font_size.current(2)
font_size.grid(row=0, column=1, padx=5)


# bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic buton
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# Underline Button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font color button
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# align left button
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center button
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right button
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)


# toolbar-----------------------------------End---------------------------------------------------------------------------------


# text editor ---------------------------------start----------------------

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(fill=tk.Y, side=tk.RIGHT)
scroll_bar.config(command=text_editor.yview)

text_editor.focus_set()
text_editor.pack(fill=tk.BOTH, expand=True)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family and font functionality
current_font_family = 'Arial'
current_font_size = 12


def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def chane_font_size(main_application):
    global current_font_size
    current_font_size = font_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", chane_font_size)


# Bold Button
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


# italic btn
def change_italic():
    text_property1 = tk.font.Font(font=text_editor['font'])
    # print(text_property1.actual())
    if text_property1.actual()['slant'] == 'roman':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'italic'))
    if text_property1.actual()['slant'] == 'italic':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'roman'))


italic_btn.configure(command=change_italic)


# underline
def change_underline():
    text_property1 = tk.font.Font(font=text_editor['font'])
    # print(text_property1.actual())
    if text_property1.actual()['underline'] == 0:
        text_editor.configure(
            font=(current_font_family, current_font_size, 'underline'))
    if text_property1.actual()['underline'] == 1:
        text_editor.configure(
            font=(current_font_family, current_font_size, 'normal'))


underline_btn.configure(command=change_underline)


# font color
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

# align function
# left


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
    # print(text_content)


align_left_btn.configure(command=align_left)

# center


def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
    # print(text_content)


align_center_btn.configure(command=align_center)

# right


def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
    # print(text_content)


align_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial', 12))


# text editor-----------------------------------End-----------------------


# main statusbar ---------------------------------start-------------------

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    if text_editor.edit_modified():
        global text_changed
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters: {characters} Words: {words}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)
# main statusbar-----------------------------------End


# main menu fuctionality---------------------------------start------------
# variable
url = ''

# file menu functionality```````````

# New
def new_file():
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


file.add_command(label='New', image=new_icon, compound=tk.LEFT,
                 accelerator='Ctrl+N', command=new_file)


# open

def open_file():
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                     filetypes=(
                                         ('Text Files', '*.txt'), ('All Files', '*.*'))
                                     )
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except:
        return
    main_application.title(os.path.basename(url))


file.add_command(label='Open', image=open_icon, compound=tk.LEFT,
                 accelerator='Ctrl+O', command=open_file)

# save file

def save_file():
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                ('Text Files', '*.txt'), ('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close
            

    except:
        return
    

file.add_command(label='Save', image=save_icon,
                 compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)

# save as
def save_as():
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                ('Text Files', '*.txt'), ('All Files', '*.*')))
        content = text_editor.get(1.0, tk.END)
        url.write(content)
        url.close
    except:
        tk.messagebox.showerror('Warning', 'Error occured')

file.add_command(label='Save As', image=save_as_icon,
                 compound=tk.LEFT, accelerator='Ctrl+Alt+S',
                 command=save_as)


# exit
def exit_func():
    global url, text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning', 'Doyou  want to save file?')
            if mbox is True:
                save_file()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit', image=exit_icon,
                 compound=tk.LEFT, accelerator='Ctrl+Q', command = exit_func)



# Edit menu functionality`````````````````````````````````````````````
# copy

edit.add_command(label='Copy', image=copy_icon,
                 compound=tk.LEFT, accelerator='Ctrl+C',
                 command=lambda : text_editor.event_generate('<Control c>'))


edit.add_command(label='Paste', image=paste_icon,
                 compound=tk.LEFT, accelerator='Ctrl+V',
                 command=lambda : text_editor.event_generate('<Control v>'))


edit.add_command(label='Cut', image=cut_icon,
                 compound=tk.LEFT, accelerator='Ctrl+X',
                 command=lambda : text_editor.event_generate('<Control x>'))

                 
edit.add_command(label='Clear All', image=clear_all_icon,
                 compound=tk.LEFT, accelerator='Ctrl+Alt+X',
                 command=lambda : text_editor.delete(1.0,tk.END))



edit.add_command(label='Find', image=find_icon,
                 compound=tk.LEFT, accelerator='Ctrl+F')





# view button functionality
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',
                     image=status_bar_icon, compound=tk.LEFT)

# color theme
count = 0
for i in color_dict:
    color_theme.add_radiobutton(
        label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1


# main menu fuctionality-----------------------------------End------------


main_application.config(menu=main_menu)

main_application.mainloop()
