# Run-NOW

Run on Streamlit [here](https://dheemantha-bhat-run-now-main-ik4e07.streamlit.app/)

**Description:**

Run-NOW is a tool designed to predict waterlogging conditions before going for a run. The key factors considered for a suitable run include:

1. Suitable temperature
2. No rain forecasted during the run
3. Good ground condition

While temperature and rainfall forecasts are readily available on weather apps, predicting ground condition (specifically if the ground is dry for a run) can be challenging. Ground wetness and waterlogging depend on the intensity and consistency of rainfall in the last few hours. Run-NOW utilizes observed rainfall data to predict if the ground conditions are ideal for a run.

**How It Works:**

The algorithm follows these steps:

1. Uses the Geopy library to convert the input location to coordinates.
2. Utilizes the Meteomatics weather API to obtain observed rainfall data in millimeters for each hour.
3. Considers the water absorption rate by the soil as 1 inch per hour.
4. Assumes the catchment area as 50 times the observed rainfall.


**How to Run:**

1. Set up the necessary credentials for the [Meteomatics](https://www.meteomatics.com/) API.
2. Execute the tool using Streamlit.


