from costumes import COSTUMES, Costume
def predict(answers: list[int]):
    if answers[1] == 1:
        return COSTUMES[2]
    
    if answers[1] == 2:
        return COSTUMES[0]
        
    if answers[1] == 3:
        return COSTUMES[3]
    
    if answers[1] == 1:
        return COSTUMES[1]
