# ============================================================
# ADVANCED CANCER PREDICTION MODEL
# Cross Validation + Hyperparameter Tuning
# ROC Curve + Feature Importance
# Model Saving + Prediction
# ============================================================

# -------------------------
# 1. IMPORT LIBRARIES
# -------------------------

import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score,
    RandomizedSearchCV
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    RocCurveDisplay,
    PrecisionRecallDisplay,
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# ============================================================
# 2. CONFIGURATION
# ============================================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "The_Cancer_data.csv.xlsx"

TARGET_COLUMN = "Diagnosis"

TEST_SIZE = 0.20
RANDOM_STATE = 42

MODEL_PATH = "models/best_model.pkl"


# ============================================================
# 3. LOAD DATASET
# ============================================================

def load_dataset(file_path):

    try:

        df = pd.read_excel(file_path)

        print("Dataset loaded successfully.")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        return df

    except FileNotFoundError:

        print("Dataset file not found.")
        print(file_path)

        raise

    except Exception as error:

        print(f"Error loading dataset: {error}")

        raise


# ============================================================
# 4. PREPARE DATA
# ============================================================

def prepare_data(df):

    X = df.drop(
        TARGET_COLUMN,
        axis=1
    )

    y = df[TARGET_COLUMN]

    print("\nData Preparation")
    print("-" * 50)

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    return X, y


# ============================================================
# 5. TRAIN TEST SPLIT
# ============================================================

def split_data(X, y):

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=TEST_SIZE,

        random_state=RANDOM_STATE,

        stratify=y
    )

    print("\nTrain-Test Split")
    print("-" * 50)

    print("Training samples:", X_train.shape[0])
    print("Testing samples :", X_test.shape[0])

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )


# ============================================================
# 6. CREATE RANDOM FOREST
# ============================================================

def create_random_forest():

    model = RandomForestClassifier(
        random_state=RANDOM_STATE
    )

    return model


# ============================================================
# 7. CROSS VALIDATION
# ============================================================

def perform_cross_validation(model, X, y):

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_STATE
    )

    scores = cross_val_score(

        model,

        X,

        y,

        cv=cv,

        scoring="roc_auc"
    )

    print("\nCross Validation Results")
    print("-" * 50)

    print("Fold ROC-AUC scores:")

    for index, score in enumerate(scores, start=1):

        print(
            f"Fold {index}: {score:.4f}"
        )

    print(
        f"\nMean ROC-AUC: {scores.mean():.4f}"
    )

    print(
        f"Standard Deviation: {scores.std():.4f}"
    )

    return scores


# ============================================================
# 8. HYPERPARAMETER TUNING
# ============================================================

def tune_random_forest(X_train, y_train):

    model = RandomForestClassifier(
        random_state=RANDOM_STATE
    )

    param_grid = {

        "n_estimators": [
            100,
            200,
            300,
            500
        ],

        "max_depth": [
            None,
            5,
            10,
            15,
            20
        ],

        "min_samples_split": [
            2,
            5,
            10
        ],

        "min_samples_leaf": [
            1,
            2,
            4
        ],

        "max_features": [
            "sqrt",
            "log2"
        ]
    }

    search = RandomizedSearchCV(

        estimator=model,

        param_distributions=param_grid,

        n_iter=20,

        scoring="roc_auc",

        cv=5,

        random_state=RANDOM_STATE,

        n_jobs=-1,

        verbose=1
    )

    search.fit(
        X_train,
        y_train
    )

    print("\nHyperparameter Tuning")
    print("-" * 50)

    print("\nBest Parameters:")

    print(
        search.best_params_
    )

    print("\nBest Cross Validation ROC-AUC:")

    print(
        f"{search.best_score_:.4f}"
    )

    return search.best_estimator_


# ============================================================
# 9. EVALUATE MODEL
# ============================================================

