# 🚦 Traffic Optimization & Mobility Strategy | Self Project

> **Goal:** Designed and tested a smart mobility solution to achieve **25% congestion reduction** and **16% modal shift** towards public transport through AI-driven traffic management and public transport expansion.

---

## 📌 Overview
This project focuses on **urban traffic optimization** and **mobility strategy** design for the PMPML network.  
The solution integrates **GPS-enabled ticketing**, **AI-based traffic flow prediction**, and **MoSCoW/RICE prioritization frameworks** to guide development.

Key highlights:
- Upgraded PMPML app with **GPS tracking** and **DigiLocker-integrated ticketing**.
- Used **AI forecasting** to optimize route planning and traffic signal timing.
- Defined **North Star Metric** and achieved a **4x ROI** by reducing avoidable transportation costs.

---

## 🏗️ Architecture
```mermaid
graph TD;
    A[Traffic Data Sources] -->|ETL| B[Data Preprocessing]
    B --> C[Feature Prioritization (RICE, MoSCoW)]
    C --> D[Traffic Forecasting Model]
    D --> E[Strategy Dashboard & App]
