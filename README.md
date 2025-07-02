# Cybersecurity-Suspicious-Web-Threat-Interactions

# 🔹 Project 2: Cybersecurity – Suspicious Web Threat Interactions

## ✏️ Objective:

To classify incoming web traffic logs from AWS CloudWatch as either normal or suspicious using anomaly
detection and supervised learning algorithms.

## 📈 Dataset Summary:

This dataset included traffic logs from a production web server with features:

```
Traffic Volumes: bytes_in, bytes_out
Timestamps: creation_time, end_time, time
Network Info: src_ip, dst_ip, protocol, dst_port
Labels: rule_names, detection_types
```
## ⚡️ Key Implementation Steps:

**✉️ Feature Engineering**

```
df['session_duration'] = (df['end_time'] -
df['creation_time']).dt.total_seconds()
df['avg_packet_size'] = (df['bytes_in'] + df['bytes_out']) /
df['session_duration']
```
**🔧 Model Training**

```
Model used: RandomForestClassifier
Additional experimentation: Isolation Forest & Neural Nets
```
```
model= RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump((model, scaler),'cybersecurity_rf_model.pkl')
```
**📄 Deployment (Flask + WebView)**

```
@app.route("/predict", methods=["POST"])
defpredict():
features = [float(request.form[f])for f ininput_keys]
prediction = model.predict([scaler.transform([features])])[0]
return render_template("index.html", prediction=class_map[prediction])
```
### • • • • • •


## 🚀 Outcome:

A local desktop dashboard for predicting if an incoming session is suspicious. The app used Flask for
serving the model and WebView for seamless embedding into a desktop environment.
