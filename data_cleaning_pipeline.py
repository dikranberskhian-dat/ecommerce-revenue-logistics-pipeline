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
df_merge = pd.merge(df_merge, df_products_ds, on="product_id", how="inner" )

