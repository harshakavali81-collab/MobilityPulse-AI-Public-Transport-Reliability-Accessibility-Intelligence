# Model card — offline delay regression demonstration

**Model type:** RandomForestRegressor (80 estimators, min_samples_leaf=4, random_state=42). **Target:** stop-event observed delay in minutes.

**Features:** Hour, day of week, previous delay and stop sequence. All features are only valid if actually known at the point when a real forecast is made; this demo does not establish that operational availability.

**Training split:** Sort by service date; first 80% of unique dates for training, final 20% held out. Compare MAE and RMSE on held-out dates against the training median baseline.

**Evaluation:** `python -m mobilitypulse.models.train_delay_model --allow-synthetic`. Metrics stored in ignored local `data/processed/delay_model.metrics.json`. No independently validated real-world accuracy is claimed. Randomness and simulated process structure can make demo metrics misleading if used for live decisions.

**Limitations:** Dataset bias, simulated route behavior, lack of weather/traffic and live feature availability checks, no concept drift monitoring, no uncertainty calibration or deployed real-time source.

**Appropriate use:** Educational portfolio only. **Inappropriate use:** Real arrival prediction, missed-connection decisions, safety-critical operations.
