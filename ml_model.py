import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import joblib

INPUT_FILE = "data/processed/worldcities_time_dilation_with_elevation.csv"

def train_neural_model():
    # Load dataset
    df = pd.read_csv(INPUT_FILE)

    # Drop rows missing elevation
    df = df.dropna(subset=["elevation_meters"])

    # Feature matrix (lat, lng, elevation)
    X = df[["lat", "lng", "elevation_meters"]].values

    # Target: microseconds of difference per year
    y = df["microseconds_difference_per_year"].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Build neural network
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation="relu", input_shape=(3,)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(1)  # predicting a continuous value
    ])

    model.compile(optimizer="adam", loss="mse")

    # Train
    history = model.fit(
        X_train_scaled, y_train,
        validation_data=(X_test_scaled, y_test),
        epochs=50,
        batch_size=64,
        verbose=1
    )

    # Save model + scaler
    model.save("model/time_dilation_nn.h5")
    joblib.dump(scaler, "model/scaler.pkl")

    print("Model + scaler saved.")
    print("Final validation loss:", history.history["val_loss"][-1])


if __name__ == "__main__":
    train_neural_model()
