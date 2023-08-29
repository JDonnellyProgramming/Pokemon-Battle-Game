import tkinter as tk
from PIL import ImageTk, Image
import time

root = tk.Tk()
root.geometry("800x600")

pikachu_image = Image.open(r"C:\Users\josep\Downloads\pikachu_image-removebg-preview.png")
resize_image = pikachu_image.resize((200, 200))
cropped_image = resize_image.crop((500, 100, 700, 700))
pik_img = ImageTk.PhotoImage(resize_image)
pikachu_img = tk.Label(image=pik_img)
pikachu_img.image = pik_img
pikachu_img.place(x=500, y=60)

charizard_image = Image.open(r"C:\Users\josep\Downloads\charizar_pic.png")
resize_image = charizard_image.resize((200, 200))
char_img = ImageTk.PhotoImage(resize_image)
charizard_img = tk.Label(image=char_img)
charizard_img.image = char_img
charizard_img.place(x=150, y=200)
current_pokemon = "Charizard"
fire_x = 500
fire_y = 200
def end_start_animate():
   karlp_img.place_forget()
   pikachu_image = Image.open(r"C:\Users\josep\Downloads\pikachu_image-removebg-preview.png")
   resize_image = pikachu_image.resize((200, 200))
   cropped_image = resize_image.crop((500, 100, 700, 700))
   pik_img = ImageTk.PhotoImage(resize_image)
   pikachu_img = tk.Label(image=pik_img)
   pikachu_img.image = pik_img
   pikachu_img.place(x=500, y=60)

   charizard_image = Image.open(r"C:\Users\josep\Downloads\charizar_pic.png")
   resize_image = charizard_image.resize((200, 200))
   char_img = ImageTk.PhotoImage(resize_image)
   charizard_img = tk.Label(image=char_img)
   charizard_img.image = char_img
   charizard_img.place(x=70, y=300)

   def reset_interface():
       option_label.config(text="")
       fight_button.config(text="FIGHT", bg="white")
       bag_button.config(text="BAG", bg="white")
       pokemon_button.config(text="POKEMON", bg="white")
       run_button.config(text="RUN", bg="white")

   def fight_clicked(event):
       global current_pokemon
       option_label.config(fg='black', bg='white')
       fight_button.config(text="", bg="white")
       bag_button.config(text="", bg="white")
       pokemon_button.config(text="", bg="white")
       run_button.config(text="", bg="white")
       move1 = tk.Label(root, bg='white', fg='black', font=('Arial', 12, 'bold'),
                        cursor="hand2")
       move1.place(x=480, y=450)
       move2 = tk.Label(root, bg='white', fg='black', font=('Arial', 12, 'bold'),
                        cursor="hand2")
       move2.place(x=650, y=450)
       move3 = tk.Label(root, bg='white', fg='black', font=('Arial', 12, 'bold'),
                        cursor="hand2")
       move3.place(x=480, y=528)
       move4 = tk.Label(root, bg='white', fg='black', font=('Arial', 12, 'bold'),
                        cursor="hand2")
       move4.place(x=650, y=528)
       if current_pokemon == 'Charizard':
             move1.config(text="Flamethrower")
             move1.bind("<Button-1>", flamethrower)
             move2.config(text="SCRATCH")
             move2.bind("<Button-1>", scratch)
             move3.config(text="HEAL")
             move3.bind("<Button-1>", heal)
             move4.config(text="BITE")
             move4.bind("<Button-1>", bite)
   def fight_enter(event):
       event.widget.config(highlightthickness=4, highlightcolor='black')

   def fight_leave(event):
       event.widget.config(highlightthickness=0)

   def bag_clicked(event):
       print("bag")

   def bag_enter(event):
       event.widget.config(highlightthickness=4, highlightcolor='black')

   def bag_leave(event):
       event.widget.config(highlightthickness=0)

   def pokemon_clicked(event):
       print("pokemon")

   def pokemon_enter(event):
       event.widget.config(highlightthickness=4, highlightcolor='black')

   def pokemon_leave(event):
       event.widget.config(highlightthickness=0)

   def run_clicked(event):
       empty_text = ""
       text1 = "You cannot run \n from a trainer battle"
       option_label.config(text=empty_text, font=('Arial', 10, 'bold'), fg='black', bg='white')
       fight_button.config(text="", bg="white")
       bag_button.config(text="", bg="white")
       pokemon_button.config(text="", bg="white")
       run_button.config(text="", bg="white")

       def update_text():
           nonlocal empty_text
           if len(empty_text) < len(text1):
               empty_text += text1[len(empty_text)]
               option_label.config(text=empty_text)
               root.after(50, update_text)
           else:
               root.after(1000, reset_interface)

       update_text()

   def run_enter(event):
       event.widget.config(highlightthickness=4, highlightcolor='black')

   def run_leave(event):
       event.widget.config(highlightthickness=0)
   def flamethrower(event):
       global fire_x
       global fire_y
       fire_x += 10
       fire_y -= 10
       fire_label = tk.Label(root, width=1, height=1, bg="red")
       fire_label.place(x=fire_x, y=fire_y)
       root.after(100, flamethrower)

   option_label = tk.Label(root, text="", width=49, height=12,
                           bd=4, relief="solid", bg="white")
   option_label.place(x=447, y=410)
   question_label = tk.Label(root, text="", width=62, height=12, bg='DodgerBlue2',
                             highlightbackground="gold",
                             highlightthickness=4)
   question_label.place(x=0, y=410)
   foe_health_label = tk.Label(root, width=42, height=8, bg="khaki1",
                               bd=4, relief="solid")
   foe_health_label.place(x=70, y=40)
   player_health_label = tk.Label(root, width=42, height=8, bg="khaki1",
                                  bd=4, relief="solid")
   player_health_label.place(x=475, y=280)
   fight_button = tk.Label(root, text="FIGHT", bg="white", fg="black",
                           font=('Arial', 20, 'bold'), cursor="hand2")
   fight_button.place(x=480, y=450)
   fight_button.bind("<Button-1>", fight_clicked)
   fight_button.bind("<Enter>", fight_enter)
   fight_button.bind("<Leave>", fight_leave)
   bag_button = tk.Label(root, text="BAG", bg="white", fg="black",
                         font=('Arial', 20, 'bold'), cursor="hand2")
   bag_button.place(x=700, y=450)
   bag_button.bind("<Button-1>", bag_clicked)
   bag_button.bind("<Enter>", bag_enter)
   bag_button.bind("<Leave>", bag_leave)
   pokemon_button = tk.Label(root, text="POKEMON", bg="white", fg="black",
                             font=('Arial', 20, 'bold'), cursor="hand2")
   pokemon_button.place(x=480, y=528)
   pokemon_button.bind("<Button-1>", pokemon_clicked)
   pokemon_button.bind("<Enter>", pokemon_enter)
   pokemon_button.bind("<Leave>", pokemon_leave)
   run_button = tk.Label(root, text="RUN", bg="white", fg="black",
                         font=('Arial', 20, 'bold'), cursor="hand2")
   run_button.place(x=700, y=528)
   run_button.bind("<Button-1>", run_clicked)
   run_button.bind("<Enter>", run_enter)
   run_button.bind("<Leave>", run_leave)
   pikachu_health_bar_border = tk.Label(root, text="", bg="khaki1", width=28, height=1,
                                        bd=4, relief="solid")
   pikachu_health_bar_border.place(x=140, y=120)
   charizard_health_bar_border = tk.Label(root, text="", bg="khaki1", width=28, height=1,
                                          bd=4, relief="solid")
   charizard_health_bar_border.place(x=545, y=360)
   pikachu_label = tk.Label(root, text="PIKACHU          Lv50", bg="khaki1", fg="black",
                            font=('Arial', 20, 'bold'))
   pikachu_label.place(x=80, y=60)
   pikachu_health_bar = tk.Label(root, text="", bg="green", width=28, height=1)
   pikachu_health_bar.place(x=140, y=120)
   charizard_health_bar = tk.Label(root, text="", bg="green", width=28, height=1)
   charizard_health_bar.place(x=545, y=360)
   charizard_label = tk.Label(root, text="CHARIZARD      Lv50", bg="khaki1", fg="black",
                              font=('Arial', 20, 'bold'))
   charizard_label.place(x=486, y=300)
