mport pika
broker_ip = "<VM1_IP>"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_ip))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
message = "Hello from Producer!"
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
print(f"Sent: {message}")
connection.close()
