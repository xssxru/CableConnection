import app_database
import customtkinter

customtkinter.set_appearance_mode("dark")


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button_solving = customtkinter.CTkButton(self, text='Solving', command=self.button_callback)
        self.button_solving.grid(row=0, column=0, padx=20, pady=5)
        self.button_tutorial = customtkinter.CTkButton(self, text='Tutorial', command=self.button_callback)
        self.button_tutorial.grid(row=1, column=0, padx=20, pady=5)

    def button_callback(self):
        print("action complete")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(app_database.metadata['name'])
        self.geometry("500x250")
        self.minsize(500, 250)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.app_label_name = customtkinter.CTkLabel(self, text=app_database.metadata['name'], font=('Segoe UI', 20))
        self.app_label_name.grid(row=0, column=0, padx=10, pady=10)

        self.home_frame = HomeFrame(self)
        self.home_frame.grid(row=1, column=0, padx=10, pady=10)
        # self.home_frame.configure(fg_color='transparent')

        self.app_label_version = customtkinter.CTkLabel(self, text=app_database.metadata['version'], font=('Segoe UI', 10))
        self.app_label_version.grid(row=2, column=0, padx=1, pady=1)


app = App()
app.mainloop()
