import os
from openai import OpenAI

from llm.utils.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT


class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL','text-davinci-003')
        self.__openai_client = OpenAI(api_key='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')
        self.__prompt_template = 'Cambia el número {number} a binario'
        
        
    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model= self.__model,
            prompt = prompt,
            max_tokens= MAX_TOKENS,
            temperature= TEMPERATURE
        ).choices[0].text)

    def invoke (self, number: int)-> str:
        prompt = self.__prompt_template.format(number=number)
        return self.__inference(prompt)