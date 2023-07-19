import requests
import json

API_KEY="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"

def pesquisa_GPT(messagem):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    id_modelo = "gpt-3.5-turbo"
    link = "https://api.openai.com/v1/chat/completions"

    corpo_mensagem = {
        "model":id_modelo,
        "messages":[{"role": "user", "content": f"{messagem}"}]
    }

    corpo_mensagem = json.dumps(corpo_mensagem)

    requisicao = requests.post(link,headers=headers,data=corpo_mensagem)
    resposta = requisicao.json()
    saida = resposta["choices"][0]["message"]["content"]
    return saida

while True:
    pergunta=input("qual a pergunta: ")
    if(pergunta == "sair"):
        print("break")
        break
    else:
        print(pesquisa_GPT(pergunta))