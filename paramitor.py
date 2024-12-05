import random
import os
import time
import sys
from googlesearch import search
import urllib.error

# Banner/Logo
logo = """
      \033[1;104mTHIS TOOLS IS EDUCATIONAL PURPOSES ONLY\033[0;37m     
\033[1;36m           WELCOME TO GHOST WORLD🌎💀
\033[31;1m╔══════════════════════════════════════════════╗
\033[31;1m║\033[32;1m  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗\033[31;1m  ║
\033[31;1m║\033[32;1m ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝\033[31;1m  ║
\033[31;1m║\033[32;1m ██║  ███╗███████║██║   ██║███████╗   ██║\033[31;1m     ║
\033[31;1m║\033[32;1m ██║   ██║██╔══██║██║   ██║╚════██║   ██║\033[31;1m     ║
\033[31;1m║\033[32;1m  ██████╔╝██║  ██║╚██████╔╝███████║   ██║\033[1;37mV.6.9\033[31;1m║
\033[31;1m║\033[32;1m  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝\033[31;1m     ║
\033[31;1m║\033[32;1m   \033[1;36m[\033[1;34m!\033[1;36m]  \033[1;35mTOOLS CREATE BY TH3 EL1T3 GH0ST \033[31;1m      ║
\033[31;1m╚══════════════════════════════════════════════╝
\033[1;36m  Tools Name : GHOST WEBSITE HACKING TOOLS
\033[1;37m             TYPE :  GIFT
 \033[1;33m# Telegram: https://t.me/TH3EL1T3GH0STOFFICIAL
\033[1;34m           Coding By: @TH3EL1T3GH0ST
\033[1;35m═══════════════════════════════════════════════
"""

# Function to log results
def logger(filename, data):
    with open(filename + ".txt", "a") as file:
        file.write(str(data) + "\n")
os.system('clear')
os.system('espeak -a 300 "welcome to ghost, word opening, dorc to paramitor finder tools,,''')
os.system('xdg-open https://t.me/TH3EL1T3GH0STOFFICIAL')
def main():
    print(logo)
    try:
        # Prompt to save the project
        resultdork = input("\033[32;1m Would you want to save the project? Y/N: ").strip().lower()
        loges = ""

        if resultdork == "y":
            loges = input("Enter the name for the log file: ").strip()
        else:
            print("Skipped saving the project.")

        # Collecting search inputs
        dork = input("\033[1;34m\nEnter Dork: ").strip()
        numr = input("Number of Results (1-100): ").strip()

        try:
            requ = 0
            counter = 0

            print("\033[1;36m\nStarting search...\n")
            for results in search(dork, tld="com", lang="en", num=int(numr), start=0, stop=None, pause=2):
                rand_user = random.choice(["Mozilla/5.0", "Chrome/91.0"])  # Example user agents
                counter += 1
                print(f" \033[31;1m[{counter}] : \033[1;36m{results} \033[32;1m<Found ")
                time.sleep(0.5)
                requ += 1

                # Save results to log if opted
                if loges:
                    logger(loges, results)

                if requ >= int(numr):
                    break

        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("[Error 429] Too many requests. Please try again later.")
                sys.exit()

        print("\nSearch Completed.")
        print("\t\t\tTH3 EL1T3 GH0ST\n")
    except KeyboardInterrupt:
        print("\n\nInterrupt detected. Exiting program.")
        sys.exit()

if __name__ == "__main__":
    main()
