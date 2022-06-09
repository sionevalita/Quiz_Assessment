from tkinter import*
from PIL import Image, ImageTk
import tkinter.messagebox

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

    
    #register button function to open register window (no function yet)
    def reg():
      register_frame = Tk()
      register_frame.title("Registration")
      reg_studentid_label = Label(register_frame , text = "Student ID" , font = "15")
      reg_studentid_label.place (x=45 , y=10)
      reg_studentid_box = Entry(register_frame)
      reg_studentid_box.place (x=160 , y=10)

      reg_password_label = Label(register_frame , text = "Password" , font = "15")
      reg_password_label.place (x=45 , y=55)
      reg_password_box = Entry(register_frame)
      reg_password_box.place (x=160 , y=55)

      confirm_pass_label = Label(register_frame , text = "Confirm Password" , font = "15")
      confirm_pass_label.place (x=10 , y=100)
      confirm_pass_box = Entry(register_frame)
      confirm_pass_box.place (x=160 , y=100)

      #register button function that puts input in a file
      def justify():
          if reg_studentid_box.get()!="" or reg_password_box.get()!="" or confirm_pass_box.get()!="":
              if reg_password_box.get()==confirm_pass_box.get():
                  with open("ID , Pass", "a") as f:
                      f.write(reg_studentid_box.get()+","+reg_password_box.get()+"\n")
                      tkinter.messagebox.showinfo('Registration' , "Your registration is successful")
                      register_frame.destroy()
              else:
                  tkinter.messagebox.showinfo('Registration' , "Your passwords do not match!")
          else:
              tkinter.messagebox.showinfo('Registration' , "The fields are empty, Please fill them out!")
                 
      register_button = Button(register_frame , text = "Register" , font = "15" , command = justify)
      register_button.place (x=150 , y=150)
        
      register_frame.geometry("400x200")  
      register_frame.mainloop()

      
    #Register Button
    self.register_button = Button(self.intro_frame, text = "Register" , command = reg)
    self.register_button.place(x=360, y=-80)

    #username entry Widget
    self.user_box = Entry(self.intro_frame)
    self.user_box.grid(row=4 , padx=90)
    self.user_label = Label(self.intro_frame , text = "Student ID" , font = "15", bg = background_color)
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