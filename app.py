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

        self.new_players.columnconfigure((0, 2), weight=1)
        self.new_players.columnconfigure(1, weight=2)

        # adding new players
        self.lbl_new_players = ctk.CTkLabel(self.new_players, text='Add new players:')
        self.lbl_new_players.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.ent_new_players = ctk.CTkEntry(self.new_players)
        self.ent_new_players.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        self.btn_new_players = ctk.CTkButton(self.new_players, width=40, text='Add')
        self.btn_new_players.grid(row=0, column=2, padx=5, pady=5)