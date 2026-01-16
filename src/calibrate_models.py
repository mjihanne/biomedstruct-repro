from sklearn.calibration import CalibratedClassifierCV


def calibrate_models(models, X_cal, y_cal):
    """
    Apply post-hoc probability calibration using isotonic regression.
    Calibration is learned exclusively on training data.
    """
    calibrated_models = {}

    for name, model in models.items():
        calibrated = CalibratedClassifierCV(
            estimator=model,
            method="isotonic",
            cv="prefit"
        )
        calibrated.fit(X_cal, y_cal)
        calibrated_models[name] = calibrated

    return calibrated_models
