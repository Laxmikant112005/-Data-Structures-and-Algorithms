# ============================================================
# CANCER PREDICTION MODEL
# Machine Learning Classification Project
# ============================================================

# -------------------------
# 1. IMPORT LIBRARIES
# -------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    ConfusionMatrixDisplay
)


# ============================================================
# 2. CONFIGURATION
# ============================================================

DATA_PATH = (
    r"C:\Users\Laxmikant Sangolagi\OneDrive\Documents"
    r"\Python-AI-and-ML\Canser prediction"
    r"\Canser-model\The_Cancer_data.csv"
)

TARGET_COLUMN = "Diagnosis"

TEST_SIZE = 0.20
RANDOM_STATE = 42

SCALED_MODELS = [
    "Logistic Regression",
    "SVM"
]


# ============================================================
# 3. LOAD DATASET
# ============================================================

def load_dataset(file_path):
    """
    Load the cancer dataset from a CSV file.
    """

    try:
        df = pd.read_csv(file_path)

        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("Error: Dataset file not found.")
        print(f"Check the file path:\n{file_path}")
        raise

    except Exception as error:
        print(f"Error while loading dataset: {error}")
        raise


# ============================================================
# 4. BASIC DATASET INFORMATION
# ============================================================

def display_dataset_information(df):
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nTarget Distribution:")
    print(df[TARGET_COLUMN].value_counts())

    print("\nTarget Distribution (%):")

    target_percentage = (
        df[TARGET_COLUMN]
        .value_counts(normalize=True)
        .mul(100)
    )

    print(target_percentage)


# ============================================================
# 5. DATA VISUALIZATION
# ============================================================

def visualize_dataset(df):
    """
    Generate exploratory data analysis visualizations.
    """

    print("\n" + "=" * 60)
    print("DATA VISUALIZATION")
    print("=" * 60)

    # -------------------------
    # Histograms
    # -------------------------

    df.hist(
        figsize=(14, 10),
        bins=20
    )

    plt.suptitle(
        "Feature Distributions",
        fontsize=16
    )

    plt.tight_layout()
    plt.show()

    # -------------------------
    # Age vs Diagnosis
    # -------------------------

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x=TARGET_COLUMN,
        y="Age"
    )

    plt.title("Age vs Cancer Diagnosis")
    plt.tight_layout()
    plt.show()

    # -------------------------
    # BMI vs Diagnosis
    # -------------------------

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x=TARGET_COLUMN,
        y="BMI"
    )

    plt.title("BMI vs Cancer Diagnosis")
    plt.tight_layout()
    plt.show()

    # -------------------------
    # Physical Activity
    # -------------------------

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x=TARGET_COLUMN,
        y="PhysicalActivity"
    )

    plt.title("Physical Activity vs Cancer Diagnosis")
    plt.tight_layout()
    plt.show()

    # -------------------------
    # Smoking vs Diagnosis
    # -------------------------

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Smoking",
        hue=TARGET_COLUMN
    )

    plt.title("Smoking vs Cancer Diagnosis")
    plt.tight_layout()
    plt.show()

    # -------------------------
    # Cancer History
    # -------------------------

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="CancerHistory",
        hue=TARGET_COLUMN
    )

    plt.title("Cancer History vs Diagnosis")
    plt.tight_layout()
    plt.show()

    # -------------------------
    # Correlation Matrix
    # -------------------------

    plt.figure(figsize=(12, 9))

    correlation_matrix = df.corr(numeric_only=True)

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Feature Correlation Matrix")
    plt.tight_layout()
    plt.show()


# ============================================================
# 6. PREPARE FEATURES AND TARGET
# ============================================================

def prepare_data(df):
    """
    Separate features (X) and target (y).
    """

    X = df.drop(
        TARGET_COLUMN,
        axis=1
    )

    y = df[TARGET_COLUMN]

    print("\n" + "=" * 60)
    print("DATA PREPARATION")
    print("=" * 60)

    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")

    return X, y


# ============================================================
# 7. TRAIN-TEST SPLIT
# ============================================================

def split_data(X, y):
    """
    Split dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("\n" + "=" * 60)
    print("TRAIN-TEST SPLIT")
    print("=" * 60)

    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples : {X_test.shape[0]}")

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )


# ============================================================
# 8. FEATURE SCALING
# ============================================================

def scale_features(X_train, X_test):
    """
    Standardize numerical features.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\nFeatures scaled successfully.")

    return (
        scaler,
        X_train_scaled,
        X_test_scaled
    )


# ============================================================
# 9. CREATE MACHINE LEARNING MODELS
# ============================================================

def create_models():
    """
    Create multiple classification models.
    """

    models = {

        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            random_state=RANDOM_STATE
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=RANDOM_STATE
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=RANDOM_STATE
        ),

        "SVM": SVC(
            probability=True,
            random_state=RANDOM_STATE
        ),

        "Gradient Boosting": GradientBoostingClassifier(
            random_state=RANDOM_STATE
        )
    }

    return models


# ============================================================
# 10. TRAIN MODELS
# ============================================================

def train_models(
    models,
    X_train,
    X_train_scaled,
    y_train
):
    """
    Train all machine learning models.
    """

    trained_models = {}

    print("\n" + "=" * 60)
    print("MODEL TRAINING")
    print("=" * 60)

    for name, model in models.items():

        if name in SCALED_MODELS:
            model.fit(
                X_train_scaled,
                y_train
            )

        else:
            model.fit(
                X_train,
                y_train
            )

        trained_models[name] = model

        print(f"✓ {name} trained successfully.")

    return trained_models


