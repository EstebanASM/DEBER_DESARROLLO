import os

from llm.services.inferenceService import InferenceService


def main():
    while True:
      try:
        number= int(input("Ingrese el numero a convertir: "))
        result = InferenceService().invoke(number)
        print(result)
        break
      except ValueError:
        print("Ingrese un numero entero válido")





if __name__ == "__main__":
    main()