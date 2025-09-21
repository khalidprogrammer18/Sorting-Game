import random
while True:
    choice = input("\nChoose the difficulty ( Easy(E) - Meduim(M) - Hard(H) ) or closing(C): ").strip().lower()
    print()
    if choice == "easy" or choice == "e":
        words = ["apple","table","chair","light","house","river","smile","brick","cloud","dream"]
        num = random.choice(range(0,len(words)))
        word = list(words[num])
        random.shuffle(word)
    elif choice == "meduim" or choice == "m":
        words = ["circle","planet","bottle","friend","little","jungle","market","laptop","random","doctor"]
        num = random.choice(range(0,len(words)))
        word = list(words[num])
        random.shuffle(word)
    elif choice == "hard" or choice == "h":
        words = ["blanket","freedom","teacher","amazing","picture","balance","monster","fortune","bicycle","journey"]
        num = random.choice(range(0,len(words)))
        word = list(words[num])
        random.shuffle(word)
    elif choice == "closing" or choice == "c":
        break
    else:
        print("     ---<(You should choose a difficulty or closing)>---")
        continue
    print(f"The shuffled word is: {"-".join(word)}")
    answer = input("Enter your answer: ").strip().lower()
    if answer == words[num]:
        print("\n     ---<( You won good jop! )>---")
    else:
        print(f"\n     ---<( You lose, the word was ({words[num]}) )>---")