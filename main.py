import os
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
        self.iconbitmap('lan.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int(screen_width / 2 - app_database.window_app_size['width'] / 2)
        y = int(screen_height / 2 - app_database.window_app_size['height'] / 2)
        self.geometry(f'{app_database.window_app_size['width']}x{app_database.window_app_size['height']}+{x}+{y}')
        # self.geometry('800x400')
        self.minsize(app_database.window_app_size['width'], app_database.window_app_size['height'])
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
