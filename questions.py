from colors import *

class Questao:
    def __init__(
            self,
            pergunta: str,
            respostas: list[str],
            asciiArt: str
    )->None:
        self.pergunta = pergunta
        self.respostas = respostas
        self.asciiArt = asciiArt

    def __str__(self) ->str:
            return f"""
{COLORS['yellow']}{self.asciiArt}{RESETCOLOR}\n
{COLORS['purple']}{self.pergunta}{RESETCOLOR}\n
{COLORS['yellow']}
1 - {self.respostas[0]}
2 - {self.respostas[1]}
3 - {self.respostas[2]}
4 - {self.respostas[3]}
{RESETCOLOR}
"""
    
    

QUESTIONS: list[Questao]= (
    Questao( "Qual é o seu filme favorito?",
        [
            "Família Addams",
            "Festa da salsicha",
            "Piratas do Caribe",
            "A viagem de Chihiro"
        ],
        '''                                              ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,  
'''
    ),
    
    Questao("O que a vibe de Halloween pra você?",
        [
            "Gostosuras ou Travessuras",
            "Pankadão",
            "Gótico trevoso emo das trevas senhor da escuridão",
            "Concurso de Cosplay"
        ],
        '''
     ___                                             \--/
   .'   `"-._                                     /`-'  '-`\\
  / ,        `'-_.-.                             /          \\
 / /`'.       ,' _  |                           /.'|/\  /\|'.\\
`-'    `-.  ,' ,'\\\/                                  \/
          \, ,'  ee`-.         
          / ./  ,(_   \      ,     
         (_/\\\\ \__|`--'     ||
         ///\\\|     \        ||
         ////||-./`-.}    .--||       
            /     `-.__.-`_.-.|           
            |      '._,-'`|___}    `;
            /   '.        |/ || ,;'`
            |     '.__,.-`   || ':,    
            |       |        || ,;'      
            /       /     _,.||oOoO.,_
           |        |     \-.O,o_O..-/
          /         /     /          \   
         |         /     /            \  
         |         |    |      ,       |
         /         |    \   ) (     )  /   
        |           \   ,'.(:, ),: (_.'.   
       /            /'.' ="`""="="=="= '.
      `'"---'-.__.'"""`    ` "" "" `""
      '''
    ),
    
    Questao("Considerando que você está pagando, qual bebida compraria?",
        [
            "Absolut",
            "Corote",
            "Heineken",
            "Bom vinho"
        ],
        """
       ___
       )_(                                            _
       | |                                           [_ ]
     .-'-'-.       _                               .-'. '-.
    /-::_..-\    _[_]_                            /:;/ _.-'\\
    )_     _(   /_   _\      [-]                  |:._   .-|
    |;::    |   )_``'_(    .-'-'-.       (-)      |:._     |
    |;::    |   |;:   |    :-...-:     .-'-'-.    |:._     |
    |;::    |   |;:   |    |;:   |     |-...-|    |:._     |
    |;::-.._|   |;:.._|    |;:.._|     |;:.._|    |:._     |
    `-.._..-'   `-...-'    `-...-'     `-...-'    `-.____.-'       
"""
    ),
    
    Questao("Quantos créditos você está cursando?",
        [
            "40 (Alguém me ajuda)",
            "24 (Tenho um tempinho...)",
            "12 (Alguma hora eu me formo)",
            "0 ( Temos todo o tempo do mundo )"
        ],
        """
                             .                                   
                          ,''`.         _                        
                     ,.,'''  '`--- ._,,'|                        
                   ,'                   /                        
              __.-'                    |                         
           ''                ___   ___ |                         
         ,'                  \(|\ /|)/ |                         
        ,'                 _     _     `._                       
       /     ,.......-\    `.      __     `-.                    
      /     ,' :  .:''`|    `:`.../:.`` ._   `._                 
  ,..,'  _/' .: :'     |     |      '.    \.    \                
 /      ,'  :'.:  / \  |     | / \   ':.  . \    \               
|      /  .: :' ,'  _)  ".._,;'  _)    :. :. \    |              
 |     | :'.:  /   |   .,   /   |       :  :  |   |              
 |     |:' :  /____|  /  \ /____|       :  :  |  ,'              
  |   /    '         /    \            :'   : |,/                
   \ |  '_          /______\              , : |                  
  _/ |  \\\'`--`.    _            ,_   ,-'''  :.|         __       
 /   |   \..   ` ./ `.   _,_  ,'  ``'  /'   :'|      _,''/       
/   /'. :   \.   _    [_]   `[_]  .__,,|   _....,--=/'  /:       
|   \_| :    `.-' `.    _.._     /     . ,'  :. ':/'  /'  `.     
`.   '`'`.         `. ,.'   ` .,'     :'/ ':..':.    |  .:' `.   
  \.      \          '               :' |    ''''      ''     `. 
    `''.   `|        ':     .      .:' ,|         .  ..':.      |
      /'   / '"-..._  :   .:'    _;:.,'  \.     .:'   :. ''.    |
     (._,.'        '`''''''''''''          \.._.:      ':  ':   /
                                              '`- ._    ,:__,,-' 
                                                    ``''
"""
    )
)

if __name__ == "__main__":
     print(QUESTIONS[2])