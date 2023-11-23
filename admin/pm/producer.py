#amqps://ohocjvwe:HqJUCS-5fer6KZ5w8lTUGaJKKkW2aBi6@beaver.rmq.cloudamqp.com/ohocjvwe
import pika, json

params = pika.URLParameters('amqps://ohocjvwe:HqJUCS-5fer6KZ5w8lTUGaJKKkW2aBi6@beaver.rmq.cloudamqp.com/ohocjvwe')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='pmmain',body=json.dumps(body), properties=properties)