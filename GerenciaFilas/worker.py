#!/usr/bin/env python
import pika
import json
import pymongo
import time 

# Abre conexão com o MongoDB
client = pymongo.MongoClient("mongodb://dba:qwe123@db_noticias:27017/")
db = client["db_noticias"]
collection = db["Noticias"]

def python_none():
    pass

# Método que lê o que foi enviado e insere no banco de dados
def callback(ch, method, properties, body):
    json_noticias = json.loads(body)
    #x = collection.insert_many(json_noticias)
    for noticia in json_noticias:    
        #print (noticia['title'])
        z = collection.find_one({"title": noticia['title']})

        #print ("Tõ printando o Z" , z)
        if z is None:
            x = collection.replace_one({"title": noticia['title'], },noticia, upsert=True)
            print(" [x] Processando item da fila... %r" % noticia['title'])
            #print(noticia)
            

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Método para testar a conexão com o banco de dados
def db_connect():
    try:
        if client.server_info():
            print("Conexão estabelecida com o banco de dados!")
            return True
    except:
        print("Banco de dados indisponível, tentando novamente...")
        return False

# Enquanto a conexão estiver estabelecida, processa as filas vindas do rabbit, se cair, volta a testar a conexão e fica em looping até voltar
while (True):
    try:
        # Testa a conexão com o banco
        test_connection = db_connect() 
        if (test_connection == True):
            # Abre conexão com o RabbitMQ
            credentials = pika.PlainCredentials('dba', 'qwe123')
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
            channel = connection.channel()
            
            # Recebe as requisições da fila que venham como task_noticias
            channel.queue_declare(queue='task_noticias', durable=True)

            # Processa o que está na fila
            channel.basic_consume(queue='task_noticias',
            on_message_callback=callback)

            print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
            channel.start_consuming()

    except pymongo.errors.ServerSelectionTimeoutError as err:
        #print(err)
        time.sleep(1)
