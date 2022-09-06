#!/usr/bin/env python
import pika
import json 

file = "/tmp/noticias.json" 

# Abre o arquivo json e faz o tratamento dos dados para o JSON entender que são vários registros
with open(file, "r") as r: 
    response = r.read() 
    response = response.replace('\n', '') 
    response = response.replace('}{', '},{') 
    response = "[" + response + "]" 
    jsonNoticias = json.loads(response)

# Abre conexão com o RabbitMQ
credentials = pika.PlainCredentials('dba', 'qwe123')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials, heartbeat=1, retry_delay=1))
channel = connection.channel()

# Abre a requisição com nome noticias
channel.queue_declare(queue='task_noticias', durable=True)

# Envia as noticias por json
channel.basic_publish(exchange='',
routing_key='task_noticias',
body=json.dumps(jsonNoticias),
properties=pika.BasicProperties(
    delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print("Notícia enviada para a fila!")

connection.close()