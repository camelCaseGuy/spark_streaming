# from kafka import KafkaProducer
from kafka import KafkaProducer, KafkaConsumer

import json
import praw

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Adjust for your Kafka setup
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Stream comments and send to Kafka
for comment in subreddit.stream.comments(skip_existing=True):
    message = {
        "author": str(comment.author),
        "body": comment.body,
        "created_utc": comment.created_utc,
    }
    producer.send("reddit-comments", value=message)
    print(f"Sent: {message}")
