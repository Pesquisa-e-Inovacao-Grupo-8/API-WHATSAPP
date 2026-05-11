from flask import Flask, jsonify , request
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

# Credenciais
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

print(TWILIO_ACCOUNT_SID)


# ============================================
# ENVIAR MENSAGEM
# ============================================
def enviar_mensagem(numero, mensagem):

    sms = client.messages.create(
        body=mensagem,
        from_=TWILIO_PHONE_NUMBER,
        to=f"whatsapp:{numero}"
    )

    return sms


# ============================================
# TEMPLATE - AGENDAMENTO CRIADO
# ============================================
def mensagem_agendamento(data):

    return f"""
📅 Olá, {data['cliente']}!

Seu agendamento foi criado com sucesso ✅

📌 Serviço: {data['servico']}
🗓️ Data: {data['data']}
⏰ Horário: {data['horario']}

🧾 Pedido: #{data['ordemPedido']}

Obrigado pela preferência ❤️
"""


# ============================================
# TEMPLATE - PAGAMENTO APROVADO
# ============================================
def mensagem_pagamento(data):

    return f"""
💳 Pagamento aprovado com sucesso ✅

📌 Serviço: {data['servico']}
💰 Valor pago: R$ {data['preco']}
🧾 Pedido: #{data['ordemPedido']}

Seu horário está confirmado 🎉
"""


# ============================================
# TEMPLATE - LEMBRETE
# ============================================
def mensagem_lembrete(data):

    return f"""
⏰ Lembrete do seu agendamento!

Olá, {data['cliente']} 😊

Seu atendimento acontecerá em 2 dias.

📌 Serviço: {data['servico']}
🗓️ Data: {data['data']}
⏰ Horário: {data['horario']}

Nos vemos em breve ❤️
"""


# ============================================
# ENDPOINT - AGENDAMENTO
# ============================================
@app.route("/notify/agendamento", methods=["POST"])
def notify_agendamento():

    data = request.get_json()

    sms = enviar_mensagem(
        data["telefone"],
        mensagem_agendamento(data)
    )

    return jsonify({
        "success": True,
        "sid": sms.sid
    })


# ============================================
# ENDPOINT - PAGAMENTO
# ============================================
@app.route("/notify/pagamento", methods=["POST"])
def notify_pagamento():

    data = request.get_json()

    sms = enviar_mensagem(
        data["telefone"],
        mensagem_pagamento(data)
    )

    return jsonify({
        "success": True,
        "sid": sms.sid
    })


# ============================================
# ENDPOINT - LEMBRETE
# ============================================
@app.route("/notify/lembrete", methods=["POST"])
def notify_lembrete():

    data = request.get_json()

    sms = enviar_mensagem(
        data["telefone"],
        mensagem_lembrete(data)
    )

    return jsonify({
        "success": True,
        "sid": sms.sid
    })


# ============================================
# START
# ============================================
if __name__ == "__main__":
    app.run(debug=True)