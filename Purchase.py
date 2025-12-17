import pandas as pd
import streamlit as st

# --------------------------------------
# APP TITLE
# --------------------------------------
st.title("📦 Purchase Order Dashboard")

# --------------------------------------
# LOAD DATA
# --------------------------------------
df = pd.read_json("purchase.json")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Total Purchase Value per Order
df["Total"] = df["Quantity"] * df["UnitPrice"]

st.subheader("📄 Overall Purchase Details")
st.dataframe(df)

# --------------------------------------
# 1. TOTAL NUMBER OF ORDERS
# --------------------------------------
total_orders = df["OrderID"].count()
st.metric("1️⃣ Total Orders", total_orders)

# --------------------------------------
# 2. TOTAL PURCHASE VALUE
# --------------------------------------
total_purchase_value = df["Total"].sum()
st.metric("2️⃣ Total Purchase Value", f"₹{total_purchase_value:,.2f}")

# --------------------------------------
# 3. TOTAL PURCHASE VALUE BY SUPPLIER
# --------------------------------------
st.subheader("3️⃣ Total Purchase Value by Supplier")
supplier_total = df.groupby("Supplier")["Total"].sum()
st.bar_chart(supplier_total)

# --------------------------------------
# 4. TOTAL PURCHASE VALUE BY PRODUCT
# --------------------------------------
st.subheader("4️⃣ Total Purchase Value by Product")
product_total = df.groupby("Product")["Total"].sum()
st.bar_chart(product_total)

# --------------------------------------
# 5. TOTAL PURCHASE VALUE BY REGION
# --------------------------------------
st.subheader("5️⃣ Total Purchase Value by Region")
region_total = df.groupby("Region")["Total"].sum()
st.bar_chart(region_total)

# --------------------------------------
# 6. TOP SUPPLIERS BY PURCHASE VALUE
# --------------------------------------
st.subheader("6️⃣ Top Suppliers by Purchase Value")
top_suppliers = (
    df.groupby("Supplier")["Total"]
    .sum()
    .sort_values(ascending=False)
)
st.dataframe(top_suppliers.reset_index())

# --------------------------------------
# 7. TOP PRODUCTS BY QUANTITY ORDERED
# --------------------------------------
st.subheader("7️⃣ Top Products by Quantity Ordered")
top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
st.dataframe(top_products.reset_index())

# --------------------------------------
# 8. ORDERS WITH QUANTITY > THRESHOLD
# --------------------------------------
st.subheader("8️⃣ Orders with Quantity > Threshold")

threshold = st.number_input(
    "Select Quantity Threshold",
    min_value=1,
    value=5
)

filtered_qty_orders = df[df["Quantity"] > threshold]
st.dataframe(filtered_qty_orders)

# --------------------------------------
# 9. MONTHLY PURCHASE TREND
# --------------------------------------
st.subheader("9️⃣ Monthly Purchase Trend")

df["Month"] = df["Date"].dt.to_period("M")

monthly_trend = (
    df.groupby("Month")["Total"]
    .sum()
    .reset_index()
)

monthly_trend["Month"] = monthly_trend["Month"].astype(str)
monthly_trend = monthly_trend.set_index("Month")

st.line_chart(monthly_trend)

# --------------------------------------
# 10. AVERAGE ORDER VALUE PER SUPPLIER
# --------------------------------------
st.subheader("🔟 Average Order Value per Supplier")

avg_order_value = (
    df.groupby("Supplier")["Total"]
    .mean()
    .sort_values(ascending=False)
)

st.dataframe(avg_order_value.reset_index())

# --------------------------------------
# 11. ORDERS BY STATUS
# --------------------------------------
st.subheader("1️⃣1️⃣ Orders by Status")

order_status = (
    df.groupby("Status")
    .size()
    .reset_index(name="Order Count")
)

st.bar_chart(order_status.set_index("Status"))

# --------------------------------------
# 12. HIGH-VALUE ORDERS HIGHLIGHT
# --------------------------------------
st.subheader("1️⃣2️⃣ High-Value Orders Highlight")

high_value_threshold = st.number_input(
    "Select High-Value Order Threshold (₹)",
    min_value=100,
    value=500
)

high_value_orders = df[df["Total"] > high_value_threshold]

def highlight_large_orders(row):
    return ["background-color: #ffcccc"] * len(row)

st.dataframe(
    high_value_orders.style.apply(highlight_large_orders, axis=1)
)

# --------------------------------------
# 13. DAILY PURCHASE TREND
# --------------------------------------
st.subheader("1️⃣3️⃣ Daily Purchase Trend")

daily_trend = df.groupby("Date")["Total"].sum()
st.line_chart(daily_trend)

# --------------------------------------
# 14. AVERAGE UNIT PRICE PER PRODUCT
# --------------------------------------
st.subheader("1️⃣4️⃣ Average Unit Price per Product")

avg_unit_price = (
    df.groupby("Product")["UnitPrice"]
    .mean()
    .sort_values(ascending=False)
)

st.dataframe(avg_unit_price.reset_index())

# --------------------------------------
# 15. FILTERED ORDERS BY STATUS & REGION
# --------------------------------------
st.subheader("1️⃣5️⃣ Filter Orders by Status & Region")

status_filter = st.multiselect(
    "Select Status",
    df["Status"].unique(),
    default=df["Status"].unique()
)

region_filter = st.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_orders = df[
    (df["Status"].isin(status_filter)) &
    (df["Region"].isin(region_filter))
]

st.dataframe(filtered_orders)
