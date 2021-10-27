from tkinter import *
from PIL import ImageTk, Image
import pygame 
from tkinter import ttk
import os
from tkinter import filedialog
import random
import time 

pygame.mixer.init()


# ***********************************************************

# CREATE TKINTER WINDOW

root = Tk()
root.geometry('900x600')
root.title("Music Player")
root.maxsize(900, 650)
root.minsize(900, 650)
root.configure(bg="black")

# ***********************************************************

# CREATE TABS

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

walker_frame = Frame(my_notebook, width=900, height=700, bg = "black")
normal_frame = Frame(my_notebook, width=900, height=700, bg = "green")

walker_frame.pack(fill="both", expand=1)
normal_frame.pack(fill="both", expand=1)

my_notebook.add(walker_frame, text="Walker Player")
my_notebook.add(normal_frame, text="Normal Player")

# ***********************************************************



# ***********************************************  FUNCTIONS *******************************************************

# 
# GRAB SONG LENGTH
def play_time():
  # grab current song elapsed time
  current_time = pygame.mixer.music.get_pos() / 1000

  #convert to time format
  converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

  # output time to status bar
  bottom_timeline1.config(text=converted_current_time)
  
  # update time
  bottom_timeline1.after(1000, play_time)


def play():
  song = song_list.get(ACTIVE)
  song = f'Music List/{song}.mp3'

  pygame.mixer.music.load(song)
  pygame.mixer.music.play(loops=0)


def shuffle_normal():
  random.shuffle(song_path_list)
  print(song_path_list)

  if pygame.mixer.music.get_busy():
    random.shuffle(song_path_list)
    pygame.mixer.music.queue(song_path_list[0])


def play_normal():

  song = song_list2.get(ACTIVE)
  play_time()
  
  for i in song_name_list:
    if song == i:
      
      name_index = song_name_list.index(i)
      pygame.mixer.music.load(song_path_list[name_index])
      pygame.mixer.music.play(loops=0)
      # pygame.mixer.music.queue(song_path_list[name_index+1])
      last_index = len(song_path_list)-1
      
      if name_index == last_index:
        
        pygame.mixer.music.queue(song_path_list[0])
        #song_list2.selection_clear(0, END)
        #song_list2.selection_set(0)
        #song_list2.selection_set(name_index+1, last=None)
      
      else:
        
        pygame.mixer.music.queue(song_path_list[name_index+1])
        #song_list2.selection_clear(0, END)
        #song_list2.selection_set(name_index+1)
      
      '''song_list2.selection_clear(0, END)
      song_list2.activate(name_index+1)
  
      song_list2.selection_set(name_index+1, last=None)'''
  

