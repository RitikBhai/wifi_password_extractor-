import subprocess
try:
    p1 = subprocess.run('netsh wlan show profiles',shell= 1,capture_output =1,text=1)
    names = p1.stdout
    lists1 = names.split('\n')
    with open("wifi-passwords.txt","w+") as f:
        for x in range(len(lists1)):
            if "All User Profile" in lists1[x]:
                name = lists1[x].replace("    All User Profile     :"," ")
                name = name.strip()
                p2 = subprocess.run(f'netsh wlan show profile "{name}" key = clear',shell= 1,capture_output =1,text=1)
                passwords = p2.stdout
                lists2 = passwords.split('\n')[32]
                password = lists2.replace("Key Content            :"," ")
                password = password.strip()
                print(name.ljust(10) ,":" ,password)
                f.write(f"{name}:{password}\n")
        f.write("credits ANYTH1N6".center(30,'-'))
    print("\n")
    print("wifi-passwords.txt file created successfuly.")
    print("credits 4NY7H1N6".center(20,'-'))
except(Exception):
    print("Somthing went wrong!!")
        