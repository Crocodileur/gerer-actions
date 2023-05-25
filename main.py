import json
from termcolor import colored
import json
import yfinance as yf
import os
import shutil
import traceback


###############################################################################################################
#                                                 CONSTANTES                                                  #
###############################################################################################################

ls_choice_menu = ['1','2','3','4']
ls_choice_sob = ['A','a','V','v']

ls_choice_menu_infos = ['1','2','3']
total_amount = 0
rdm = 0

###############################################################################################################
#                                               FONCTIONS                                                     #
###############################################################################################################

def print_centered(s):
    print('\n'*(int(shutil.get_terminal_size().lines/2)))
    print(s.center(shutil.get_terminal_size().columns))

def print_centered_nh(s):
    print(s.center(shutil.get_terminal_size().columns))

def print_main_menu():
    print('\n'*(int(shutil.get_terminal_size().lines/2)-8))
    list_menu = [(colored('[1] Ajouter une donnée\n', 'blue')),(colored('[2] Consulter les données\n', 'blue')),(colored('[3] Consulter vos actions actuelles\n', 'blue')),(colored('[4] Quitter le programme\n', 'blue'))]
    for x in list_menu:
        print(x.center(shutil.get_terminal_size().columns))

def input_centered(s):
    value = input(s.rjust((int(shutil.get_terminal_size().columns))//2))
    return value

def write_json(dico, f='datas.json'):
    with open(f,'w') as file: 
        file_data = json.dump(dico, file) # On écrit les données

def get_json(f='datas.json'):
    with open(f) as json_file: 
        data = json.load(json_file) # On récupère le JSON
    return data # On retourne le JSON (format DICTIONNAIRE)


###############################################################################################################
#                                                  MAIN                                                       #
###############################################################################################################

while True:
    try:
        if os.path.exists('datas.json') == False: # Si le fichier settings n'existe pas, on le crée.
            settings = open('datas.json', 'w')
            settings.write('{}')
            settings.close()
        else: # Si le fichier settings existe
            try:
                while True:
                    os.system('cls')
                    print_main_menu()
                    choice_menu = input_centered('Choix : ')
                    if choice_menu in ls_choice_menu:
                        break
                if choice_menu == '1': # Ajouter une donnée
                    while True:
                        os.system('cls')
                        print_centered(colored('Avez vous acheté ou vendu une action ? (A/V)\n', 'green'))
                        print_centered_nh(colored('X pour retour\n', 'light_magenta'))
                        choice_sob = input_centered('Choix : ')
                        if choice_sob == 'x' or choice_sob == 'X':
                            break
                        if choice_sob in ls_choice_sob:
                            break
                    datas = get_json()
                    if choice_sob == 'A' or choice_sob == 'a':
                        os.system('cls')
                        print_centered(colored('Saisissez le mini-nom de(s) l\'action(s) achetée(s) : \n', 'green'))
                        print_centered_nh(colored('X pour retour\n', 'light_magenta'))
                        choice_name_action = input_centered('Choix : ')
                        if choice_name_action == 'x' or choice_name_action == 'X':
                            continue
                        while True:
                            os.system('cls')
                            print_centered(colored('Saisissez le nombre d\'action(s) acheté(s) : \n', 'green'))
                            print_centered_nh(colored('X pour retour\n', 'light_magenta'))
                            choice_amount_action = input_centered('Choix : ')
                            if choice_amount_action == 'X' or choice_amount_action == 'x':
                                rdm = 1
                                break
                            try:
                                choice_amount_action = int(choice_amount_action)
                                break
                            except:
                                pass

                        if rdm == 1:
                            rdm = 0
                            continue
                        # Traitement et remplacement / ajout dans le JSON
                        

                        if choice_name_action in datas:
                            os.system('cls')
                            # L'actions choisie est déjà dans le JSON --> on l'ajoute.
                            print_centered(colored('Nombre d\'actions : \n', 'cyan'))
                            print_centered_nh((colored(datas[choice_name_action],'white', 'on_red'))+(colored(' --> ', 'white'))+(colored(datas[choice_name_action] + int(choice_amount_action),'white', 'on_green'))+'\n')
                            datas[choice_name_action] = datas[choice_name_action] + int(choice_amount_action)
                        
                            write_json(datas)
                            input_centered(colored('Continuer...', 'white'))
                            
                        else:
                            os.system('cls')
                            datas[choice_name_action] = int(choice_amount_action)
                            write_json(datas)
                            print_centered(colored('Nombre d\'actions : \n', 'cyan'))
                            input_centered(colored('Continuer...', 'white'))
                            print_centered_nh((colored('0','white', 'on_red'))+(colored(' --> ', 'white'))+(colored(int(choice_amount_action),'white', 'on_green'))+'\n')
                    elif choice_sob == 'v' or choice_sob == 'V':
                        os.system('cls')
                        print_centered(colored('Saisissez le mini-nom de(s) action(s) vendue(s) : \n', 'green'))
                        print_centered_nh(colored('X pour retour\n', 'light_magenta'))
                        choice_name_action = input_centered('Choix : ')
                        if choice_name_action == 'x' or choice_name_action == 'x':
                            continue
                        while True:
                            os.system('cls')
                            print_centered(colored('Saisissez le nombre d\'action(s) vendue(s) : \n', 'green'))
                            print_centered_nh(colored('X pour retour\n', 'light_magenta'))
                            choice_amount_action = input_centered('Choix : ')
                            if choice_amount_action == 'x' or choice_amount_action == 'X':
                                rdm = 1
                                break
                            try:
                                choice_amount_action = int(choice_amount_action)
                                break
                            except:
                                pass
                        if rdm == 1:
                            rdm = 0
                            continue
                        if choice_name_action in datas:
                            os.system('cls')
                            # L'actions choisie est déjà dans le JSON --> on l'ajoute.
                             
                            if datas[choice_name_action] < int(choice_amount_action):
                                print_centered((colored('Vous avez seulement ', 'red'))+(colored(datas[choice_name_action], 'cyan'))+(colored(' actions de ce type', 'red')))
                            else:
                                print_centered(colored('Nombre d\'actions : \n', 'cyan'))
                                print_centered_nh((colored(datas[choice_name_action],'white', 'on_green'))+(colored(' --> ', 'white'))+(colored(datas[choice_name_action] - int(choice_amount_action),'white', 'on_red'))+'\n')
                                datas[choice_name_action] = datas[choice_name_action] - int(choice_amount_action)
                                write_json(datas)
                            input_centered(colored('Continuer...', 'white'))
                        else:
                            os.system('cls')
                            print_centered(colored('Vous ne possédez aucune action de ce type', 'red'))
                if choice_menu == '2':
                    while True:
                        os.system('cls')
                        print('\n'*(int(shutil.get_terminal_size().lines/2)-5))
                        list_menu = [(colored('[1] Afficher les données générales\n', 'blue')),(colored('[2] Afficher les données par action\n', 'blue')),(colored('[3] Retour\n', 'blue'))]
                        for x in list_menu:
                            print(x.center(shutil.get_terminal_size().columns))
                        choice_menu_infos = input_centered('Choix : ')
                        if choice_menu_infos in ls_choice_menu_infos:
                            break
                    if choice_menu_infos == '1':
                        os.system('cls')
                        datas = get_json()
                        for key in datas:
                            try:
                                action = yf.Ticker(key)
                                datas_action = action.info
                                print_centered_nh(str(datas_action['longName']) + ' : ' + str(datas_action['currentPrice']) + '€/u')
                                total_amount = int(datas_action['currentPrice'])*datas[key]
                            except Exception:
                                print_centered_nh(key + ' n\'a pas été trouvé.') # L'action n'existe pas
                        print_centered_nh(('\nValeur totale : ') + str(colored((str(total_amount) + '€') + '\n', 'green')))
                        input_centered('Retour : ')
                    elif choice_menu_infos == '2':
                        os.system('cls')
                        print_centered(colored(('Pas encore disponible...'), 'cyan'))
                        input_centered('Retour : ')
                    elif choice_menu_infos == '3':
                        pass 

                if choice_menu == '3': 
                    os.system('cls')
                    datas = get_json()
                    for key in datas:
                        x = colored((key + ':' + str(datas[key]) + '\n'), 'light_cyan')
                        print(x.center(shutil.get_terminal_size().columns))
                    input_centered('Retour : ')
                if choice_menu == '4':
                    quit()
                    
            
            except ZeroDivisionError:
                print('Une erreur est survenue...')
                # A voir mais pourquoi pas print_main_menu()
                break
    except ZeroDivisionError:
        print('Erreur générale')
        break