def start_animate():
   global pikachu_label
   global main_label
   empty_text = ""
   empty_text2 = ""
   text1 = "You are faced by foe Karl Pilkington"
   text2= "You must fight!!"
   main_label = tk.Label(root, text=empty_text, width=113, height=12, bd=4, relief="solid")
   main_label.place(x=0, y=410)
   pikachu_label.place_forget()
   charizard_label.place_forget()
   pikachu_health_bar.place_forget()
   pikachu_health_bar_border.place_forget()
   charizard_health_bar.place_forget()
   charizard_health_bar_border.place_forget()
   pikachu_img.place_forget()
   charizard_img.place_forget()

   def karl_animate():
       global karlp_img
       karl_image = Image.open(r"C:\Users\josep\Downloads\karl_pilkginton.png")
       karl_image = karl_image.convert('RGB')  # Convert the image to RGB format
       resize_image = karl_image.resize((200, 200))
       karl_img = ImageTk.PhotoImage(resize_image)
       karlp_img = tk.Label(image=karl_img)
       karlp_img.image = karl_img
       karlp_img.place(x=550, y=70)
       time.sleep(1)
       end_start_animate()
       #pikachu_animate()
       #charizard_animate()
   def update_text3():
       nonlocal empty_text2
       main_label.place_forget()
       main2_label = tk.Label(root, text=empty_text2, width=113, height=12, bd=4, relief="solid")
       main2_label.place(x=0, y=410)
       if len(empty_text2) < len(text2):
           empty_text2 += text2[len(empty_text2)]
           main_label.config(text=empty_text2)
           root.after(50, update_text3)
       else:
           time.sleep(1)
           karl_animate()
   def update_text2():
       nonlocal empty_text
       if len(empty_text) < len(text1):
           empty_text += text1[len(empty_text)]
           main_label.config(text=empty_text)
           root.after(50, update_text2)
       else:
           time.sleep(1)
           update_text3()
   update_text2()

