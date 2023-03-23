from kafka import KafkaConsumer
import json
import joblib
from pymongo import MongoClient


model = joblib.load("random_forest_model.joblib")

consumer = KafkaConsumer(
    "random_forest_model",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="carolus"
)

client = MongoClient("mongodb://localhost:27017/")
db = client["nom_de_la_base_de_donnees"]
predictions = db["predictions"]

print("data pending...")

for message in consumer:
    data = message.value
    prediction = model.predict(data)
    prediction_doc = {"prediction": prediction.tolist()}
    predictions.insert_one(prediction_doc)
    producer.send("prediction_random_forest", value = prediction)
    print("prédictions: ", prediction)
