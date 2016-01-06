#!/usr/bin/env python
import pika
import sys, re
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='wl_update_queue', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
   nesplit = body.split(",")
   print(" [x] Received %r" % body)
   doc = {
       'primary_name': nesplit[1],
       'dob' : '19680901'
   }
   res = es.index(index="rni-test", doc_type="record",  id=nesplit[0], body=doc)
   print("hi %s" %res)

channel.basic_consume(callback,
                      queue='wl_update2',
                      no_ack=True)

channel.start_consuming()