def add_song():
  global song_path
  song = filedialog.askopenfilename(initialdir='C:/Users/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav")))
  song_path = song
  name = os.path.basename(song)
  name = name.replace(".mp3", "")
  song_list2.insert(END, name)


def add_selected_songs_to_list():
  
  songs = filedialog.askopenfilenames(initialdir='C:/Users/', title="Choose many songs", filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav")))
  
  global song_path_list, song_name_list
  song_path_list = []
  song_name_list = []
  for song in songs:
    name = os.path.basename(song)
    name = name.replace(".mp3", "")
    song_path_list.append(song)
    song_name_list.append(name)
    
  
  add_many_songs()



def add_many_songs():

  for name in song_name_list:
    
    song_list2.insert(END, name)

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

def play_next_normal():
  next_one = song_list2.curselection()
  next_one = next_one[0]  

  last_index = len(song_path_list)-1
      
  if next_one == last_index:
    song = song_path_list[0]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list2.selection_clear(0, END)
    song_list2.activate(0)
    song_list2.selection_set(0, last=None)
  else:
    next_one = next_one + 1
    song = song_path_list[next_one]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list2.selection_clear(0, END)
    song_list2.activate(next_one)
    song_list2.selection_set(next_one, last=None)
  

def play_prev_normal():
  next_one = song_list2.curselection()
  next_one = next_one[0]  

  last_index = len(song_path_list)-1
      
  if next_one == 0:
    song = song_path_list[last_index]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list2.selection_clear(0, END)
    song_list2.activate(last_index)
    song_list2.selection_set(last_index, last=None)
  else:
    next_one = next_one - 1
    song = song_path_list[next_one]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list2.selection_clear(0, END)
    song_list2.activate(next_one)
    song_list2.selection_set(next_one, last=None)


  '''next_one = song_list2.curselection()
  next_one = next_one[0] - 1
  song = song_path_list[next_one]
  pygame.mixer.music.load(song)
  pygame.mixer.music.play(loops=0)

  song_list2.selection_clear(0, END)
  song_list2.activate(next_one)
  song_list2.selection_set(next_one, last=None)'''


def previous_song():
  next_one = song_list.curselection()

  next_one = next_one[0] - 1
  # next_one = next_one[0] + 1
  song = song_list.get(next_one)
  song = f'Music List/{song}.mp3'

  pygame.mixer.music.load(song)
  pygame.mixer.music.play(loops=0)

  song_list.selection_clear(0, END)
  song_list.activate(next_one)
  song_list.selection_set(next_one, last=None)
  

def stop():
  pygame.mixer.music.stop()
  song_list.selection_clear(ACTIVE)

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

def delete_song():
  song_list2.delete(ANCHOR)
  pygame.mixer.music.stop()

def delete_all_songs():
  song_list2.delete(0, END)
  pygame.mixer.music.stop()

def shuffle_songs():
  pass






#def sh


# ************************* WALKER TAB **********************************

# FRAMES IN THE WALKER TAB 

song_list = Listbox(walker_frame, bg="black", fg="white", selectbackground="grey", selectforeground="black", relief='groove', bd=7,
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

bottom_timeline = Frame(walker_frame, bg="black", relief='groove', bd=7)
bottom_timeline.place(x=10, y=455, width=880, height=50)

bottom_playback = Frame(walker_frame, bg="black", relief='groove', bd=7)
bottom_playback.place(x=212, y=515, width=475, height=75)

# ALL BUTTONS

shuffle_button = Button(walker_frame, bg="grey25", activebackground="white", image=shuffle_image, command=shuffle_songs)
shuffle_button.place(x=225, y=529, width=50, height=50)

prev_button = Button(walker_frame, bg="grey25", activebackground="white", image=prev_image, command=previous_song)
prev_button.place(x=305, y=529, width=50, height=50)

play_button = Button(walker_frame, bg="grey25", activebackground="white", image=play_image, command=play)
play_button.place(x=385, y=529, width=50, height=50)

pause_button = Button(walker_frame, bg="grey25", activebackground="white", image=pause_image, command=lambda: pause(paused))
pause_button.place(x=465, y=529, width=50, height=50)

next_button = Button(walker_frame, bg="grey25", activebackground="white", image=next_image, command=next_song)
next_button.place(x=625, y=529, width=50, height=50)

stop_button = Button(walker_frame, bg="grey25", activebackground="white", image=stop_image, command = stop)
stop_button.place(x=545, y=529, width=50, height=50)


# **************************** NORMAL PLAYER TAB ****************************************************

# FRAMES IN NORMAL TAB

song_list2 = Listbox(normal_frame, bg="darkolivegreen1", fg="black", selectbackground="darkolivegreen2", selectforeground="black", relief='groove', bd=7,
                    font=('Sans', 16), cursor="circle")
song_list2.place(x=240, y=10, width=650, height=415)

canvas1 = Canvas(normal_frame, width=220, height=150)
canvas1.place(x=10, y=10, width=220, height=150)
img1 = ImageTk.PhotoImage(Image.open("normal_symbol.png"))
canvas1.create_image(0, 0, anchor=NW, image=img1)

medium_left1 = Frame(normal_frame, bg="darkolivegreen1", relief='groove', bd=7)
medium_left1.place(x=10, y=170, width=220, height=255)

bottom_timeline1 = Label(normal_frame, bg="darkolivegreen1", relief='groove', bd=7, anchor=E)
bottom_timeline1.place(x=10, y=455, width=880, height=50)

bottom_playback1 = Frame(normal_frame, bg="darkolivegreen1", relief='groove', bd=7)
bottom_playback1.place(x=212, y=515, width=475, height=75)

# BUTTONS IN NORMAL TAB

Image_button1 = Button(normal_frame, bg="darkolivegreen1", activebackground="darkolivegreen1", image=Name_image)
Image_button1.place(x=225, y=529, width=50, height=50)

prev_button1 = Button(normal_frame, bg="darkolivegreen1", activebackground="white", image=prev_image, command=play_prev_normal)
prev_button1.place(x=305, y=529, width=50, height=50)

play_button1 = Button(normal_frame, bg="darkolivegreen1", activebackground="white", image=play_image, command=play_normal)
play_button1.place(x=385, y=529, width=50, height=50)

pause_button1 = Button(normal_frame, bg="darkolivegreen1", activebackground="white", image=pause_image, command=lambda: pause(paused))
pause_button1.place(x=465, y=529, width=50, height=50)

next_button1 = Button(normal_frame, bg="darkolivegreen1", activebackground="white", image=next_image, command=play_next_normal)
next_button1.place(x=625, y=529, width=50, height=50)

stop_button = Button(normal_frame, bg="darkolivegreen1", activebackground="white", image=stop_image, command = stop)
stop_button.place(x=545, y=529, width=50, height=50)

add_many_song_button = Button(medium_left1, text="Add Songs", font=("Arial", 16, 'bold'), bg="darkolivegreen1", fg="black",activebackground="white", relief='groove', bd=10,command=add_selected_songs_to_list)
add_many_song_button.pack(pady=10)

remove_song = Button(medium_left1, text="Remove A Song", font=("Arial", 16, 'bold'), bg="darkolivegreen1", fg="black",activebackground="white", relief='groove', bd=10, command=delete_song)
remove_song.pack(pady=10)

remove_all_songs = Button(medium_left1, text="Remove All Songs", font=("Arial", 16, 'bold'), bg="darkolivegreen1", fg="black",activebackground="white", relief='groove', bd=10, command=delete_all_songs)
remove_all_songs.pack(pady=10)

root.mainloop()