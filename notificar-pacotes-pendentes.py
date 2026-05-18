from flask import Flask, jsonify , request
import requests

app = Flask(__name__)

print("INICIANDO DISPARO DE NOTIFICAÇÕES...")

def notificar_pacotes_pendentes(data):
    print("NOTIFICANDO PACOTES PENDENTES...")
    requests.post("http://localhost:8080/notificar/pacotes_pendentes", json=data)
    print("NOTIFICAÇÃO DE PACOTES PENDENTES ENVIADA!")

