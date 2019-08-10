import sys, pygame
from settings import Settings
import game_functions as gf

from background import Background
import heroes


def character_creation():
    print("Wizard, Elf, or Knight")
    char_select = input('-> ').lower()

    if char_select == 'wizard':
        print('Choose green staff[g] or red staff[r]')
    elif char_select == 'elf':
        print('Choose axe[a], baton[b], cleaver[c], duel sword[d]')
    elif char_select == 'knight':
        print('Choose big sword[bs], big hammer[bh], knight sword[ks]')
    else:
        exit(1)

    weapon = input('-> ').lower()
    return char_select, weapon


def run_game():
    char_select, weapon = character_creation()

    pygame.init()
    clock = pygame.time.Clock()
    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dungeon Capture")

    forrest = Background(
        game_settings, screen, '../resources/backgrounds/forest3.png')

    if char_select == 'wizard':
        player = heroes.Wizard(game_settings, screen, weapon)
    elif char_select == 'elf':
        player = heroes.Elf(game_settings, screen, weapon)
    else:
        player = heroes.Knight(game_settings, screen, weapon)

    while True:

        gf.check_events(player)
        player.update()
        gf.update_screen(game_settings, screen, clock, forrest, player)


run_game()

