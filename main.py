from ai import call_gpt
import random 
import time

def  vault_art():
    print("""
     ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓████████▓▒░ 
        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     
        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░              ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     
        ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░         ░▒▓█▓▒▒▓█▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     
        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░               ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     
        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░               ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     
        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░         ░▒▓██▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░                                                                                                         
    """)

def access():
                print("""
              ████╗  ██████╗ ██████╗███████╗███████╗███████╗     ██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ 
            ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
            ███████║██║     ██║     █████╗  ███████╗███████╗    ██║  ███╗███████║██║██╔██╗ ██║█████╗  ██║  ██║
            ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║    ██║   ██║██╔══██║██║██║╚██╗██║██╔══╝  ██║  ██║
            ██║  ██║╚██████╗╚██████╗███████╗███████║███████║    ╚██████╔╝██║  ██║██║██║ ╚████║███████╗██████╔╝
            ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═════╝ """)

def deny():
                    print("""
                ██╗   ██╗███╗   ██╗ █████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ██████╗ ██╗███████╗███████╗██████╗     
                ██║   ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗██║╚══███╔╝██╔════╝██╔══██╗    
                ██║   ██║██╔██╗ ██║███████║██║   ██║   ██║   ███████║██║   ██║██████╔╝██║  ███╔╝ █████╗  ██║  ██║    
                ██║   ██║██║╚██╗██║██╔══██║██║   ██║   ██║   ██╔══██║██║   ██║██╔══██╗██║ ███╔╝  ██╔══╝  ██║  ██║    
                ╚██████╔╝██║ ╚████║██║  ██║╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║██║███████╗███████╗██████╔╝    
                ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝     
                                                                                                                    
                █████╗  ██████╗ ██████╗███████╗███████╗███████╗                                                     
                ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝                                                     
                ███████║██║     ██║     █████╗  ███████╗███████╗                                                     
                ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║                                                     
                ██║  ██║╚██████╗╚██████╗███████╗███████║███████║                                                     
                ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝                                                     
                                                                                                                    
                ██████╗ ███████╗███╗   ██╗██╗███████╗██████╗                                                         
                ██╔══██╗██╔════╝████╗  ██║██║██╔════╝██╔══██╗                                                        
                ██║  ██║█████╗  ██╔██╗ ██║██║█████╗  ██║  ██║                                                        
                ██║  ██║██╔══╝  ██║╚██╗██║██║██╔══╝  ██║  ██║                                                        
                ██████╔╝███████╗██║ ╚████║██║███████╗██████╔╝                                                        
                ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝╚═════╝                                                         """)

def welcome():
    print("""WELCOME TO THE VAULT TERMINAL\n
    Here you will have to open the vault by guessing the password. You have four levels.
    Each level the ciphered password will be shown. You will have to figure out which cipher it is and 
    DECIPHER it...Feel free to find cipher translators online and try guessing which type it is and 
    eventually get HOLD OF THE DECIPHERED TEXT!!!!!
    If you are stuck after 3 attempts you can opt for a HINT.
    BE CAREFUL AND WARY OF OPENING THE VAULT. 
    I CAN'T GUARANTEE YOUR SAFETY
    
                                                        ~Nandhu """)

def puzzlerun(prompt,answer,code):
    print(">"+prompt)
    at=int(0)
    while at<3:
        ans=input(">Enter password:").strip().upper()
        if answer==ans:
            access()
            return True 
        else:
                deny()
                time.sleep(2)
                print("!! SYSTEM ERROR !! \n")
                at=at+1
                print("\n Attempt no:", at, "out of 3 \n")
                time.sleep(2)
    a = input("You failed 3 times. Do you want a HINT? (yes/no): ").strip().lower()
    if a == "yes":
        print("HINT: " + code)
        ans = input(">Try again: ").strip().upper()
        if ans == answer:
               access()
               return True
        else:
            deny()
            return False

