from termcolor import colored
import time

banner='''
            ┏━━━┓━━┏━━━┓
            ┃┏━┓┃━━┃┏━┓┃
            ┃┃━┃┃━━┃┗━┛┃
            ┃┗━┛┃━━┃┏━━┛  
            ┃┏━┓┃┏┓┃┃━━━
            ┗┛━┗┛┗┛┗┛━━━
            ━━━━━━━━━━━━
            ━━━━━━━━━━━━
'''

print(colored(banner, "light_red",attrs=['bold']))

caption='''
this toos is made for  some mathematical calculation of (A.P).
 
    [A] enter first term
    [B] enter common diffrence
    [C] enter no of terms
    [D] enter last term
    '''
    

permission=input(colored("do you want to continue [y/n] : ", "light_yellow"))

print()
print()
print(colored("DEVLOP BY :", "light_yellow", "on_light_red"), colored(" khalidx456", "light_cyan"))

print(colored(caption, "light_blue"))

print(colored("Note", "light_yellow", "on_red"),colored(": if value is not given then press enter.", "white"))
print()

if permission=="y":
    time.sleep(0.3)
    
    while True:
        first_terms=int(input(colored("first term : ", "light_green")))
        common_diff=int(input(colored("Common diffrence of : ", "light_green")))
        nterms=input(colored("no of terms n : ", "light_green"))
        last_terms=input(colored("last term : ", "light_green"))
        
        if last_terms=="":
            nA=[]
            calc_last_terms=first_terms+(int(nterms)*common_diff)-common_diff
            for termsA in range(first_terms,calc_last_terms+1,common_diff):
                nA.append(termsA)
            print()
            print(colored("A.P = ", "light_yellow"),colored(nA, "light_cyan"))
           
            
            print(colored("n terms = ", "light_yellow"), colored(len(nA), "light_green"))
            print()
            
        elif nterms=="":
            nB=[] 
            for termsB in range(first_terms,int(last_terms)+1,common_diff):
                nB.append(termsB) 
                
            print()
            print(colored("A.P = ", "light_yellow"),colored(nB, "light_cyan"))
            
            print(colored("n terms = ", "light_yellow"), colored(len(nB), "light_green"))
            print()
            
        else:
            nC=[] 
            for termsC in range(first_terms,int(last_terms)+1,common_diff):
                nC.append(termsC) 
                
            print()
            print(colored("A.P = ", "light_yellow"),colored(nC, "light_cyan"))
            
            print(colored("n terms = ", "light_yellow"), colored(len(nC), "light_green"))
            print()
            
            
        print(colored("Thanks !!", "light_red"))       
        print()       
        print()     
else:
    exit
    