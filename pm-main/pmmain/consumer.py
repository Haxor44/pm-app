import pika, json,os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmmain.settings")
django.setup()
from pm.models import PmStaff

params = pika.URLParameters('amqps://ohocjvwe:HqJUCS-5fer6KZ5w8lTUGaJKKkW2aBi6@beaver.rmq.cloudamqp.com/ohocjvwe')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='pmmain')

def callback(ch,method,properties,body):
    print("Recieved in pmmain!!!")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'pmform_created':
        pmstaff = PmStaff()
        pmstaff.name = data["name"]
        pmstaff.save()
        
    elif properties.content_type == "pmform_updated":
        pmstaff = PmStaff.objects.get(data["id"])
        pmstaff.name = data["name"]
        pmstaff.save()

    elif properties.content_type == "pmform_deleted":
        pmstaff = PmStaff.objects.get(data["id"])
        pmstaff.delete()


channel.basic_consume(queue='pmmain', on_message_callback=callback, auto_ack=True)

print("started consumption!!!")
channel.start_consuming()
channel.close()