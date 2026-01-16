from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import HistGradientBoostingClassifier


def train_models(X_train, y_train, config):
    """
    Train the three reference models used in the study:
    Logistic Regression, Random Forest, and Histogram-Based Gradient Boosting.
    Hyperparameters are fixed to ensure reproducibility.
    """
    models = {}

    models["LR"] = LogisticRegression(
        solver=config["logistic_regression"]["solver"],
        penalty=config["logistic_regression"]["penalty"],
        C=config["logistic_regression"]["C"],
        max_iter=config["logistic_regression"]["max_iter"],
        class_weight=config["logistic_regression"]["class_weight"],
        random_state=config["random_state"]
    ).fit(X_train, y_train)

    models["RF"] = RandomForestClassifier(
        n_estimators=config["random_forest"]["n_estimators"],
        max_depth=config["random_forest"]["max_depth"],
        min_samples_leaf=config["random_forest"]["min_samples_leaf"],
        max_features=config["random_forest"]["max_features"],
        class_weight=config["random_forest"]["class_weight"],
        random_state=config["random_state"]
    ).fit(X_train, y_train)

    models["HGBT"] = HistGradientBoostingClassifier(
        learning_rate=config["hgbt"]["learning_rate"],
        max_depth=config["hgbt"]["max_depth"],
        max_bins=config["hgbt"]["max_bins"],
        l2_regularization=config["hgbt"]["l2_regularization"],
        random_state=config["random_state"]
    ).fit(X_train, y_train)

    return models
