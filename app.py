import customtkinter as ctk
from generator import TeamGenerator


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window properties
        self.geometry('600x300')
        self.title('TeamGenerator')

        # grid configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=1)

        # frames
        self.new_players = ctk.CTkFrame(self)
        self.generator = ctk.CTkFrame(self)

        self.new_players.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
        self.generator.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
