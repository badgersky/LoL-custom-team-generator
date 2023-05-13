import random


class team_generator:

    def __init__(self, *args):
        self._players = [player.lower().strip() for player in ' '.join(args).split()]

    def __str__(self):
        """print all players"""

        return ', '.join(self._players)
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, players):
        try:
            if not isinstance(players, list):
                raise TypeError
            self._players = players
        except TypeError:
            print('Wrong data type!')
            return None

    def add_player(self, player):
        """add players to self.players"""

        if player.lower().strip() in self.players:
            print(f'{player.lower().strip()} already in generator.')
            return None
        
        print(f'added: {player.lower().strip()}.')
        self.players.append(player.lower().strip())

    def delete_player(self, player):
        """delete players from self.players"""

        if player.lower().strip() in self.players:
            self._players.remove(player.lower().strip())
            print(f'deleted: {player.lower().strip()}.')
        else:
            print(f'No such player: {player.lower().strip()}.')

    def generate_teams(self):
        """divide players into two teams"""

        random.shuffle(self.players)

        players_per_team = len(self.players) // 2

        teams = {}
        teams['left'] = self.players[:players_per_team]
        teams['right'] = self.players[players_per_team:]
        
        return teams
    
    def show_teams(self):
        """print teams in formatted way"""

        teams = self.generate_teams()

        for side, team in teams.items():
            print(side + ': ' + ', '.join(team))


if __name__ == '__main__':
    pass
