import customtkinter as ctk
from generator import TeamGenerator
from tkinter import messagebox


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window properties
        self.geometry('650x350')
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

        self.players_manager.rowconfigure((0, 1, 2), weight=1)
        self.players_manager.columnconfigure((0, 1, 2), weight=1)
        # self.players_manager.columnconfigure(1, weight=2)

        # players manager label
        self.lbl_players_manager = ctk.CTkLabel(self.players_manager, text='PLAYERS MANAGER')
        self.lbl_players_manager.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        # adding new players
        self.lbl_new_players = ctk.CTkLabel(self.players_manager, text='Add new players:')
        self.lbl_new_players.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.ent_players = ctk.CTkEntry(self.players_manager, width=350)
        self.ent_players.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.btn_new_players = ctk.CTkButton(self.players_manager, width=40, text='Add', command=self.add_player)
        self.btn_new_players.grid(row=1, column=2, padx=10, pady=5, sticky='w')

        # removing players
        self.lbl_remove_players = ctk.CTkLabel(self.players_manager, text='Chose players to remove:')
        self.lbl_remove_players.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        self.remove_players_combobox = self.create_choose_players_combobox()
        self.remove_players_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.btn_remove_players = ctk.CTkButton(self.players_manager, width=60, text='remove', command=self.remove_players)
        self.btn_remove_players.grid(row=2, column=2, padx=10, pady=5, sticky='w')

    def add_player(self):
        new_players = self.ent_players.get().split()

        with open('players.txt', 'a+') as file:
            players = self.load_players()
            for player in new_players:
                if player.lower() not in players:
                    file.write(player.lower() + '\n')
                else:
                    messagebox.showinfo('Already Saved', f'Player: {player.lower()} already saved.')

        self.choose_players.destroy()
        self.create_choose_players_combobox()
        self.ent_players.delete('0', 'end')

    def load_players(self):
        try:
            with open('players.txt', 'r') as file:
                players = file.readlines()
        except FileNotFoundError:
            return []
        return [player[:-1] for player in players]
    
    def create_choose_players_combobox(self):
        if players := self.load_players():
            self.choose_players = ctk.CTkComboBox(self.players_manager, values=players, command=self.insert_players)
        else:
            self.choose_players = ctk.CTkComboBox(self.players_manager, values=['no players'], state='readonly')
            self.choose_players.set('no players')
        return self.choose_players
    
    def insert_players(self, player):
        self.ent_players.insert('end', player + ' ')

    def remove_players(self):
        players = self.load_players()
        players_to_remove = self.ent_players.get().split()

        for player in players_to_remove:
            if player in players:
                players.remove(player)

        with open('players.txt', 'w') as file:
            for player in players:
                file.write(player.lower() + '\n')

        self.choose_players.destroy()
        self.create_choose_players_combobox()
        self.ent_players.delete('0', 'end')
        