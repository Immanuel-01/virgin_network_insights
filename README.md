# Virgin Media Broadband Quality Analysis 🚀

## Overview 
This project analyzes the quality of Virgin Media’s broadband service by investigating real-world KPI measurements including **packet loss**, **disconnection rates**, **latency trends**, and **download speeds** across different broadband packages, hub types, and regions (Central vs Southern).

The project builds upon the dataset provided during the **Virgin Media Hackathon**, where my team and I were proud winners 🏆. I attended the hackathon to develop deeper insights, propose targeted network improvements, and build predictive tools for future broadband optimization.

---

## Tools and Technologies 
- **Power BI** — Data visualization and KPI tracking
- **Python (Streamlit)** — Interactive web app development
- **Hugging Face Spaces** — Model deployment and remote access
- **Pandas, Plotly** — Data cleaning and advanced visualizations
- **Git, GitHub** — Version control and project hosting

---

## Key Business Issues Investigated 🔎
- High packet loss incidents affecting certain users
- Disconnection patterns across different locations
- Latency fluctuations across weekdays
- Download speed performance across broadband tiers
- Regional quality differences (Central vs Southern)
- Hub device and broadband package performance gaps

---

## Key Findings 📊

### 1. Packet Loss Trends 
- Overall packet loss remained low (~0.04%–0.05%).
- Hub C devices had slightly elevated packet loss, especially in Expert Gamer and Surf&Stream tiers.

**Action:** Investigate Hub C device performance and optimize midweek traffic routing.

**Why focus on these days?**  
Research shows that broadband networks experience the highest stress on **Wednesdays, Fridays, and Saturdays** due to increased online traffic.  
Since **packet loss** refers to the failure of network data to reach its destination (often caused by congestion or overload), investigating these peak days provides meaningful insights into when and where the network may become slightly less reliable.

## Wednesday

![Screenshot (630)](https://github.com/user-attachments/assets/01e08472-eeba-4760-86eb-3779944571df)


## Friday

![Screenshot (629)](https://github.com/user-attachments/assets/a9529d6d-9391-4946-b7db-71384702357b)


## Saturday

![Screenshot (628)](https://github.com/user-attachments/assets/d58ddd7c-b573-47ca-82d4-70594b848406)


---

### 2. Disconnection Patterns 
- Disconnection spikes were observed in the Central region, especially around December 13–14.
- Central region had significantly higher disconnection counts than the Southern region.

**Action:** Conduct root-cause analysis of December outages and prioritize Central hubs for proactive stability upgrades.

## Disconnection Pattern in Southern Areas


![Screenshot (632)](https://github.com/user-attachments/assets/3f6c905f-20ef-4d1c-af98-9ec59d6e86f3)

## Disconnection Pattern in Central Areas

![Screenshot (631)](https://github.com/user-attachments/assets/332afa25-df21-46d8-9934-050c28a7e852)


---

### 3. Latency Insights 
- Average latency remained consistently low (~13 ms).
- Minor midweek latency peaks observed (non-critical).

**Action:** Implement midweek load balancing strategies to sustain low latency during peak working days.

## Average Latency in a week


![Screenshot (633)](https://github.com/user-attachments/assets/60aa30c4-1bac-4f6b-b544-7999fa8d8757)


---

### 4. Download Speed Performance 
- The **VM All-Rounder Tier** delivered the highest download speeds (~1200 Mbps).
- **Expert Gamer** and **Surf&Stream** tiers showed lower speeds (~600 Mbps and ~470 Mbps respectively).
- Midday speed dips were minor but notable.

**Action:** Optimize midday bandwidth allocation and promote All-Rounder as the premium experience.

## Average download speed of 470Mbps noticed in VM Surf & Stream Tier in Southern Areas

![Screenshot (636)](https://github.com/user-attachments/assets/e21ca276-ca43-4285-8331-4a620cfa10f6)


## Average download speed of 600Mbps noticed in VM Expert Gamer Tier in Southern Areas

![Screenshot (635)](https://github.com/user-attachments/assets/73c94374-04ed-4f40-9ea1-7156392edad4)


## Average download speed of 1200Mbps noticed in VM All-Rounder Tier in Southern Areas

![Screenshot (634)](https://github.com/user-attachments/assets/24e8b61c-0612-4dac-81e2-2f791b7b6525)

---

### 5. Hub Type and Broadband Package Comparison 
- Hub A and Hub B outperformed Hub C in both packet loss and download speeds.
- All-Rounder package users had the most consistent quality across all hubs.

**Action:** Initiate hub replacement programs focusing first on Hub C users.

---

### 6. Regional Differences 
- Central region: higher disconnection counts but better average speeds.
- Southern region: lower disconnection counts but slightly lower speeds.

**Action:** Stability upgrades for Central hubs and bandwidth enhancements for Southern region.


## Higher disconnection counts but better average speeds noticed in Central region.

![Screenshot (641)](https://github.com/user-attachments/assets/1d872594-7588-438d-80a2-79637539106f)


## Lower disconnection counts but slightly lower speeds noticed in Southern region.

![Screenshot (640)](https://github.com/user-attachments/assets/21c83b54-2381-4345-bcd0-72df7c3cf532)

---

## Project Deployment 🌐
- **Power BI Dashboard:** KPI visualizations across latency, disconnection, packet loss, and download speed metrics.
- **Hugging Face Spaces:** Web-based deployment for remote app access and demonstration. https://huggingface.co/spaces/EOEOkunfolami/virgin-media-disconnect-predictor

---

## Conclusion 
This project demonstrates how continuous, data-driven monitoring through interactive dashboards and predictive analytics can reveal critical broadband service gaps. Broadband providers like Virgin Media can leverage these insights for predictive maintenance, service tier optimization, and improved user experience.

---
