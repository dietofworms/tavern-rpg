import random
import time


# Classes
class Character(object):
    def __init__(self, name, attack, pp, hp, mp):
        self.name = name
        self.attack = attack
        self.pp = pp
        self.hp = hp
        self.mp = mp


class Enemy(object):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp


elemental_name = ['Chi', 'Mizu', 'Ka', 'Fu']
# (name, attack, pp, hp, mp)
arnie = Character('Arnie', 150, 120, 200, 120)
chunt = Character('Chunt', 180, 50, 125, 120)
usidore = Character('Usidore', 100, 100, 150, 300)
the_player = Character('Player',
                       random.randint(60, 150), random.randint(50, 150),
                       random.randint(80, 150), random.randint(50, 150))
charlist = [arnie, chunt, usidore, the_player]

# Bosses
monster = Enemy('Blemish', 20, random.randint(1500, 2000))
monster2 = Enemy('Orc General', 30, random.randint(2000, 2550))
monster3 = Enemy('The Dark Lord', 40, random.randint(2000, 3000))
monlist = [monster, monster2, monster3]

# Enemies
ooze = Enemy('Ooze', 20, 500)
skeleton = Enemy('Skeleton', 30, 500)
orc = Enemy('Orc', 40, 3000)
small_spider = Enemy('Spider', 20, 300)
goblin = Enemy('Goblin', 60, 2000)
bats = Enemy('Bat', 14, 655)
ghost = Enemy('Hunger Ghost', 50, 700)
snakes = Enemy('Snakes', 45, 450)
rock = Enemy('Magic Rock', 5, 10)
mushroom = Enemy('Mushroom', 10, 400)
agent = Enemy('Real Estate Agent', 25, 600)


def heal(person):
    if person.pp > 0:
        recovered = (person.mp + person.attack) * 0.5
        person.pp -= 5
        return round(recovered)
    else:
        print(person.name + ' is out of PP.')


def action_statement(person, action):
    print(person.name, action + '!')


def att(p1):
    attack = p1.attack + random.randint(2,6)
    return attack


def mag(p1):
    if p1.pp > 0:
        magic = (p1.attack + p1.mp) + random.randint(2, 3)
        p1.pp -= 5
        return magic
    else:
        print(p1.name+' is out of PP!')


def mon_att(mon, p1, p2, p3, p4):
    crit = random.randint(1, 100)
    turn = 0
    if crit > 20:
        num = random.randint(1, 11)

        if num == 1 or num == 5:
            dmg = att(mon)
            p1.hp -= dmg
            print('>The enemy attacks ' + p1.name)
            turn += 1
        elif num == 2 or num == 6:
            dmg = att(mon)
            p2.hp -= dmg
            print('>The enemy attacks ' + p2.name)
            turn += 1
        elif num == 3 or num == 7:
            dmg = att(mon)
            p3.hp -= dmg
            print('>The enemy attacks ' + p3.name)
            turn += 1
        elif num == 4 or num == 8:
            dmg = att(mon)
            p4.hp -= dmg
            print('>The enemy attacks ' + p4.name)
            turn += 1
        else:
            print(">The enemy missed!")
            turn += 1
    else:
        dmg = mon.attack * 4
        elemental = elemental_name[random.randint(0, 3)]
        print(mon.name + ' used ' + elemental + ' attack!')
        if elemental == elemental_name[0] or elemental_name[2]:
            p1.hp -= dmg
            p3.hp -= dmg

        elif elemental == elemental_name[1] or elemental_name[3]:
            p2.hp -= dmg
            p4.hp -= dmg


def player_status(person):
    print(person.name + " | HP = " + str(person.hp)
          + " | PP = " + str(person.pp))


