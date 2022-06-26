import tkinter
import customtkinter
import Main

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()  
app.geometry("1080x360")

def next_week():
    print("Playing Next Week")

def play_league():
    print("Playing All League")

nextWeek = customtkinter.CTkButton(master=app, text="Next Week", command=next_week)
nextWeek.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

playAllLeague = customtkinter.CTkButton(master=app, text="Play All League", command=play_league)
playAllLeague.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)




app.mainloop()