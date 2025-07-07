# CO₂ Buildup Analysis in Indian Hostel Rooms

This repository contains experimental data, Python scripts, and theoretical modeling related to the study of carbon dioxide (CO₂) buildup in a naturally ventilated Indian student hostel room. The project quantifies the impact of human occupancy on indoor air quality (IAQ) and evaluates the effectiveness of passive ventilation strategies.

## 📌 Objective

To experimentally investigate the temporal evolution of CO₂ concentration under controlled conditions for different occupancy levels (1, 2, and 3 persons) and validate mass-balance-based ventilation models by extracting parameters like:

- Air Change per Hour (ACH)
- Steady-state CO₂ concentration
- Indoor CO₂ generation rate

## 🧪 Methodology

- **Setup:** A closed hostel room (10×10×10 ft³) was monitored with minimal passive ventilation.
- **Instrumentation:** CO₂ concentration was measured using a non-dispersive infrared (NDIR) sensor (UART interface). Temperature and humidity were logged using a DHT11 sensor.
- **Data Logging:** Readings were recorded every 2 seconds for 4–6 hours per trial.
- **Analysis:**
  - Data smoothing using Savitzky-Golay filter.
  - Exponential curve fitting for CO₂ rise.
  - Mass-balance modeling and ACH calculation.
  - ASTM-based validation and comparison.

## 📊 Results Summary

| Occupancy | Steady-State CO₂ (ppm) | ACH    | R² (Fit Quality) |
|-----------|------------------------|--------|------------------|
| 1 Person  | ~702                   | 0.84   | 0.9805           |
| 2 Person  | ~1149                  | 1.12   | 0.9952           |
| 3 Person  | ~2038                  | 1.30   | 0.9592           |

- CO₂ levels exceeded the 1000 ppm threshold (ASHRAE/WHO) for 2 and 3-person cases.
- Vertical stratification was minimal: a one-time check showed negligible difference between mid-height and ceiling readings.
- No strong correlation found between temperature/humidity and CO₂ buildup.

## 🧠 Key Implications

- Natural ventilation becomes insufficient beyond single occupancy.
- CO₂ buildup occurred rapidly even at low activity levels (~1.2 MET).
- Suggests implementation of low-cost mechanical ventilation like timed fan-assisted flushing in shared student accommodations.

## 📁 Repository Contents

- `/scripts/`: Python files for filtering, curve fitting, and parameter extraction.
- `/figures/`: Final plots used in the paper.
- `report_summary.pdf`: Abstract and highlights from the submitted research paper.


## 📬 Contact

For queries, collaboration, or data requests, reach out via sidhwatanuj@gmail.com / srivarshadodda@gmail.com.


