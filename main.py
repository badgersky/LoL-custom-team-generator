from app import App


if __name__ == '__main__':
    app = App()
    app.mainloop()
    # prompt = f'Enter space separated players` nicknames:\n'
    # while True:
    #     players = input(prompt)
    #     if not players.strip():
    #         continue

    #     generator = team_generator(players)
    #     break

    # commands = {
    #     'press enter': 'generate team based on provided players.',
    #     'a / add': '"add player1 player2 ..." => add players to generator.',
    #     'd / delete': '"delete player1 player2 ..." => delete players from generator.',
    #     's / set': '"set player1 player2 ..." => sets new list of players.',
    #     'p / players': 'displays all players in generator',
    #     'c / clear': 'clears list of players.',
    #     'q / quit': 'quit program.',
    #     'h / help': 'display available commands.',
    # }

    # while True:
    #     prompt = f'\nPress "enter" to generate team, "q" => "enter" to quit, "help" => "enter" to display commands.\n'
    #     command = input(prompt)
    #     command = [word.lower().strip() for word in command.split()]

    #     if not command:
    #         print('-' * 40)
    #         generator.show_teams()
    #         print('-' * 40)
    #     elif command[0] in ['q', 'quit']:
    #         break
    #     elif command[0] in ['h', 'help']:
    #         print('\n' + '-' * 40)
    #         for command, description in commands.items():
    #             print(command + ' >>> ' + description)
    #             print('-' * 40)
    #     elif command[0] in ['a', 'add']:
    #         players = command[1:]
    #         for player in players:
    #             generator.add_player(player)
    #     elif command[0] in ['d', 'delete']:
    #         players = command[1:]
    #         for player in players:
    #             generator.delete_player(player)
    #     elif command[0] in ['c', 'clear']:
    #         generator.players = []
    #     elif command[0] in ['s', 'set']:
    #         players = command[1:]
    #         generator.players = players
    #     elif command[0] in ['p', 'players']:
    #         print('\n' + '-' * 40)
    #         print(f'players: {generator}')
    #         print('-' * 40)
    #     else:
    #         print('invalid command')
            