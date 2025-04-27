Virgin Media Broadband Quality Analysis 🚀

Overview 📊
This project analyzes the quality of Virgin Media’s broadband service by investigating real-world KPI measurements including packet loss, disconnection rates, latency trends, and download speeds across different broadband packages, hub types, and regions (Central vs Southern).

The project builds upon the dataset provided during the Virgin Media Hackathon, where my team and I were proud winners 🏆.
I extended the analysis to create deeper insights, propose targeted network improvements, and build predictive tools for future broadband optimization.

Tools and Technologies 🛠️
Power BI — Data visualization and KPI tracking

Python (Streamlit) — Interactive web app development

Hugging Face Spaces — Model deployment and remote access

Pandas, Plotly — Data cleaning and advanced visualizations

Git, GitHub — Version control and project hosting

Key Business Issues Investigated 🔍
High packet loss incidents affecting certain users

Disconnection patterns across different locations

Latency fluctuations across weekdays

Download speed performance across broadband tiers

Regional quality differences (Central vs Southern)

Hub device and broadband package performance gaps

Key Findings 📈
1. Packet Loss Trends
Overall packet loss remained low (~0.04%–0.05%).

Hub C devices had slightly elevated packet loss, especially in Expert Gamer and Surf&Stream tiers.

👉 Action: Investigate Hub C device performance and optimize midweek traffic routing.

2. Disconnection Patterns
Disconnection spikes identified around December 13–14 mainly in Central regions.

Central hubs reported significantly higher disconnection counts than Southern.

👉 Action: Root-cause analysis and predictive maintenance recommended.

3. Latency Insights
Average latency was consistently low (~13ms).

Slight increases observed midweek (Wednesday/Thursday).

👉 Action: Midweek traffic balancing strategies to sustain performance.

4. Download Speed Performance
All-Rounder Tier offered the highest average download speeds (~1200 Mbps).

Expert Gamer and Surf&Stream Tiers reported lower speeds (~600 Mbps and ~470 Mbps).

👉 Action: Promote All-Rounder for premium users; optimize mid-day performance dips.

5. Hub Type and Package Performance
Hub A and Hub B outperformed Hub C across all tiers.

Hub C associated with slightly higher packet loss and slower speeds.

👉 Action: Upgrade or replace underperforming Hub C devices.

Solution Summary ✅

Issue	Proposed Solution
Packet Loss	Hardware optimization and midweek traffic balancing
Disconnections	Predictive maintenance and regional upgrades
Latency	Load balancing on peak weekdays
Download Speed Drops	Improve Surf&Stream tiers and midday load distribution
Regional Gaps	Central region stability focus; Southern region speed improvements
Project Deployment 🚀
Power BI Dashboard:
Visualizes KPI metrics across locations, hubs, and packages.

Streamlit App:
Allows users to interactively explore network quality indicators.

Hugging Face App:
Provides a remote-access platform for disconnection risk prediction based on real-time network conditions.

📂 Explore the Project

🔗 Hugging Face Spaces App : https://huggingface.co/spaces/EOEOkunfolami/virgin-media-disconnect-predictor

🔗 Power BI Dashboard Screenshots : 

📸 Key Visualizations

Insight	Screenshot
Overall KPI Summary	
Packet Loss Trends (Hub C)	
Disconnection Patterns	
Latency Trends by Weekday	
Download Speed by Package	
Regional Differences

Conclusion 🏁
By continuously monitoring packet loss, download speeds, latency, and disconnections, Virgin Media can enhance broadband quality, boost customer satisfaction, and reduce churn.
Data-driven strategies, predictive analytics, and proactive infrastructure upgrades are key steps forward.

About Me 🎯
I am passionate about combining data science, analytics, and machine learning to uncover hidden opportunities for service improvement.
Winning the Virgin Media Hackathon was a proud moment — and this project extends that journey into solving real-world challenges.

Let's keep building solutions that matter! 🚀

Tags
#DataAnalytics #VirginMedia #BroadbandQuality #Streamlit #PowerBI #HackathonWinner #PredictiveAnalytics #HuggingFaceSpaces