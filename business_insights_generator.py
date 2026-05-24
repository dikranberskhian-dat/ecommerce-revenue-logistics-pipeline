import pandas as pd

df_customers = pd.read_csv("olist_customers_dataset.csv")
df_location = pd.read_csv("olist_geolocation_dataset.csv")
df_orders_main = pd.read_csv("olist_order_items_dataset.csv")
df_orders_payments = pd.read_csv("olist_order_payments_dataset.csv")
df_customers_reviews = pd.read_csv("olist_order_reviews_dataset.csv")
df_orders_ds = pd.read_csv("olist_orders_dataset.csv")
df_products_ds = pd.read_csv("olist_products_dataset.csv")
df_sellers_ds = pd.read_csv("olist_sellers_dataset.csv")


df_merge = pd.merge(df_orders_main, df_customers_reviews, on="order_id", how="left")
df_merge = pd.merge(df_merge, df_products_ds, on="product_id", how="inner")
df_merge = pd.merge(df_merge, df_orders_payments, on="order_id", how="inner")


df_final_marketplace = pd.merge(df_merge, df_orders_ds, on="order_id", how="inner")

date_cols = ['shipping_limit_date',
             'review_creation_date',
             'review_answer_timestamp',
             'order_delivered_customer_date',
             'order_estimated_delivery_date']
for col in date_cols:
    df_final_marketplace[col] = pd.to_datetime(df_final_marketplace[col])

df_final_marketplace["delivery_delay_days"] = (
        df_final_marketplace["order_delivered_customer_date"] -
        df_final_marketplace["order_estimated_delivery_date"]).dt.days

print("=" * 40 + "\nLOGISTICS INSIGHTS")
print("=" * 40)

logistics_summary = df_final_marketplace.groupby('review_score')['delivery_delay_days'].mean()
print(logistics_summary)
print("\n")
print("=" * 40 + "\nFINANCIAL INSIGHTS")
print("=" * 40)

payment_summary = df_final_marketplace.groupby('payment_type')['payment_value'].mean().sort_values(ascending=False)
print(payment_summary)

# 7. Export clean results for your portfolio summary
with open("portfolio_results.txt", "w") as f:
    f.write("=== BRAZILIAN E-COMMERCE PORTFOLIO RAW DATA ===\n\n")
    f.write("1. LOGISTICS INSIGHTS (Average Delivery Delay by Review Score):\n")
    f.write(logistics_summary.to_string())
    f.write("\n\n2. FINANCIAL INSIGHTS (Average Order Value by Payment Type):\n")
    f.write(payment_summary.to_string())

print("Portfolio data successfully exported to portfolio_results.txt!")