def evaluate_model(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(
        X_test
    )

    y_probability = model.predict_proba(
        X_test
    )[:, 1]

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    roc_auc = roc_auc_score(
        y_test,
        y_probability
    )

    print("\nFinal Model Evaluation")
    print("-" * 50)

    print(
        f"Accuracy : {accuracy:.4f}"
    )

    print(
        f"Precision: {precision:.4f}"
    )

    print(
        f"Recall   : {recall:.4f}"
    )

    print(
        f"F1 Score : {f1:.4f}"
    )

    print(
        f"ROC-AUC  : {roc_auc:.4f}"
    )

    print("\nClassification Report")

    print(
        classification_report(
            y_test,
            y_pred
        )
    )

    return y_pred, y_probability


# ============================================================
# 10. ROC CURVE
# ============================================================

def plot_roc_curve(
    model,
    X_test,
    y_test
):

    RocCurveDisplay.from_estimator(

        model,

        X_test,

        y_test
    )

    plt.title(
        "Random Forest - ROC Curve"
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# 11. PRECISION-RECALL CURVE
# ============================================================

def plot_precision_recall_curve(
    model,
    X_test,
    y_test
):

    PrecisionRecallDisplay.from_estimator(

        model,

        X_test,

        y_test
    )

    plt.title(
        "Random Forest - Precision-Recall Curve"
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# 12. CONFUSION MATRIX
# ============================================================

def plot_confusion_matrix(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(
        X_test
    )

    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    print("\nConfusion Matrix")
    print("-" * 50)

    print(matrix)

    plt.figure(
        figsize=(6, 5)
    )

    plt.imshow(
        matrix
    )

    plt.title(
        "Random Forest - Confusion Matrix"
    )

    plt.xlabel(
        "Predicted"
    )

    plt.ylabel(
        "Actual"
    )

    plt.colorbar()

    plt.tight_layout()

    plt.show()


# ============================================================
# 13. FEATURE IMPORTANCE
# ============================================================

def plot_feature_importance(
    model,
    X
):

    importance = pd.Series(

        model.feature_importances_,

        index=X.columns
    )

    importance = importance.sort_values(
        ascending=False
    )

    print("\nFeature Importance")
    print("-" * 50)

    print(
        importance
    )

    plt.figure(
        figsize=(10, 6)
    )

    importance.plot(
        kind="bar"
    )

    plt.title(
        "Random Forest - Feature Importance"
    )

    plt.xlabel(
        "Features"
    )

    plt.ylabel(
        "Importance"
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# 14. SAVE MODEL
# ============================================================

def save_model(model):

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print("\nModel saved successfully.")

    print(
        f"Location: {MODEL_PATH}"
    )


# ============================================================
# 15. LOAD MODEL
# ============================================================

def load_model():

    model = joblib.load(
        MODEL_PATH
    )

    return model


# ============================================================
# 16. PREDICTION FUNCTION
# ============================================================

def predict_cancer(
    model,
    input_data
):

    input_df = pd.DataFrame(
        [input_data]
    )

    prediction = model.predict(
        input_df
    )

    probability = model.predict_proba(
        input_df
    )[:, 1]

    return (
        prediction[0],
        probability[0]
    )


# ============================================================
# 17. MAIN FUNCTION
# ============================================================

def main():

    print("=" * 60)
    print("ADVANCED CANCER PREDICTION MODEL")
    print("=" * 60)

    # Step 1: Load dataset

    df = load_dataset(
        DATA_PATH
    )

    # Step 2: Prepare data

    X, y = prepare_data(
        df
    )

    # Step 3: Train-test split

    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = split_data(
        X,
        y
    )

    # Step 4: Create Random Forest

    base_model = create_random_forest()

    # Step 5: Cross-validation

    perform_cross_validation(
        base_model,
        X_train,
        y_train
    )

    # Step 6: Hyperparameter tuning

    best_model = tune_random_forest(
        X_train,
        y_train
    )

    # Step 7: Evaluate best model

    evaluate_model(
        best_model,
        X_test,
        y_test
    )

    # Step 8: ROC Curve

    plot_roc_curve(
        best_model,
        X_test,
        y_test
    )

    # Step 9: Precision-Recall Curve

    plot_precision_recall_curve(
        best_model,
        X_test,
        y_test
    )

    # Step 10: Confusion Matrix

    plot_confusion_matrix(
        best_model,
        X_test,
        y_test
    )

    # Step 11: Feature Importance

    plot_feature_importance(
        best_model,
        X
    )

    # Step 12: Save model

    save_model(
        best_model
    )

    print("\nPipeline completed successfully.")


# ============================================================
# 18. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()