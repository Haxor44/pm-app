import pika


params = pika.URLParameters('amqps://ohocjvwe:HqJUCS-5fer6KZ5w8lTUGaJKKkW2aBi6@beaver.rmq.cloudamqp.com/ohocjvwe')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print("Recieved in admin!!!")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print("started consumption!!!")
channel.start_consuming()
channel.close()