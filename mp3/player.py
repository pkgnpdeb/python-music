from tkinter import*
from tkinter import filedialog

root = Tk()

# Application Title
root.title("MP3 Player")

# Application Box Size 
root.geometry("500x400")

# Function for single media
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose a single media", filetypes=(("mp3 Files", "*.mp3"), ))
    # stripping directory structure and song content
    song = song.replace("/home/n0v1c3/Documents/python-music/mp3/audio/", "")
    song = song.replace(".mp3", "")
    
    playlist_box.insert(END, song)
    
# Function for multiple media
def add_many_songs():
    pass

# Playlist Widget 
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground='black')
playlist_box.pack(pady=20) 

# Button Images 
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

# Buttons Frame Widgets 
control_frame = Frame(root)
control_frame.pack(pady=20)

# Buttons 
back_button = Button(control_frame, image =back_btn_img, borderwidth=0)
forward_button = Button(control_frame,  image=forward_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Song Menu 
my_menu = Menu(root)
root.config(menu = my_menu)

# create drop-downs
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# add single media dropdown
add_song_menu.add_command(label="Add Single Media to Playlist", command=add_song)
# add multiple media dropdown
add_song_menu.add_command(label="Add Multiple Media to Playlist", command=add_many_songs)

# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
