from pathlib import Path
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "model.pkl"

def get_data():
    # Features: area (sq ft), bedrooms, house age (years)
    X = np.array([[600,1,20],[750,2,15],[900,2,10],[1100,2,8],
                  [1250,3,7],[1400,3,5],[1600,3,4],[1800,4,3],
                  [2000,4,2],[2200,4,1],[1000,2,12],[1500,3,6]], dtype=float)
    # Synthetic illustrative prices in lakh rupees
    y = np.array([25,32,38,45,52,60,68,76,85,94,41,64], dtype=float)
    return X, y

def train_model():
    X, y = get_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    mae = mean_absolute_error(y_test, model.predict(X_test))
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    print(f"Mean Absolute Error: {mae:.2f} lakh rupees")
    return model, mae

if __name__ == "__main__":
    train_model()
