import pika
broker_ip = "<VM1_IP>"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_ip))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
print("Waiting for messages...")
channel.start_consuming()
