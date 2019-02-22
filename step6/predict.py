import sys
import numpy as np
from sklearn.datasets import fetch_openml

from palladium.config import get_config


def predict(features):
    # Get hold of the Palladium configuration in config.py:
    config = get_config()
    # Use the model_persister to load the trained model:
    model = config['model_persister'].read()
    # From here on, it's plain scikit-learn:
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    dataset = fetch_openml("wine-quality-red")

    # Print the feature ranking
    print("Feature ranking:")

    for i in indices:
        print(f"{dataset.feature_names[i]} {importances[i]}")

if __name__ == '__main__':
    predict([float(v) for v in sys.argv[1:]])
