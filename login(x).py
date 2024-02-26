from tkinter import *
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("CriminalRecords-LOGIN")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Vidheesha T M\Desktop\DBMSMiniProject\rapunzels room.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a login frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Username label and entry
        lbl_username = Label(frame, text="Username", fg="white", bg="black")
        lbl_username.pack(pady=10)
        self.username_entry = Entry(frame)
        self.username_entry.pack()

        # Password label and entry
        lbl_password = Label(frame, text="Password", fg="white", bg="black")
        lbl_password.pack(pady=10)
        self.password_entry = Entry(frame, show="*")
        self.password_entry.pack()

        # Login button
        login_btn = Button(frame, text="Login", command=self.login)
        login_btn.pack(pady=20)

        # Label to display login status
        self.login_status_label = Label(frame, text="", fg="white", bg="black")
        self.login_status_label.pack()

    def login(self):
        # Debugging: Check if the method is called
        print("Login method called")

        # Retrieve username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Debugging: Check retrieved values
        print("Username:", username)
        print("Password:", password)

        # Example: Check if username and password are valid
        if username == "admin" and password == "secret":
            self.login_status_label.config(text="Login successful", fg="green")
        else:
            self.login_status_label.config(text="Invalid credentials", fg="red")

if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
