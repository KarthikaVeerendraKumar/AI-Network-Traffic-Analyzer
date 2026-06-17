import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load trained model
model = joblib.load("models/model.pkl")

st.title("AI-Based Smart Network Traffic Analyzer")

st.write(
    "Upload a network traffic dataset and let the AI detect suspicious traffic."
)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv", "txt"]
)

if uploaded_file is not None:

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

    df = pd.read_csv(
        uploaded_file,
        names=column_names
    )

    # Encode categorical columns
    encoder = LabelEncoder()

    df["protocol_type"] = encoder.fit_transform(df["protocol_type"])
    df["service"] = encoder.fit_transform(df["service"])
    df["flag"] = encoder.fit_transform(df["flag"])

    # Prepare features
    X = df.drop(["label"], axis=1)

    # Predict
    predictions = model.predict(X)

    prediction_labels = [
        "Attack" if p == 0 else "Normal"
        for p in predictions
    ]

    df["Prediction"] = prediction_labels

    st.subheader("Prediction Results")

    st.dataframe(df.head())

    normal_count = (
        df["Prediction"] == "Normal"
    ).sum()

    attack_count = (
        df["Prediction"] == "Attack"
    ).sum()

    total_count = len(df)

    st.metric(
        "Total Connections",
        total_count
    )

    st.metric(
        "Normal Traffic",
        normal_count
    )

    st.metric(
        "Attack Traffic",
        attack_count
    )

    st.subheader(
        "Traffic Distribution"
    )

    st.bar_chart(
        df["Prediction"].value_counts()
    )