def gain():
      print("""
 ▓██   ██▓ ▒█████   █    ██     ██░ ██  ▄▄▄    ██▒   █▓▓█████    
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██░ ██▒▒████▄ ▓██░   █▒▓█   ▀    
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██▀▀██░▒██  ▀█▄▓██  █▒░▒███      
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█ ░██ ░██▄▄▄▄██▒██ █░░▒▓█  ▄    
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▓█▒░██▓ ▓█   ▓██▒▒▀█░  ░▒████▒   
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░   
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ░  ░   
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░  ░░ ░  ░   ▒     ░░     ░      
 ░ ░         ░ ░     ░         ░  ░  ░      ░  ░   ░     ░  ░   
 ░ ░                                              ░             
  ▄████  ▄▄▄       ██▓ ███▄    █ ▓█████ ▓█████▄                 
 ██▒ ▀█▒▒████▄    ▓██▒ ██ ▀█   █ ▓█   ▀ ▒██▀ ██▌                
▒██░▄▄▄░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒▒███   ░██   █▌                
░▓█  ██▓░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ░▓█▄   ▌                
░▒▓███▀▒ ▓█   ▓██▒░██░▒██░   ▓██░░▒████▒░▒████▓                 
 ░▒   ▒  ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▒▓  ▒                 
  ░   ░   ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░ ░ ▒  ▒                 
░ ░   ░   ░   ▒    ▒ ░   ░   ░ ░    ░    ░ ░  ░                 
      ░       ░  ░ ░           ░    ░  ░   ░                    
                                         ░                      
 ▄▄▄       ▄████▄   ▄████▄  ▓█████   ██████   ██████            
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒██    ▒            
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒███   ░ ▓██▄   ░ ▓██▄              
░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒           
 ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░▒████▒▒██████▒▒▒██████▒▒           
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░           
  ▒   ▒▒ ░  ░  ▒     ░  ▒    ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░           
  ░   ▒   ░        ░           ░   ░  ░  ░  ░  ░  ░             
      ░  ░░ ░      ░ ░         ░  ░      ░        ░             
          ░        ░                                            """)
def Haunt():
    print("""
▄█ █▀▄▀█       ▄▀  ████▄    ▄      ▄   ██       
██ █ █ █     ▄▀    █   █     █      █  █ █      
██ █ ▄ █     █ ▀▄  █   █ ██   █ ██   █ █▄▄█     
▐█ █   █     █   █ ▀████ █ █  █ █ █  █ █  █     
 ▐    █       ███        █  █ █ █  █ █    █     
     ▀                   █   ██ █   ██   █      
                                        ▀       
 ▄  █ ██     ▄      ▄     ▄▄▄▄▀                 
█   █ █ █     █      █ ▀▀▀ █                    
██▀▀█ █▄▄█ █   █ ██   █    █                    
█   █ █  █ █   █ █ █  █   █                     
   █     █ █▄ ▄█ █  █ █  ▀                      
  ▀     █   ▀▀▀  █   ██                         
       ▀                                        
▀▄    ▄ ████▄   ▄                               
  █  █  █   █    █                              
   ▀█   █   █ █   █                             
   █    ▀████ █   █                             
 ▄▀           █▄ ▄█                             
               ▀▀▀                              
                                                
    """)
def main():
    vault_art()
    time.sleep(2)
    welcome()
    time.sleep(2)
    puzzles = [
        ("KHOOR", "HELLO", "Decrypt Caesar Cipher"),
        ("01000001 01001001", "AI", "Binary"),
        ("48 41 49 4B 55", "HAIKU", "Hex"),
        ("UEFTU1dPUkQ=", "PASSWORD", "Base64"),
        ("MWQ", "CPI", "Vigenère (KEY) ")
    ]
    for prompt, answer,code in puzzles:
         while not puzzlerun(prompt, answer, code):
            pass
    print("VAULT UNLOCKED.\n")
    time.sleep(2)
    print("YOU SHOULD NOT HAVE DONE THAT.\n")
    time.sleep(1.5)
    gain()
    time.sleep(5)
    gpt=call_gpt("You are a scary, broken AI that has just been hacked. The user broke into a secret vault, and now you are angry. \
     Write a creepy and spooky threat to the user.Make it sound like the AI is watching them and something bad is about to happen. \
     The message should feel scary, like in a horror movie. Use around 100 words.")
    print(gpt)
    Haunt()
    time.sleep(5)
    vault_art()
    print("""
    ------------------------------------------------------------------------------------------------------------------------
    tysm :)
    hope you liked the game
                                 ~Srinandhini Saravanan (Nandhu)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")



if __name__ == "__main__":
    main()
