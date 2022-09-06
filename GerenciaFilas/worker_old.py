#!/usr/bin/env python
from unicodedata import name
import pika
import json
import pymongo
from pymongo import MongoClient
from datetime import date

today = date.today()

# Abre conexão com o MongoDB
client = pymongo.MongoClient("mongodb://dba:qwe123@localhost:27017/")
db = client["db_noticias"]
collection = db["noticias"]

# Abre conexão com o RabbitMQ
credentials = pika.PlainCredentials('dba', 'qwe123')
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials, heartbeat=1, socket_timeout=3, retry_delay=3, connection_attempts=9999))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Recebe as requisições da fila que venham como noticias
channel.queue_declare(queue='task_noticias', durable=True)

# Método que lê o que foi enviado e insere no banco de dados
def callback(ch, method, properties, body):
    json_noticias = json.loads(body)
    #x = collection.insert_many(json_noticias)
    for noticia in json_noticias:    
        x = collection.replace_one({"title": noticia["title"]}, noticia, upsert=True)
        print(noticia)
    print(" [x] Received %r" % x)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='task_noticias',
on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)