from pathlib import Path
import joblib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "model.pkl"

def predict_example():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Run src/train.py first.")
    model = joblib.load(MODEL_PATH)
    price = float(model.predict(np.array([[1200, 3, 6]], dtype=float))[0])
    print(f"Predicted house price: {price:.2f} lakh rupees")
    return price

if __name__ == "__main__":
    predict_example()
