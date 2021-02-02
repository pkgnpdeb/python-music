from tkinter import*
from tkinter import filedialog
import pygame 
import time 
from mutagen.wave import WAVE
import tkinter.ttk as ttk
#from pygame import mixer

# Root Window
root = Tk()

# Application Title
root.title("MUSIC Player") 

# Application Box Size 
root.geometry("600x500")

# Initalize PyGame
pygame.mixer.init()

# Function to deal with time 
def play_time():
	# grab current song time 
	current_time = pygame.mixer.music.get_pos() / 1000
	
	# converting song time to time format 
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
	
	# Reconstructing song with directory structure 
	song = playlist_box.get(ACTIVE)
	song = f'/home/n0v1c3/Documents/python-music/mp3/audio/{song}.wav'
	
	# FInd current song length
	song_mut = WAVE(song)
	global song_length
	song_length = song_mut.info.length
	
	# Convert to time format 
	converted_song_length =  time.strftime('%M:%S', time.gmtime(song_length))
	my_label.config(text=converted_song_length)
	
	# Set slider length to song length 
	song_slider.config(to=song_length)
	my_label.config(text=song_slider.get())
	
	# Move slider along time stamp
	next_time = int(song_slider.get()) + 1
	
	# Output new time value to slider 
	song_slider.config(value=next_time)
	
	# add current time to status bar 
	if current_time >= 0:
		status_bar.config(text=f'TIme Elapsed: {converted_current_time} of {converted_song_length}  ')
	
	# create loop to create time every second
	status_bar.after(1000, play_time) 

# Initalize Mixer 
# mixer.init()

# Function for single media
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose a single media", filetypes=(("WAV Files", "*.wav"), ))
    # stripping directory structure and song content
    song = song.replace("/home/n0v1c3/Documents/python-music/mp3/audio/", "")
    song = song.replace(".wav", "")
    # Add to end of playlist 	
    playlist_box.insert(END, song)
    
# Function for multiple media
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("WAV Files", "*.wav" ), ))
	
	# Loop through song list and replace directory structure and mp3 from song name
	for song in songs:
		# Strip out directory structure and .mp3 from song title
		song = song.replace("/home/n0v1c3/Documents/python-music/mp3/audio/", "")
		song = song.replace(".wav", "")
		# Add To End of Playlist
		playlist_box.insert(END, song)

# Function for deleting Single Media
def delete_song():
	# Delete highlighted song drom playlist
	playlist_box.delete(ANCHOR)

# Function for deleting Multiple Media
def delete_all_songs():
	# Delete alll media 
	playlist_box.delete(0, END)

# Function for Playing Media 
def play():
	# Reconstructuring media with directory structure 
	song = playlist_box.get(ACTIVE)
	song = f'/home/n0v1c3/Documents/python-music/mp3/audio/{song}.wav'

	#Load media with pygame mixer
	pygame.mixer.music.load(song)

	#Play media with pygame mixer
	pygame.mixer.music.play(loops=0)
	
	# Get song time 
	play_time()

# Function to Stop Media 
def stop():
	# Stop the song 
	pygame.mixer.music.stop()	
	
	# Clear the Playlist Bar
	playlist_box.selection_clear(ACTIVE)
	
	status_bar.config(text=f'')

# Function for Next Media 
def next_song():
	# Get next song number 
	next_one = playlist_box.curselection()
	my_label.config(text=next_one)
	# Append one to current song number tuple/list
	next_one = next_one[0] + 1	
	
	# Media title from playlist 
	song = playlist_box.get(next_one)
	
	# Add directory structure to the media  
	song = f'/home/n0v1c3/Documents/python-music/mp3/audio/{song}.wav'
	
	#Load song with pygame mixer
	pygame.mixer.music.load(song)

	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0)
	
	# Clearing Active Bar in Playlist 
	playlist_box.selection_clear(0, END)
	
	# Move Active Bar to next song 
	playlist_box.activate(next_one)
	
	# Set Active Bar to next song 
	playlist_box.selection_set(next_one, last=None)


# Function to Play Previous Song 
def previous_song():
	# Get next song number 
	next_one = playlist_box.curselection()
	my_label.config(text=next_one)
	# Append one to current song number tuple/list
	next_one = next_one[0] - 1	
	
	# Media title from playlist 
	song = playlist_box.get(next_one)
	
	# Add directory structure to the media  
	song = f'/home/n0v1c3/Documents/python-music/mp3/audio/{song}.wav'
	
	#Load song with pygame mixer
	pygame.mixer.music.load(song)

	#Play song with pygame mixer
	pygame.mixer.music.play(loops=0)
	
	# Clearing Active Bar in Playlist 
	playlist_box.selection_clear(0, END)
	
	# Move Active Bar to next song 
	playlist_box.activate(next_one)
	
	# Set Active Bar to next song 
	playlist_box.selection_set(next_one, last=None)

# Pause Variable
global paused  
paused = False 

# Function to Pause Media 
def pause(is_paused):
	global paused 
	paused = is_paused 
	
	if paused: 
		#unpause
		pygame.mixer.music.unpause()
		paused = False  
	else: 
		#pause
		pygame.mixer.music.pause()
		paused = True

# Create Volume Function
def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())

# Creare Slider Function 
def slide(x):
	pass

# Create Main Frame 
main_frame = Frame(root)
main_frame.pack(pady=20)

# Playlist Box 
playlist_box = Listbox(main_frame, bg="black", fg="white", width=60, selectbackground="yellow", selectforeground='black')
playlist_box.grid(row=0, column=0)

# Create volume slider frame 
volume_frame = LabelFrame(main_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

# Create Volume Slider 
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, length=125, value=1, command=volume)
volume_slider.pack(pady=10)

# Create Song Slider 
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, length=360, value=0, command=slide)
song_slider.grid(row=2, column=0, pady=20)

# Button Images 
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

# Buttons Frame Widgets 
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

# Buttons 
back_button = Button(control_frame, image =back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(control_frame,  image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Song Menu 
my_menu = Menu(root)
root.config(menu = my_menu)

# create add-song drop-downs
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# add single media dropdown
add_song_menu.add_command(label="Add Single Media to Playlist", command=add_song)
# add multiple media dropdown
add_song_menu.add_command(label="Add Multiple Media to Playlist", command=add_many_songs)

# create delete drop downs
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label= "Remove Songs", menu=remove_song_menu)
# remove single media dropdown
remove_song_menu.add_command(label="Remove Single Media from Playlist", command=delete_song)
# remove multiple media dropdown
remove_song_menu.add_command(label="Remove Multiple Media from Playlist", command = delete_all_songs)

# Create Status Bar 
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2) 

# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
