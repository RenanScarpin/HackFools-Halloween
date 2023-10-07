from time import sleep
from os import system
from colors import *
from questions import QUESTIONS
from costumes import COSTUMES, Costume

NAME = "HALLOWEEN3000"

def interfaceStart()->None:
    system("clear")
    print(COLORS["yellow"],"""
.___,_______,_____Happy_Halloween____.
| ./(       )\.        |             |
| )  \/\_/\/  (        |             |
| `)  (^Y^)  (`      \(|)/           |
|  `),-(~)-,(`      --(")--          |
|      '"'      \\    /`\            |
|          .-'```^```'-.    ,     ,  |
|         /   (\ __ /)  \   )\___/(  |
|         |    ` \/ `   |  {(@)v(@)} |
|         \    \____/   /   {|~~~|}  |
|          `'-.......-'`    {/^^^\}  |
.____________________________`m-m`___.
      """, RESETCOLOR)
    sleep(1)
    #system("clear")
    print(f"{COLORS['purple']}------BEM VINDO À {COLORS['yellow']}{NAME}{COLORS['purple']}!------{RESETCOLOR}\n")
    sleep(1)
    print("Precisa de uma fantasia e não sabe o que usar?")
    sleep(1)
    print("Deixa com a gente!\n")
    sleep(1)
    print("Responda essas perguntas e a gente te recomenda uma fantasia!")
    sleep(1)
    input("(PRESSIONE ENTER PARA COMEÇAR)")

def Ask(index: int)->int:
    system("clear")
    print(QUESTIONS[index],end="")
    return int(input("Digite a sua resposta:\n"))

def Result(costume: Costume)->None:
    system("clear")
    print(f"{COLORS['yellow']}E a sua fantasia é:{RESETCOLOR}\n")
    sleep(1)

    print(COLORS['purple'], end="")
    for i in range(1,6):
        print("CALCULANDO" + "."*i, end='\r')
        sleep(1.2)
    print(RESETCOLOR,end="")
    system("clear")
    print(costume)


def main()->None:
    Result(COSTUMES[3])

if __name__ == "__main__":
    main()