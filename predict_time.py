import numpy as np
import joblib
import tensorflow as tf

scaler = joblib.load("model/scaler.pkl")

# Load WITHOUT compiling
model = tf.keras.models.load_model(
    "model/time_dilation_nn.h5",
    compile=False
)

def predict_time_dilation(lat, lng, elevation):
    X = np.array([[lat, lng, elevation]], dtype=float)
    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)[0][0]
    return float(pred)

if __name__ == "__main__":
    chicago_lat = 41.8781
    chicago_lng = -87.6298
    chicago_elev = 181

    pred = predict_time_dilation(chicago_lat, chicago_lng, chicago_elev)
    print("Predicted microseconds per year:", pred)
