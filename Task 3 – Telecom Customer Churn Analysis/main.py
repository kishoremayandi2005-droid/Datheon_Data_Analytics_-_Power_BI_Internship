import pandas as pd

df = pd.read_csv("telco_customer_churn.csv")

print(df.head())
# Total number of customers
total_customers = len(df)

# Number of customers who left
churned_customers = (df["Churn"] == "Yes").sum()

# Number of customers who stayed
retained_customers = (df["Churn"] == "No").sum()

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
# Total number of customers
total_customers = len(df)

# Number of customers who left
churned_customers = (df["Churn"] == "Yes").sum()

# Number of customers who stayed
retained_customers = (df["Churn"] == "No").sum()

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
# Calculate churn rate
churn_rate = (churned_customers / total_customers) * 100

print("Churn Rate:", round(churn_rate, 2), "%")
# Calculate retention rate
retention_rate = (
    retained_customers / total_customers
) * 100

print("Retention Rate:", round(retention_rate, 2), "%")
# Create tenure groups
bins = [0, 12, 24, 36, 48, 60, 72]

labels = [
    "0-12 Months",
    "13-24 Months",
    "25-36 Months",
    "37-48 Months",
    "49-60 Months",
    "61-72 Months"
]

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Count customers in each group
print(df["TenureGroup"].value_counts().sort_index())
# Calculate churn by tenure group

tenure_analysis = df.groupby(
    "TenureGroup",
    observed=True
).agg(
    Total_Customers=("customerID", "count"),
    Churned_Customers=(
        "Churn",
        lambda x: (x == "Yes").sum()
    )
)

# Calculate churn rate for each group
tenure_analysis["Churn_Rate"] = (
    tenure_analysis["Churned_Customers"]
    / tenure_analysis["Total_Customers"]
) * 100

print("\nChurn Analysis by Tenure:")
print(tenure_analysis.round(2))
# Analyze churn by contract type

contract_analysis = df.groupby("Contract").agg(
    Total_Customers=("customerID", "count"),
    Churned_Customers=(
        "Churn",
        lambda x: (x == "Yes").sum()
    )
)

# Calculate churn rate
contract_analysis["Churn_Rate"] = (
    contract_analysis["Churned_Customers"]
    / contract_analysis["Total_Customers"]
) * 100

print("\nChurn Analysis by Contract:")
print(contract_analysis.round(2))
# Analyze churn by payment method

payment_analysis = df.groupby("PaymentMethod").agg(
    Total_Customers=("customerID", "count"),
    Churned_Customers=(
        "Churn",
        lambda x: (x == "Yes").sum()
    )
)

# Calculate churn rate
payment_analysis["Churn_Rate"] = (
    payment_analysis["Churned_Customers"]
    / payment_analysis["Total_Customers"]
) * 100

print("\nChurn Analysis by Payment Method:")
print(payment_analysis.round(2))
# Create monthly charges groups

bins = [0, 35, 70, float("inf")]

labels = [
    "Low Charges",
    "Medium Charges",
    "High Charges"
]

df["ChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Analyze churn by monthly charges

charge_analysis = df.groupby(
    "ChargeGroup",
    observed=True
).agg(
    Total_Customers=("customerID", "count"),
    Churned_Customers=(
        "Churn",
        lambda x: (x == "Yes").sum()
    )
)

# Calculate churn rate

charge_analysis["Churn_Rate"] = (
    charge_analysis["Churned_Customers"]
    / charge_analysis["Total_Customers"]
) * 100

print("\nChurn Analysis by Monthly Charges:")
print(charge_analysis.round(2))
# Filter Fiber Optic customers without Tech Support

high_risk_customers = df[
    (df["InternetService"] == "Fiber optic") &
    (df["TechSupport"] == "No")
]

# Calculate customer counts

total_high_risk = len(high_risk_customers)

churned_high_risk = (
    high_risk_customers["Churn"] == "Yes"
).sum()

# Calculate churn rate

high_risk_churn_rate = (
    churned_high_risk / total_high_risk
) * 100

# Display results

print("\nFiber Optic Customers Without Tech Support")

print("Total Customers:", total_high_risk)

print("Churned Customers:", churned_high_risk)

print(
    "Churn Rate:",
    round(high_risk_churn_rate, 2),
    "%"
)
# Compare high-risk churn rate with overall churn rate

print("\nChurn Rate Comparison")

print(
    "Overall Churn Rate:",
    round(churn_rate, 2),
    "%"
)

print(
    "High-Risk Churn Rate:",
    round(high_risk_churn_rate, 2),
    "%"
)

difference = high_risk_churn_rate - churn_rate

print(
    "Difference:",
    round(difference, 2),
    "percentage points"
)

if difference > 0:
    print("Result: High-risk group has higher churn.")
else:
    print("Result: High-risk group does not have higher churn.")
    print("\nChurn Rate Comparison")
print("Overall Churn Rate:", round(churn_rate, 2), "%")
print("High-Risk Churn Rate:", round(high_risk_churn_rate, 2), "%")

difference = high_risk_churn_rate - churn_rate
print("Difference:", round(difference, 2), "percentage points")
print("\nChurn Rate Comparison")
print("Overall Churn Rate:", round(churn_rate, 2), "%")
print("High-Risk Churn Rate:", round(high_risk_churn_rate, 2), "%")

difference = high_risk_churn_rate - churn_rate
print("Difference:", round(difference, 2), "percentage points")
# STEP 4: TENURE COHORT ANALYSIS

print("\n========== TENURE COHORT ANALYSIS ==========")

bins = [0, 12, 24, 36, 48, 60, 72]
labels = [
    "0-12 Months",
    "13-24 Months",
    "25-36 Months",
    "37-48 Months",
    "49-60 Months",
    "61-72 Months"
]

df["Tenure Group"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

cohort_data = df.groupby(
    "Tenure Group",
    observed=False
).agg(
    Total_Customers=("customerID", "count"),
    Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
)

cohort_data["Churn Rate (%)"] = (
    cohort_data["Churned_Customers"] /
    cohort_data["Total_Customers"] * 100
)

print(cohort_data.round(2))

cohort_data.to_csv(
    "tenure_cohort_analysis.csv"
)

print("\nTenure Cohort Analysis Completed!")
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("Visualizations", exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Churn by Tenure
plt.figure(figsize=(10, 5))
sns.barplot(
    x=cohort_data.index.astype(str),
    y=cohort_data["Churn Rate (%)"]
)
plt.title("Customer Churn Rate by Tenure")
plt.xlabel("Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("Visualizations/tenure_churn.png", dpi=300)
plt.show()
# 2. Churn by Contract
plt.figure(figsize=(9, 5))
sns.barplot(
    data=df,
    x="Contract",
    y=df["Churn"].eq("Yes").astype(int) * 100
)
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("Visualizations/contract_churn.png", dpi=300)
plt.show()


# 3. Churn by Payment Method
payment_data = df.groupby("PaymentMethod")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).reset_index(name="Churn Rate")

plt.figure(figsize=(10, 5))
sns.barplot(data=payment_data, x="PaymentMethod", y="Churn Rate")
plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("Visualizations/payment_churn.png", dpi=300)
plt.show()


# 4. Churn by Monthly Charges
charge_data = df.groupby("ChargeGroup")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).reset_index(name="Churn Rate")

plt.figure(figsize=(8, 5))
sns.barplot(data=charge_data, x="ChargeGroup", y="Churn Rate")
plt.title("Customer Churn by Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("Visualizations/monthly_charges_churn.png", dpi=300)
plt.show()

print("All 4 Visualizations Created Successfully!")