from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

class Intro:
  def __init__(self , master):
    background_color = "#FFFFFF"

    #Frame set up
    self.intro_frame = Frame(master, bg = background_color, padx=100, pady=100)
    self.intro_frame.grid()

    #Label widget for heading      
    self.top_label = Label(self.intro_frame, text = "MRGS Chromebook Booking App", font=("Arial" , "15" , "bold"), bg = background_color)
    self.top_label.grid(row=2, padx=0 , pady=48)

    #Image 
    self.image_label = Image.open("mrgs logo.jpg")
    self.image_label = self.image_label.resize((100,100), Image.ANTIALIAS)
    self.image_label = ImageTk.PhotoImage(self.image_label)

    #Image Label
    self.label_image = Label(self.intro_frame, image = self.image_label, bg = background_color)
    self.label_image.place(x=110, y=-57)

    #Register Button
    self.signin_button = Button(self.intro_frame, text = "Register")
    self.signin_button.place(x=360, y=-80)

    #username entry Widget
    self.user_box = Entry(self.intro_frame)
    self.user_box.grid(row=4 , padx=90)
    self.user_label = Label(self.intro_frame , text = "Username" , font = "15", bg = background_color)
    self.user_label.place(x=0, y=125)

    #password entry Widget
    self.pass_box = Entry(self.intro_frame)
    self.pass_box.grid(row=6, pady=20)
    self.pass_label = Label(self.intro_frame, text = "Password" , font = "15", bg = background_color)
    self.pass_label.place(x=0,y=167)

    #Log in button
    self.log_button = Button(self.intro_frame, text = "Log In")
    self.log_button.place(x=150,y=220)
    
    
    

    


    
#***************start program ******************#

if __name__ == "__main__":
  window = Tk()
  window.title("MRGS Chromebook Booking App")
  class_starter = Intro(window)
  window.mainloop()