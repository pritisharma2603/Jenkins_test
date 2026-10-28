from pathlib import Path
import joblib
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from train import get_data

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "model.pkl"

def evaluate():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Run src/train.py first.")
    model = joblib.load(MODEL_PATH)
    X, y = get_data()
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    mae = mean_absolute_error(y_test, model.predict(X_test))
    print(f"Evaluation MAE: {mae:.2f} lakh rupees")
    return mae

if __name__ == "__main__":
    evaluate()
