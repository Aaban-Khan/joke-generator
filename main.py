import time
import os
import sys
from colorama import Fore,Style
import requests
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def fetching_info():
    print("\n")
    print(f"{Fore.YELLOW}🔀 Fetching Data{Style.RESET_ALL}", end="")
    for _ in range(10):
        print(f"{Fore.YELLOW}.{Style.RESET_ALL}", end="", flush=True)
        time.sleep(0.03)
    print("\n")

    try:
        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political,explicit&type=single"
        r = requests.get(url)

        if r.status_code == 200:

            data = r.json()
            joke = data.get('joke', 'N/A')

            print(f"{Fore.CYAN}Joke - {joke} {Style.RESET_ALL}")
            return joke
        else:
            print("❗Failed to Fetch Joke")
            return None,None

    except Exception as e:
        print(f"❗Error: {e}")
        return None , None

def saving_data(joke_count, joke):
    if not joke:
        return
    
    if not os.path.exists('database'):
        os.makedirs('database')

    file_name = f"database/quotes_{datetime.now().strftime('%b-%d-%Y')}.txt"
    file_time = datetime.now().strftime('%I:%M:%S %p')

    if joke_count == 1:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"# Saving Data....\n\n")

    with open(file_name,"a", encoding="utf-8") as file:
        file.write(f"{joke_count}) {joke}! At {file_time}\n\n")

def main():
    typewriter("😂 Random Joke Generator 😂")
    time.sleep(0.5)
    joke_count = 0 

    while True:
        user = input("Enter(y) to generate a Joke(y/n): ").lower() if joke_count == 0 else input("Do you Want to generate it Again?(y/n): ").lower()
        if user == "y":
            if joke_count != 0:
                clear_screen()
            
            joke = fetching_info()

            if joke:
                joke_count += 1
                saving_data(joke_count, joke)
        
        elif user == "n":
            print(f"\n{Fore.LIGHTBLACK_EX}You generate {joke_count} Jokes!!{Style.RESET_ALL}")
            typewriter("Exiting...Have a Great Day")
            time.sleep(0.02)
            break
            
        else:
            print("❗Please enter 'y' or 'n'")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()