def player_moves(player, mon, p2, p3, p4):
    turn = True
    attack = ['a', 'attack', 'Attack']
    magic = ['m', 'magic', 'MAGIC', 'Magic']
    heals = ['h', 'heal', 'HEAL', 'Heal']
    skip = ['skip', 's', 'SKIP']
    while turn:
        if player.hp < 0:
            print(player.name+' is unable to battle.')
            turn = False
        else:
            action = input('What will ' + player.name
                               + ' do? (Attack, Magic, Heal, Skip): ')

            if action in attack:
                damage = att(player)
                mon.hp -= damage
                print(player.name + ' did ' + str(damage) + ' damage.')
                turn = False
            elif action in magic:
                try:
                    damage = mag(player)
                    mon.hp -= damage
                    print(player.name + ' did ' + str(damage))
                    turn = False
                except:
                    print
            elif action in skip:
                print(player.name + ' decided to skip.')
                turn = False
            elif action in heals:
                try:
                    print("Who would you like " + player.name + " to heal?")
                    print("1: Arnie  |  2: Chunt  |  3: Usidore  |  4: Player")

                    user_heal = input('Who will he heal? (Type in the number before the name): ')
                    if user_heal == 'himself' or user_heal == player.name or user_heal == '1':
                        recovered = heal(player)
                        player.hp += recovered
                        action_statement(player, 'healed himself ' + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p2.name or user_heal == '2':
                        recovered = heal(player)
                        p2.hp += recovered
                        action_statement(player, 'healed ' + p2.name + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p3.name or user_heal == '3':
                        recovered = heal(player)
                        p3.hp += recovered
                        action_statement(player, 'healed ' + p3.name + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p4.name or user_heal == '4':
                        recovered = heal(player)
                        p4.hp += recovered
                        action_statement(player, 'healed ' + p4.name + ' '+str(recovered))
                        turn = False
                    else:
                        print("His mind slipped and he failed to heal!")
                        turn = False
                except:
                    print("Out of PP!")

            else:
                print("Please try that again")


def battle_system(p1, p2, p3, p4, mon):
    orginalhp = mon.hp
    alive = True
    print("\nYou encountered: " + mon.name + "!")
    while alive:
        print("+--------------------------------------------+")
        print("Enemy: " + mon.name + "   |   HP: "+str(mon.hp))
        print("+--------------------------------------------+")
        player_status(p1)
        player_status(p2)
        player_status(p3)
        player_status(p4)

        player_moves(p1, mon, p2, p3, p4)
        player_moves(p2, mon, p1, p3, p4)
        mon_att(mon, p1, p2, p3, p4)
        player_moves(p3, mon, p1, p2, p4)
        player_moves(p4, mon, p1, p2, p3)
        if p1.hp <= 0 and p2.hp <= 0 and p3.hp <= 0 and p4.hp <= 0:
            print('You lose')
            time.sleep(3)
            alive = False
            player_status(p1)
            player_status(p2)
            player_status(p3)
            player_status(p4)
            break

        if mon.hp <= 0:
            print('''
            ***************
            *   YOU WON   *
            ***************
            ''')
            time.sleep(1)
            alive = False
            mon.hp = orginalhp


def area(area, num_floors, boss):
    place = True
    while place:
        ran_num = random.randint(1,100)
        print("There are " + str(num_floors) + " floors remaining in the", area + "...")
        if num_floors == 1:
            print('''
            ***************
            * Final Boss! *
            ***************
            ''')
            time.sleep(2)

            battle_system(arnie, chunt, usidore, the_player, boss)
            place = False
        else:
            direction = input('Type in the first letter of Up/Down/Left/Right to move: ')
            if direction.lower() == 'up' or direction.lower() == 'u' or direction.lower() == 'Up' or direction.lower() == 'UP':
                print('>The party moved up')
                time.sleep(1)
                if ran_num <= 33:
                    battle_system(arnie, chunt, usidore, the_player, ooze)
                    num_floors -= 1
                elif ran_num > 33 and ran_num < 66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(arnie, chunt, usidore, the_player, skeleton)
                    num_floors -= 1
            elif direction.lower() == 'down' or direction.lower() == 'd' or direction.lower() == 'DOWN' or direction.lower() == 'Down':
                print(">The party moved down")
                time.sleep(1)
                if ran_num <= 15:
                    battle_system(arnie, chunt, usidore, the_player, orc)
                    num_floors -= 1
                elif ran_num > 15 and ran_num <= 33:
                    battle_system(arnie, chunt, usidore, the_player, ghost)
                    num_floors -= 1
                elif ran_num > 33 and ran_num < 66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(arnie, chunt, usidore, the_player, goblin)
                    num_floors -= 1
            elif direction.lower() == 'left' or direction.lower() =='l' or direction.lower() == 'Left' or direction.lower() == 'LEFT':
                print('>The party moved left')
                time.sleep(1)
                if ran_num <= 33:
                    battle_system(arnie, chunt, usidore, the_player, agent)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(arnie, chunt, usidore, the_player, snakes)
                    num_floors -= 1
            elif direction.lower() == 'right' or direction.lower() =='r' or direction.lower() == 'RIGHT':
                time.sleep(1)
                print('>The party moved right')
                if ran_num <= 33:
                    battle_system(arnie, chunt, usidore, the_player, bats)
                    num_floors -= 1
                elif ran_num > 33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(arnie, chunt, usidore, the_player, mushroom)
                    num_floors -= 1
            else:
                print('Wait... where?')
                time.sleep(2)


def welcome():
    print("****")
    print("Hello from the Magic Tavern!")
    print("In this quest, you'll help Arnie, Chunt\nand Usidore adventure through Foon...")
    print("Good luck!")
    print("*****")
    time.sleep(2)


def game_complete():
    print("*****")
    print("After defeating the dark lord, the party returns to the Vermillion Minitaur.\n")
    print("They record a new episode of the podcast and order is restored...")
    print("Thanks for playing!")
    print("*****")


# Main flow of the game
welcome()
print("After some time, you arrive at the Dungeon.")
time.sleep(2)
area('Dungeon', 3, monster)
print('The party obtains the Lunar Sword and leaves the dungeon.\n They make their way to the Haunted Woods.')
time.sleep(1)
print("You arrived at the Woods.")
area('Woods', 5, monster2)
print('After your victory, you obtain the ancient Goblin relic and move on.')
time.sleep(1)
print('There it is. The Dark Lord\'s tower.')
area('Tower', 10, monster3)
game_complete()
