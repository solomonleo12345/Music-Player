from tkinter import *
from PIL import ImageTk, Image
import pygame
from tkinter import ttk
import os
from tkinter import filedialog
import random
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

pygame.mixer.init()

# ***********************************************************

# CREATE TKINTER WINDOW

walker_frame = Tk()
walker_frame.geometry('900x600')
walker_frame.title("Music Player")
walker_frame.maxsize(900, 650)
walker_frame.minsize(900, 650)
walker_frame.configure(bg="black")


# ***********************************************************

# CREATE TABS

# GRAB SONG LENGTH
def play_time():
    # grab current song elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000

    # convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # current_song = song_list.curselection()
    # current_song = current_song[0]
    # next_one = next_one[0] + 1

    # get the song name
    song = song_list.get(ACTIVE)
    # add the path to it
    song = f'Music List/{song}.mp3'

    # load song with mutagen
    song_mut = MP3(song)
    # get song length
    global song_length
    song_length = song_mut.info.length
    # convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # output time to status bar
    time_label.config(text=f'Time Elapsed - {converted_current_time} of {converted_song_length} ')

    # update slider position value to current song position
    my_slider.config(value=current_time)


    # update time
    time_label.after(1000, play_time)


def play():
    play_time()
    song = song_list.get(ACTIVE)
    song = f'Music List/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


def next_song():
    # get the current song tuple number
    next_one = song_list.curselection()
    next_one = next_one[0] + 1
    # next_one = next_one[0] + 1

    # get the song name
    song = song_list.get(next_one)
    # add the path to it
    song = f'Music List/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, END)
    song_list.activate(next_one)
    song_list.selection_set(next_one, last=None)
    song_list.see(ACTIVE)


def previous_song():
    next_one = song_list.curselection()

    next_one = next_one[0]
    print(next_one)
    # next_one = next_one[0] + 1
    if next_one == 0:
        pygame.mixer.music.stop()
        song_list.selection_clear(ACTIVE)
        '''song = song_list.get(next_one)
        song = f'Music List/{song}.mp3'
    
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    
        song_list.selection_clear(0, END)
        song_list.activate("end")
        song_list.selection_set("end")
        song_list.see("end")'''
    else:
        next_one = next_one - 1
        song = song_list.get(next_one)
        song = f'Music List/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        song_list.selection_clear(0, END)
        song_list.activate(next_one)
        song_list.selection_set(next_one, last=None)

    '''song = song_list.get(next_one)
    song = f'Music List/{song}.mp3'
  
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
  
    song_list.selection_clear(0, END)
    song_list.activate(next_one)
    song_list.selection_set(next_one, last=None)'''


def stop():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

    # clear the status bar
    bottom_timeline.config(text='')


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def slide(x):
    slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')

# ************************* WALKER TAB **********************************

# FRAMES IN THE WALKER TAB 

song_list = Listbox(walker_frame, bg="black", fg="white", selectbackground="grey", selectforeground="black",
                    relief='groove', bd=7,
                    font=('Sans', 16), cursor="circle")
song_list.place(x=240, y=10, width=650, height=415)

my_files = os.listdir('Music List')
for file in my_files:
    song_name = file.replace(".mp3", "")
    song_list.insert(END, song_name)

# BUTTON IMAGES

play_image = PhotoImage(file="play.png")
next_image = PhotoImage(file="next.png")
prev_image = PhotoImage(file="prev.png")
pause_image = PhotoImage(file="pause.png")
stop_image = PhotoImage(file="stop.png")
shuffle_image = PhotoImage(file="shuffle.png")
Name_image = PhotoImage(file="Name_image.png")
w_image = PhotoImage(file="S.png")

# WALKER SYMBOL

canvas = Canvas(walker_frame, width=220, height=150)
canvas.place(x=10, y=10, width=220, height=150)
img = ImageTk.PhotoImage(Image.open("symbol.png"))
canvas.create_image(0, 0, anchor=NW, image=img)

medium_left = Label(walker_frame, text="W41K3R_63986"
                                       "\n\nWE POTATO YOU"
                                       "\n\nMUSIC PLAYER"
                                       "\n\nWE LIVE"
                                       "\nWE LOVE"
                                       "\nWE LIE", font=('algerian', 14), bg="black", fg="white", relief='groove', bd=7)

medium_left.place(x=10, y=170, width=220, height=255)

bottom_timeline = Frame(walker_frame, bg="grey55", relief='groove', bd=7)
bottom_timeline.place(x=10, y=455, width=880, height=50)

time_label = Label(walker_frame, bg="grey55", bd=7)
time_label.place(x=700, y=510, width=180, height=30)

bottom_playback = Frame(walker_frame, bg="black", relief='groove', bd=7)
bottom_playback.place(x=212, y=515, width=475, height=75)

# ALL BUTTONS

shuffle_button = Button(walker_frame, bg="grey55", activebackground="white", image=w_image)
shuffle_button.place(x=225, y=529, width=50, height=50)

prev_button = Button(walker_frame, bg="grey55", activebackground="white", image=prev_image, command=previous_song)
prev_button.place(x=305, y=529, width=50, height=50)

play_button = Button(walker_frame, bg="grey55", activebackground="white", image=play_image, command=play)
play_button.place(x=385, y=529, width=50, height=50)

pause_button = Button(walker_frame, bg="grey55", activebackground="white", image=pause_image,
                      command=lambda: pause(paused))
pause_button.place(x=465, y=529, width=50, height=50)

next_button = Button(walker_frame, bg="grey55", activebackground="white", image=next_image, command=next_song)
next_button.place(x=625, y=529, width=50, height=50)

stop_button = Button(walker_frame, bg="grey55", activebackground="white", image=stop_image, command=stop)
stop_button.place(x=545, y=529, width=50, height=50)

my_slider = ttk.Scale(bottom_timeline, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=850)
my_slider.pack(pady=5)

slider_label = Label(walker_frame, bg="grey55", text='0')
slider_label.place(x=10, y=510, width=180, height=30)

walker_frame.mainloop()
