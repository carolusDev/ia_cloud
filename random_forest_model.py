from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
import joblib


housing = fetch_california_housing()
X, y = housing.data, housing.target

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
joblib.dump(model, "random_forest_model.joblib")

