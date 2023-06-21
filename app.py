import customtkinter as ctk
from generator import TeamGenerator
from tkinter import messagebox


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window properties
        self.geometry('650x300')
        self.title('TeamGenerator')

        # grid configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=1)   

        # frames
        self.players_manager = ctk.CTkFrame(self)
        self.generator = ctk.CTkFrame(self)

        self.players_manager.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
        self.generator.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.players_manager.rowconfigure((0, 1), weight=1)
        self.players_manager.columnconfigure((0, 1, 2), weight=1)
        # self.players_manager.columnconfigure(1, weight=2)

        # adding new players
        self.lbl_new_players = ctk.CTkLabel(self.players_manager, text='Add new players:')
        self.lbl_new_players.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.ent_new_players = ctk.CTkEntry(self.players_manager, width=350)
        self.ent_new_players.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.btn_new_players = ctk.CTkButton(self.players_manager, width=40, text='Add', command=self.add_player)
        self.btn_new_players.grid(row=0, column=2, padx=10, pady=5, sticky='w')

        # removing players
        self.lbl_remove_players = ctk.CTkLabel(self.players_manager, text='Chose players to remove:')
        self.lbl_remove_players.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.create_remove_players_combobox()

        self.btn_remove_players = ctk.CTkButton(self.players_manager, width=60, text='remove')
        self.btn_remove_players.grid(row=1, column=2, padx=10, pady=5, sticky='w')

    def add_player(self):
        new_players = self.ent_new_players.get().split()

        with open('players.txt', 'a') as file:
            for player in new_players:
                file.write(player + '\n')

        self.chose_players.destroy()
        self.create_remove_players_combobox()
        self.ent_new_players.delete('0', 'end')
        messagebox.showinfo('Succes', 'Players succesfully saved!')

    def load_players(self):
        try:
            with open('players.txt', 'r') as file:
                players = file.readlines()
                print(players)
        except FileNotFoundError:
            return ['no players']
        return players
    
    def create_remove_players_combobox(self):
        self.chose_players = ctk.CTkComboBox(self.players_manager, values=self.load_players(), command=self.insert_players)
        self.chose_players.grid(row=1, column=1, padx=5, pady=5, sticky='w')
    
    def insert_players(self, player):
        self.ent_new_players.insert('end', player + ' ')
