from tkinter import*

root = Tk()

# Application Title
root.title("MP3 Player")

# Application Box Size 
root.geometry("500x400")

# Playlist Widget 
playlist_box = Listbox(root, bg="black", fg="green", width=60)
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

root.mainloop()