def reset_interface():
   option_label.config(text="")
   fight_button.config(text="FIGHT", bg="white")
   bag_button.config(text="BAG", bg="white")
   pokemon_button.config(text="POKEMON", bg="white")
   run_button.config(text="RUN", bg="white")
def fight_clicked(event):
   print("fight")
def fight_enter(event):
   event.widget.config(highlightthickness=4, highlightcolor='black')
def fight_leave(event):
   event.widget.config(highlightthickness=0)
def bag_clicked(event):
   print("bag")
def bag_enter(event):
   event.widget.config(highlightthickness=4, highlightcolor='black')
def bag_leave(event):
   event.widget.config(highlightthickness=0)
def pokemon_clicked(event):
   print("pokemon")
def pokemon_enter(event):
   event.widget.config(highlightthickness=4, highlightcolor='black')
def pokemon_leave(event):
   event.widget.config(highlightthickness=0)
def run_clicked(event):
   empty_text = ""
   text1 = "You cannot run \n from a trainer battle"
   option_label.config(text=empty_text, font=('Arial', 10, 'bold'), fg='black', bg='white')
   fight_button.config(text="", bg="white")
   bag_button.config(text="", bg="white")
   pokemon_button.config(text="", bg="white")
   run_button.config(text="", bg="white")

   def update_text():
       nonlocal empty_text
       if len(empty_text) < len(text1):
           empty_text += text1[len(empty_text)]
           option_label.config(text=empty_text)
           root.after(50, update_text)
       else:
           root.after(1000, reset_interface)

   update_text()
def run_enter(event):
   event.widget.config(highlightthickness=4, highlightcolor='black')
def run_leave(event):
   event.widget.config(highlightthickness=0)
option_label = tk.Label(root, text="", width=49, height=12,
                       bd=4, relief="solid", bg="white")
option_label.place(x=447, y=410)
question_label = tk.Label(root, text="", width=62, height=12, bg='DodgerBlue2',
                         highlightbackground="gold",
                         highlightthickness=4)
question_label.place(x=0, y=410)
foe_health_label = tk.Label(root, width=42, height=8, bg="khaki1",
                           bd=4, relief="solid")
foe_health_label.place(x=70, y=40)
player_health_label = tk.Label(root, width=42, height=8, bg="khaki1",
                              bd=4, relief="solid")
player_health_label.place(x=475, y=280)
fight_button = tk.Label(root, text="FIGHT", bg="white", fg="black",
                       font=('Arial', 20, 'bold'), cursor="hand2")
fight_button.place(x=480, y=450)
fight_button.bind("<Button-1>", fight_clicked)
fight_button.bind("<Enter>", fight_enter)
fight_button.bind("<Leave>", fight_leave)
bag_button = tk.Label(root, text="BAG", bg="white", fg="black",
                     font=('Arial', 20, 'bold'), cursor="hand2")
bag_button.place(x=700, y=450)
bag_button.bind("<Button-1>", bag_clicked)
bag_button.bind("<Enter>", bag_enter)
bag_button.bind("<Leave>", bag_leave)
pokemon_button = tk.Label(root, text="POKEMON", bg="white", fg="black",
                         font=('Arial', 20, 'bold'), cursor="hand2")
pokemon_button.place(x=480, y=528)
pokemon_button.bind("<Button-1>", pokemon_clicked)
pokemon_button.bind("<Enter>", pokemon_enter)
pokemon_button.bind("<Leave>", pokemon_leave)
run_button = tk.Label(root, text="RUN", bg="white", fg="black",
                         font=('Arial', 20, 'bold'), cursor="hand2")
run_button.place(x=700, y=528)
run_button.bind("<Button-1>", run_clicked)
run_button.bind("<Enter>", run_enter)
run_button.bind("<Leave>", run_leave)
pikachu_health_bar_border = tk.Label(root, text="", bg="khaki1", width=28, height=1,
                                    bd=4, relief="solid")
pikachu_health_bar_border.place(x=140, y=120)
charizard_health_bar_border = tk.Label(root, text="", bg="khaki1", width=28, height=1,
                                       bd=4, relief="solid")
charizard_health_bar_border.place(x=545, y=360)
pikachu_label = tk.Label(root, text="PIKACHU          Lv50", bg="khaki1", fg="black",
                        font=('Arial', 20, 'bold'))
pikachu_label.place(x=80, y=60)
pikachu_health_bar = tk.Label(root, text="", bg="green", width=28, height=1)
pikachu_health_bar.place(x=140, y=120)
charizard_health_bar = tk.Label(root, text="", bg="green", width=28, height=1)
charizard_health_bar.place(x=545, y=360)
charizard_label = tk.Label(root, text="CHARIZARD      Lv50", bg="khaki1", fg="black",
                          font=('Arial', 20, 'bold'))
charizard_label.place(x=486, y=300)
start_animate()

root.mainloop()
