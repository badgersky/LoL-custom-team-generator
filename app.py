import customtkinter as ctk
from generator import TeamGenerator
from tkinter import messagebox


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window properties
        self.geometry('650x420')
        self.title('TeamGenerator')

        # grid configuration
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)   

        # frames
        self.players_manager = ctk.CTkFrame(self)
        self.generator = ctk.CTkFrame(self)

        self.players_manager.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
        self.generator.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.players_manager.rowconfigure((0, 1, 2), weight=1)
        self.players_manager.columnconfigure((0, 1, 2), weight=1)
        
        self.generator.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.generator.columnconfigure(0, weight=1)
        self.generator.columnconfigure(1, weight=2)

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

        self.remove_players_combobox = self.create_choose_players_combobox(self.players_manager, self.insert_players_to_remove)
        self.remove_players_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.btn_remove_players = ctk.CTkButton(self.players_manager, width=60, text='Remove', command=self.remove_players)
        self.btn_remove_players.grid(row=2, column=2, padx=10, pady=5, sticky='w')

        # team generator label
        self.lbl_generate_teams = ctk.CTkLabel(self.generator, text='TEAM GENERATOR')
        self.lbl_generate_teams.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # choose players to make teams out of
        self.choose_players_combobox = self.create_choose_players_combobox(self.generator, command=self.insert_players_to_generator)
        self.choose_players_combobox.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.txt_choose_players = ctk.CTkTextbox(self.generator, height=50, width=350)
        self.txt_choose_players.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        # generate teams
        self.btn_generate_teams = ctk.CTkButton(self.generator, width=60, text='Generate', command=self.generate_teams)
        self.btn_generate_teams.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        # clear button
        self.btn_clear_generator = ctk.CTkButton(self.generator, width=60, text='Clear', command=self.clear_generator)
        self.btn_clear_generator.grid(row=2, column=1,padx=10, pady=10, sticky='w')

        # left and right generated team labels and textboxes
        self.lbl_left_team = ctk.CTkLabel(self.generator, text='Left team:')
        self.lbl_right_team = ctk.CTkLabel(self.generator, text='Right team:')
        self.lbl_left_team.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.lbl_right_team.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.ent_left_team = ctk.CTkEntry(self.generator)
        self.ent_right_team = ctk.CTkEntry(self.generator)
        self.ent_left_team.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.ent_right_team.grid(row=4, column=1, padx=10, pady=10, sticky='ew')


    def add_player(self):
        new_players = list(set(player.lower() for player in self.ent_players.get().split()))

        with open('players.txt', 'a+') as file:
            players = self.load_players()
            for player in sorted(new_players):
                if player.lower() not in players:
                    file.write(player.lower() + '\n')
                else:
                    messagebox.showinfo('Already Saved', f'Player: {player.lower()} already saved.')

        self.update_comboboxes()
        self.ent_players.delete('0', 'end')

    def load_players(self):
        try:
            with open('players.txt', 'r') as file:
                players = file.readlines()
        except FileNotFoundError:
            return []
        return [player[:-1] for player in players]
    
    def create_choose_players_combobox(self, frame, command=None):
        if players := self.load_players():
            self.choose_players = ctk.CTkComboBox(frame, values=players, command=command)
        else:
            self.choose_players = ctk.CTkComboBox(frame, values=['no players'], state='readonly')
            self.choose_players.set('no players')
        return self.choose_players
    
    def insert_players_to_remove(self, player):
        chosen_players = self.ent_players.get()
        if player not in chosen_players:
            self.ent_players.insert('end', player + ' ')
        else:
            chosen_players = chosen_players.replace(player + ' ', '')
            self.ent_players.delete('0', 'end')
            self.ent_players.insert('end', chosen_players)

    def remove_players(self):
        players_in_generator = self.txt_choose_players.get('0.0', 'end').split()
        players = self.load_players()
        players_to_remove = self.ent_players.get().split()

        for player in players_to_remove:
            if player in players:
                players.remove(player)
            if player in players_in_generator:
                players_in_generator.remove(player)

        with open('players.txt', 'w') as file:
            for player in players:
                file.write(player.lower() + '\n')

        self.update_comboboxes()
        self.ent_players.delete('0', 'end')
        self.txt_choose_players.delete('0.0', 'end')
        self.txt_choose_players.insert('0.0', ' '.join(players_in_generator))

    def update_comboboxes(self):
        self.remove_players_combobox.destroy()
        self.remove_players_combobox = self.create_choose_players_combobox(self.players_manager, self.insert_players_to_remove)
        self.remove_players_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.choose_players_combobox.destroy()
        self.choose_players_combobox = self.create_choose_players_combobox(self.generator, self.insert_players_to_generator)
        self.choose_players_combobox.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    def insert_players_to_generator(self, player):
        chosen_players = self.txt_choose_players.get('0.0', 'end').split()
        if player not in chosen_players:
            self.txt_choose_players.insert('end', player + ' ')
        else:
            chosen_players.remove(player)
            self.txt_choose_players.delete('0.0', 'end')
            self.txt_choose_players.insert('end', ' '.join(chosen_players) + ' ')

    def generate_teams(self):
        players = self.txt_choose_players.get('0.0', 'end').split()
        
        generator = TeamGenerator(players)
        teams = generator.generate_teams()

        self.ent_right_team.delete('0', 'end')
        self.ent_left_team.delete('0', 'end')

        self.ent_left_team.insert('end', ' '.join(teams['left']))
        self.ent_right_team.insert('end', ' '.join(teams['right']))

    def clear_generator(self):
        self.txt_choose_players.delete('0.0', 'end')
        self.ent_right_team.delete('0', 'end')
        self.ent_left_team.delete('0', 'end')
        