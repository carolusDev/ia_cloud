import joblib

model = joblib.load("random_forest_model.joblib")

new_data = [[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]
prediction = model.predict(new_data)

print("prédictions: ", prediction)


