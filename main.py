from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

class Intro(Frame):#this class is a Frame
    def __init__(self , master , controller):
        Frame.__init__(self , master)
        background_color = "#FFFFFF"
        self.configure(bg=background_color) 

        #Label widget for heading      
        self.top_label = Label(self, text = "MRGS Chromebook Booking App", font=("Arial" , "15" , "bold"), bg = background_color)
        self.top_label.place(x=50,y=155)

        #Image 
        self.image_label = Image.open("mrgs logo.jpg")
        self.image_label = self.image_label.resize((100,100), Image.ANTIALIAS)
        self.image_label = ImageTk.PhotoImage(self.image_label)

        #Image Label
        self.label_image = Label(self, image = self.image_label, bg = background_color)
        self.label_image.place(x=200, y=40)
        #self.label_image.grid(row=1,pady=20)


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
            reg_password_box = Entry(register_frame , show = '*')
            reg_password_box.place (x=160 , y=55)

            confirm_pass_label = Label(register_frame , text = "Confirm Password" , font = "15")
            confirm_pass_label.place (x=10 , y=100)
            confirm_pass_box = Entry(register_frame , show = '*')
            confirm_pass_box.place (x=160 , y=100)

            #register button function that puts input in a file
            def justify():
                if reg_studentid_box.get()!="" or reg_password_box.get()!="" or confirm_pass_box.get()!="":
                    if reg_password_box.get()==confirm_pass_box.get():
                        with open("id_pass.txt", "a") as f:
                            f.write(reg_studentid_box.get()+","+reg_password_box.get()+"\n")
                            messagebox.showinfo('Registration' , "Your registration is successful")
                            register_frame.destroy()
                    else:
                        messagebox.showinfo('Registration' , "Your passwords do not match!")
                else:
                    messagebox.showinfo('Registration' , "The fields are empty, Please fill them out!")

            register_button = Button(register_frame , text = "Register" , font = "15" , command = justify)
            register_button.place (x=150 , y=150)

            register_frame.geometry("400x200")  
            register_frame.mainloop()


        #Register Button
        self.register_button = Button(self, text = "Register" , command = reg)
        self.register_button.place(x=400, y=15)

        #username entry Widget
        self.user_box = Entry(self)
        self.user_box.place(x=160, y=210)
        self.user_label = Label(self , text = "Student ID" , font = "15", bg = background_color)
        self.user_label.place(x=60, y=210)
        #self.user_label.grid(row=4 , padx=10)
 

        #password entry Widget
        self.pass_box = Entry(self, show = '*')
        self.pass_box.place(x=160,y=254)
        self.pass_label = Label(self, text = "Password" , font = "15", bg = background_color)
        self.pass_label.place(x=70,y=254)

        #Log in button function
        def validation():
            try:
                with open("id_pass.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.student_id, self.student_pass =e.split(",")
                        if self.student_id.strip() == self.user_box.get() and self.student_pass.strip() == self.pass_box.get():
                            controller.show_frame(Book)                                                  
                            i = 1                        
                            break
                        
                    if i==0:
                        messagebox.showinfo("Error", "Please enter correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please try again")

        #Log in button
        self.log_button = Button(self, text = "Log In" , command = validation)
        self.log_button.place(x=225 , y=300)   

      
#Booking Activity class
class Book(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        background_color = "#FFFFFF"
        self.configure(bg=background_color)

        #Label heading Widget
        self.top_label = Label(self, text = "MRGS Chromebook Booking App", font=("Arial" , "15" , "bold"), bg = background_color)
        self.top_label.place(x=60,y=125)

        #image
        self.image_label = Image.open("mrgs logo.jpg")
        self.image_label = self.image_label.resize((100,100), Image.ANTIALIAS)
        self.image_label = ImageTk.PhotoImage(self.image_label)

        #Image Label
        self.label_image = Label(self, image = self.image_label, bg = background_color)
        self.label_image.place(x=200, y=20)    
        
        #instruction label
        self.int_label = Label(self, text="Details:", bg=background_color, font=("Arial Bold", 13))
        self.int_label.place(x=220, y=170)      

        #user's name label and input box
        self.name_label = Label(self , text="Name" , font=(13) , bg=background_color)#label for user instruction
        self.name_label.place(x=110 , y=215)
        name_box = Entry(self)#user input
        name_box.place(x=180, y=215)

        #user's input for time
        self.time_label = Label(self, text="Time" , font=(13), bg=background_color)
        self.time_label.place(x=120 , y=265)

        click = StringVar()
        click.set("1:30")
        time = OptionMenu(self, click, "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00", "3:10")
        time.place(x=180, y=260)

        #user's input for location
        self.loc_label = Label(self, text="Location", font=(13), bg=background_color)
        self.loc_label.place(x=95 , y=314)

        clicked = StringVar()
        clicked.set("Resource Room")
        location = OptionMenu(self, clicked, "Resource Room", "Deans Centre", "IT Department" )
        location.place(x=180 , y=310)

        #preview Window
        def preview():
      
            preview_frame = Tk()
            preview_frame.title("Preview")

            #Label for user's decision
            pre_label = Label(preview_frame, text="Selected Details", font="13")
            pre_label.place(x=120,y=30)

            #Name preview
            pre_name_label = Label(preview_frame, text="Name:", font="11")
            pre_name_label.place(x=70,y=110)
            sel_name_label = Label(preview_frame, text=name_box.get(), font="11" )
            sel_name_label.place(x=170,y=110)
          
            #Time preview
            pre_time_label = Label(preview_frame, text="Time:", font="11")
            pre_time_label.place(x=70,y=160)
            sel_time_label = Label(preview_frame, text=click.get(), font="11")
            sel_time_label.place(x=170,y=160)
    
            #Location preview
            pre_location_label = Label(preview_frame, text="Location:", font="11")
            pre_location_label.place(x=70,y=210)
            sel_location_label = Label(preview_frame, text=clicked.get(), font="11")#selected option from dropdown menu
            sel_location_label.place(x=170,y=210)
   
            #Close button
            close_button = Button(preview_frame, text="Close", font="11", borderwidth=3, command=preview_frame.destroy)
            close_button.place(x=10,y=300)

            #function for save button
            def save_details():
              with open("details.txt","a") as f:
                f.write(name_box.get()+","+click.get()+","+clicked.get()+",\n")

                preview_frame.destroy()#destroys preview frame
                controller.show_frame(End)#shows end frame
            
            #Save button 
            save_button = Button(preview_frame, text="Save", font="11", borderwidth=3, command = save_details)
            save_button.place(x=270,y=300)
          
            #frame resize and mainloop 
            preview_frame.geometry("350x350")
            preview_frame.mainloop()
                  
        #info save button
        self.save_button = Button(self , text = "save", command=preview)
        self.save_button.place(x=420 , y=360)

      
#Summary/End Page
class End(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        background_color = "#FFFFFF"
        self.configure(bg=background_color)
      
        #Label to let user know the order is successful
        sum_label = Label(self, text="Your chromebook has\n been saved for you to pick up" , bg=background_color, font=15)
        sum_label.place(x=100,y=100)

        #function for close Button
        def close():
          exit()
      
        #close Button
        fin_button = Button(self, text="Close", font=15, command = close)
        fin_button.place(x=400,y=370)

        




class BookingApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        bg=background_color = "white"

        self.window = Frame(self,bg=background_color)
        self.window.pack()

        self.window.grid_rowconfigure(0, minsize = 800)
        self.window.grid_columnconfigure(0, minsize = 800)

        self.frames = {}
        for F in (Intro,Book,End):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")#have to use sticky

        self.show_frame(Intro)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title("Booking App")


#start of program
if __name__ == '__main__':           
    app = BookingApp()
    app.maxsize(500,450)
    app.mainloop()