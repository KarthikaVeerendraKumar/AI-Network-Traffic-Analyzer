import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Column names
column_names = [
    "duration","protocol_type","service","flag",
    "src_bytes","dst_bytes","land","wrong_fragment",
    "urgent","hot","num_failed_logins","logged_in",
    "num_compromised","root_shell","su_attempted",
    "num_root","num_file_creations","num_shells",
    "num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count",
    "srv_count","serror_rate","srv_serror_rate",
    "rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate",
    "dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
    "difficulty"
]

# Load dataset
df = pd.read_csv(
    "dataset/network_data.csv",
    names=column_names
)

# Convert labels
df["label"] = df["label"].apply(
    lambda x: "Normal" if x == "normal" else "Attack"
)

# Encode text columns
encoder = LabelEncoder()

df["protocol_type"] = encoder.fit_transform(df["protocol_type"])
df["service"] = encoder.fit_transform(df["service"])
df["flag"] = encoder.fit_transform(df["flag"])

# Features and target
X = df.drop(["label"], axis=1)

# Convert label to numbers
y = LabelEncoder().fit_transform(df["label"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "models/model.pkl")

print("Model saved successfully!")