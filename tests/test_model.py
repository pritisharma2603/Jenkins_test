import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from train import get_data, train_model

def test_dataset_shapes():
    X, y = get_data()
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 3

def test_training_and_prediction():
    model, mae = train_model()
    assert hasattr(model, "predict")
    assert mae >= 0
    prediction = model.predict([[1200, 3, 6]])
    assert len(prediction) == 1
    assert prediction[0] > 0
