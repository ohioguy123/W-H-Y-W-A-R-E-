import webbrowser
import os

def print_blue(text):
    print("\033[94m" + text + "\033[0m")

def print_red(text):
    print("\033[91m" + text + "\033[0m")

def print_green(text):
    print("\033[92m" + text + "\033[0m")

def unblocked_nsfw_website():
    print_green('pornhub.com')

def government_leaks():
    print_blue('http://intelrepository.com/?i=1')

def hire_a_hitman():
    print_blue('http://hitman2xnfbcaaodfv6s2s5yagerqvb4cli2xeyoljhcf4yfvaa63ryd.onion/')

def china_leaks():
    print_blue('http://tirxscsg3pcenlff67ecn2kb3jfv3ori7bgwryyn7btktohfdkms2cyd.onion/')

def dark_web_hacker_for_hire():
    print_blue('http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion/')

def fake_ids():
    print_blue('http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion/')

def destroy_psycho_clubs():
    print_blue('http://destroy2wnzdx7oiqwsry4ixhwkpype5b2rcfr6fxdstjwlfiwnwcxid.onion/')

def nsfw_website():
    print_blue('https://rule34.xxx/index.php?page=post&s=list&tags=komi-san_wa_komyushou_desu')

def dog_sex():
    print_blue('http://dogsexwnsitn2dpfor7l65vdwgaxssbszuhifni7qbt4gxnow2e3ezqd.onion/')

def hi():
    print_blue('http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion')

def tom_and_jerry():
    print_blue('http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/')

def bitcoin_buyer():
    print_blue('http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/')

def webuybitcoins():
    print_blue('http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion')

def hotdog():
    print_blue('http://spywaredrcdg5krvjnukp3vbdwiqcv3zwbrcg6qh27kiwecm4qyfphid.onion')

def custom():
    print_blue('http://ho2hua2hfduv6f7hcbzdj2e6qdn4szgyy2jjnx545v4z3epq7uyrscid.onion/')

def warez():
    print_blue('http://warezmkywr5hx6rucpnueupwmklyrliavddzj2rdkgnunr4gs3d67gad.onion/')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_options():
    print_red('01. Unblocked NSFW Website')
    print_red('02. Government Leaks')
    print_red('03. Hire a Hitman')
    print_red('04. China Leaks')
    print_red('05. Dark Web Hacker for Hire')
    print_red('06. Fake IDs')
    print_red('07. Destroy Psycho Clubs')
    print_red('08. NSFW Website')
    print_red('09. Dog Sex')
    print_red('10. Meth&Drugs')
    print_red('11. Tom And Jerry')
    print_red('12. Bitcoin Buyer')
    print_red('13. WeBuyBitcoins')
    print_red('14. Spyware Watchdog')
    print_red('15. Satanic Ceremony')
    print_red('16. Warez Dark Web')
    print_red('99. Exit')
    print_red('')

def main():
    while True:
        clear_screen()
        print('\033[95m' + '''
    ██╗    ██╗██╗  ██╗██╗   ██╗██╗    ██╗ █████╗ ██████╗ ███████╗
    ██║    ██║██║  ██║╚██╗ ██╔╝██║    ██║██╔══██╗██╔══██╗██╔════╝
    ██║ █╗ ██║███████║ ╚████╔╝ ██║ █╗ ██║███████║██████╔╝█████╗  
    ██║███╗██║██╔══██║  ╚██╔╝  ██║███╗██║██╔══██║██╔══██╗██╔══╝  
    ╚███╔███╔╝██║  ██║   ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗
     ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                     Made By: Marsx
                                                                      \033[0m''')
        print_options()
        print('\033[92m' + 'Enter your choice: ' + '\033[0m', end='')
        choice = input()

        if choice == '1':
            unblocked_nsfw_website()
        elif choice == '2':
            government_leaks()
        elif choice == '3':
            hire_a_hitman()
        elif choice == '4':
            china_leaks()
        elif choice == '5':
            dark_web_hacker_for_hire()
        elif choice == '6':
            fake_ids()
        elif choice == '7':
            destroy_psycho_clubs()
        elif choice == '8':
            nsfw_website()
        elif choice == '9':
            dog_sex()
        elif choice == '10':
            hi()
        elif choice == '11':
            tom_and_jerry()
        elif choice == '12':
            bitcoin_buyer()
        elif choice == '13':
            webuybitcoins()
        elif choice == '14':
            hotdog()
        elif choice == '15':
            custom()
        elif choice == '16':
            warez()
        elif choice == '99':
            print_red('http://bit.ly/3tjP8hM')
            exit()
        else:
            webbrowser.open(choice)

        input('\nPress Enter to continue...')

if __name__ == '__main__':
    main()