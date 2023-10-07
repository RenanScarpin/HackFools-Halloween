from interface import *
from predict import predict

def main():
    answers: list[int] = []

    interfaceStart()
    for i in range(len(QUESTIONS)):
        answers.append(Ask(i))
    costume = predict(answers)
    Result(costume)

    
    
    




if __name__ == "__main__":
    main()