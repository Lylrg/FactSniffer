import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score
import pandas as pd
import pickle

# Read dataset
dataset = pd.read_csv('Dataset.csv')

# Set the MLflow tracking URI to the correct port
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Test train data split
X_train, X_test, y_train, y_test = train_test_split(dataset['text'], dataset['label'], test_size=0.2, random_state=1)

# Initialize CountVectorizer
cv = CountVectorizer()
cv_1 = cv.fit_transform(X_train)

# Initialize classifiers
classifiers = {
    "RandomForest": RandomForestClassifier(random_state=1),
    "SVM": SVC(random_state=1),
    "LogisticRegression": LogisticRegression(random_state=1),
    "KNeighbors": KNeighborsClassifier(),
    "MultinomialNB": MultinomialNB()
}

# Train and evaluate each classifier
for clf_name, clf in classifiers.items():
    # Check if there's an active run and end it
    if mlflow.active_run():
        mlflow.end_run()

    # Start a new MLflow run for each classifier
    with mlflow.start_run(run_name=clf_name):
        try:
            # Train the classifier
            clf.fit(cv_1, y_train)

            # Predict on the test set
            y_pred = clf.predict(cv.transform(X_test))

            # Calculate metrics
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')

            # Print classification report
            report = classification_report(y_test, y_pred)
            print(f"{clf_name} Classifier Report:\n{report}")

            # Log parameters
            mlflow.log_params({
                "model_type": type(clf).__name__,
            })

            # Log metrics
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1_score", f1)

            # Log the model
            mlflow.sklearn.log_model(clf, "model")

            # Log the CountVectorizer object as an artifact
            with open("count_vectorizer.pkl", "wb") as f:
                pickle.dump(cv, f)
            mlflow.log_artifact("count_vectorizer.pkl")

        except Exception as e:
            print(f"Exception occurred while processing {clf_name}: {str(e)}")
            # Log the exception
            mlflow.log_param("exception", str(e))
