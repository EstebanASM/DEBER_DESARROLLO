import openai

openai.api_key = "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"

hexadecimal = input('Ingresa el numero Hexadecimal: ')
prompt = f"Convertir el número hexadecimal {hexadecimal} a binario."

completion = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    n=1,
    temperature=0.2,
    stop=None
)

response = completion.choices[0].text
total_tokens = completion.usage.total_tokens
print(response)
print("El número de tokens utilizados son:", total_tokens)

