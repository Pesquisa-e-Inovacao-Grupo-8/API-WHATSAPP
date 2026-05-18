from flask import Flask, jsonify , request
import requests

app = Flask(__name__)

print("INICIANDO DISPARO DE NOTIFICAÇÕES (AGENDAMENTOS PRÓXIMOS)...")

def notificar_agendamentos_proximos(data):
    print("NOTIFICANDO AGENDAMENTOS PRÓXIMOS...")
    requests.post("http://localhost:8080/notificar/agendamentos_proximos", json=data)
    print("NOTIFICAÇÃO DE AGENDAMENTOS PRÓXIMOS ENVIADA!")