# ============================================================
# 11. EVALUATE MODELS
# ============================================================

def evaluate_models(
    trained_models,
    X_test,
    X_test_scaled,
    y_test
):
    """
    Evaluate all trained models using
    Accuracy, Precision, Recall, F1 and ROC-AUC.
    """

    results = []

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    for name, model in trained_models.items():

        if name in SCALED_MODELS:
            X_eval = X_test_scaled

        else:
            X_eval = X_test

        # Predictions
        y_pred = model.predict(X_eval)

        # Probability predictions
        y_prob = model.predict_proba(X_eval)[:, 1]

        # Evaluation metrics
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
            y_prob
        )

        results.append({
            "Model": name,
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1 Score": f1,
            "ROC-AUC": roc_auc
        })

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="ROC-AUC",
        ascending=False
    ).reset_index(drop=True)

    return results_df


# ============================================================
# 12. DISPLAY MODEL RESULTS
# ============================================================

def display_results(results_df):
    """
    Display model comparison results.
    """

    print("\n" + "=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)

    print(
        results_df.to_string(
            index=False,
            float_format=lambda x: f"{x:.4f}"
        )
    )


# ============================================================
# 13. CLASSIFICATION REPORT
# ============================================================

def display_classification_reports(
    trained_models,
    X_test,
    X_test_scaled,
    y_test
):
    """
    Display detailed classification reports
    for every trained model.
    """

    print("\n" + "=" * 60)
    print("CLASSIFICATION REPORTS")
    print("=" * 60)

    for name, model in trained_models.items():

        if name in SCALED_MODELS:
            X_eval = X_test_scaled

        else:
            X_eval = X_test

        y_pred = model.predict(X_eval)

        print("\n" + "=" * 60)
        print(name)
        print("=" * 60)

        print(
            classification_report(
                y_test,
                y_pred
            )
        )


# ============================================================
# 14. MODEL COMPARISON VISUALIZATION
# ============================================================

def plot_model_comparison(results_df):
    """
    Plot performance comparison of all models.
    """

    metrics = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]

    results_plot = results_df.set_index("Model")

    results_plot[metrics].plot(
        kind="bar",
        figsize=(14, 7)
    )

    plt.title(
        "Cancer Prediction Model Comparison"
    )

    plt.ylabel("Score")

    plt.xlabel("Machine Learning Model")

    plt.ylim(0, 1)

    plt.xticks(
        rotation=30,
        ha="right"
    )

    plt.legend(
        loc="lower right"
    )

    plt.tight_layout()
    plt.show()


# ============================================================
# 15. SELECT BEST MODEL
# ============================================================

def select_best_model(
    results_df,
    trained_models
):
    """
    Select the best model based on ROC-AUC.
    """

    best_model_name = results_df.iloc[0]["Model"]

    best_model = trained_models[
        best_model_name
    ]

    print("\n" + "=" * 60)
    print("BEST MODEL")
    print("=" * 60)

    print(
        f"Best model based on ROC-AUC: "
        f"{best_model_name}"
    )

    print("\nModel Details:")
    print(best_model)

    return (
        best_model_name,
        best_model
    )


# ============================================================
# 16. CONFUSION MATRIX
# ============================================================

def plot_confusion_matrix(
    best_model_name,
    best_model,
    X_test,
    X_test_scaled,
    y_test
):
    """
    Display confusion matrix for the best model.
    """

    if best_model_name in SCALED_MODELS:
        X_eval = X_test_scaled

    else:
        X_eval = X_test

    ConfusionMatrixDisplay.from_estimator(
        best_model,
        X_eval,
        y_test
    )

    plt.title(
        f"{best_model_name} - Confusion Matrix"
    )

    plt.tight_layout()
    plt.show()


# ============================================================
# 17. MAIN FUNCTION
# ============================================================

def main():
    """
    Execute the complete machine learning pipeline.
    """

    # Step 1: Load dataset
    df = load_dataset(DATA_PATH)

    # Step 2: Understand dataset
    display_dataset_information(df)

    # Step 3: Visualize dataset
    visualize_dataset(df)

    # Step 4: Prepare X and y
    X, y = prepare_data(df)

    # Step 5: Train-test split
    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = split_data(X, y)

    # Step 6: Feature scaling
    (
        scaler,
        X_train_scaled,
        X_test_scaled
    ) = scale_features(
        X_train,
        X_test
    )

    # Step 7: Create models
    models = create_models()

    # Step 8: Train models
    trained_models = train_models(
        models,
        X_train,
        X_train_scaled,
        y_train
    )

    # Step 9: Evaluate models
    results_df = evaluate_models(
        trained_models,
        X_test,
        X_test_scaled,
        y_test
    )

    # Step 10: Display results
    display_results(results_df)

    # Step 11: Classification reports
    display_classification_reports(
        trained_models,
        X_test,
        X_test_scaled,
        y_test
    )

    # Step 12: Compare models visually
    plot_model_comparison(
        results_df
    )

    # Step 13: Select best model
    (
        best_model_name,
        best_model
    ) = select_best_model(
        results_df,
        trained_models
    )

    # Step 14: Confusion matrix
    plot_confusion_matrix(
        best_model_name,
        best_model,
        X_test,
        X_test_scaled,
        y_test
    )


# ============================================================
# 18. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()