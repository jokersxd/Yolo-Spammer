from colorama import Fore, init, Style
import threading
import requests
import ctypes
import os

os.system('cls')
init(convert=True, autoreset=True)
lock = threading.Lock()
SentCounter = 0
ErrorCounter = 0
ctypes.windll.kernel32.SetConsoleTitleW('Yolo Spammer | Developed by jokers')
print(Fore.WHITE + Style.BRIGHT + 'URL Code:')
URLCode = str(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(Fore.WHITE + Style.BRIGHT + '\nMessage:')
message = str(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(Fore.WHITE + Style.BRIGHT + '\nThreads:')
threads = int(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(Fore.WHITE + Style.BRIGHT + '\nAmount:')
amount = int(input(Fore.YELLOW + '> ' + Fore.WHITE + Style.BRIGHT))
print(' ')

def Spammer():
    global SentCounter
    global ErrorCounter
    try:
        session = requests.Session()
        headers = {
            'path': '/' + str(URLCode) + '/message',
            'content-type': 'application/json;charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        data = '{"text":"' + str(message) + '","cookie":"5w5j5djvvk3snnf5llrrfo","wording":"Send honest messages"}'
        POST = session.post('https://onyolo.com/' + str(URLCode) + '/message', headers=headers, data=data)
        if 'ok' in POST.text:
            SentCounter += 1
            lock.acquire()
            print(Fore.GREEN + '[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Sent message | #' + str(SentCounter))
            lock.release()
            ctypes.windll.kernel32.SetConsoleTitleW('Yolo Spammer | Sent: ' + str(SentCounter) + ' | Errors: ' + str(ErrorCounter) + ' | Developed by jokers')
        elif 'Forbidden' in POST.text:
            ErrorCounter += 1
            lock.acquire()
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Ratelimited')
            lock.release()
            ctypes.windll.kernel32.SetConsoleTitleW('Yolo Spammer | Sent: ' + str(SentCounter) + ' | Errors: ' + str(ErrorCounter) + ' | Developed by jokers')
        else:
            print(POST.text)
    except Exception as e:
        print(e)

for i in range(amount):
    threading.Thread(target=Spammer, args=()).start()
