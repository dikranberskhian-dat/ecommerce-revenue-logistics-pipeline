```markdown
# Brazilian E-Commerce Business Insights Generator

An end-to-end data processing pipeline that merges, cleans, and analyzes relational e-commerce data from the **Olist Dataset** (Brazilian eCommerce public dataset). The script engineers operational metrics to uncover how fulfillment logistics directly impact customer satisfaction and analyzes purchasing behaviors across payment channels.

---

## 🚀 Features

* **Relational Data Integration:** Merges multiple relational datasets (Orders, Payments, Reviews, Products) using optimized `pandas` merge operations.
* **Feature Engineering:** Converts raw timestamps into datetime objects and calculates `delivery_delay_days` to measure actual vs. estimated delivery timelines.
* **Operational Analytics:** Grouped aggregations mapping average logistics delays directly against customer `review_score`.
* **Financial Segmentation:** Isolates average order values across different payment methods to evaluate revenue channels.
* **Automated Reporting:** Generates a structured portfolio summary report (`portfolio_results.txt`) for stakeholders.

---

## 📊 Data Architecture & Pipeline

The pipeline handles complex transactional data by systematically resolving entities across multiple data sources:


```

[Orders Main] ──(Left)──> [Reviews] ──(Inner)──> [Products] ──(Inner)──> [Payments] ──(Inner)──> [Orders Master]
│
▼
[Feature Engineering]
│
┌───────────────┴───────────────┐
▼                               ▼
[Logistics Analysis]            [Financial Analysis]

```

---

## 🛠️ Requirements & Installation

Ensure you have Python 3.8+ and `pandas` installed.

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/brazilian-ecommerce-insights.git](https://github.com/yourusername/brazilian-ecommerce-insights.git)
   cd brazilian-ecommerce-insights

```

2. Install dependencies:
```bash
pip install pandas

```


3. Place the Olist CSV datasets in the root directory:
* `olist_customers_dataset.csv`
* `olist_order_items_dataset.csv`
* `olist_order_payments_dataset.csv`
* `olist_order_reviews_dataset.csv`
* `olist_orders_dataset.csv`
* `olist_products_dataset.csv`



---

## 💻 Usage

Run the primary analytical script from your terminal:

```bash
python business_insights_generator.py

```

### Console Output Example:

```text
========================================
LOGISTICS INSIGHTS
========================================
review_score
1.0    12.4
2.0     6.8
3.0     2.1
4.0    -3.5
5.0    -5.2
Name: delivery_delay_days, dtype: float64


========================================
FINANCIAL INSIGHTS
========================================
payment_type
credit_card    163.31
boleto         145.03
debit_card     142.52
voucher         65.78
Name: payment_value, dtype: float64

Portfolio data successfully exported to portfolio_results.txt!

```

---

## 📈 Insights Generated

### 1. Logistics Impact on Retention (`Logistics Insights`)

By calculating the delta between the estimated delivery window and actual arrival, the script exposes a clear correlation: negative values (early deliveries) strongly align with 4 and 5-star ratings, while delayed timelines sharply trigger 1 and 2-star reviews.

### 2. Transactional Value Distribution (`Financial Insights`)

Analyzes the average purchasing power associated with each payment type, revealing which payment gateways secure the highest ticket sizes (e.g., Credit Card vs. Voucher).

---

## 📂 Output

Upon execution, the script generates a clean text asset designed for portfolios:

* `portfolio_results.txt`: Contains raw text-based summaries of both logistical metrics and financial summaries, formatted perfectly for inclusion in markdown files, case studies, or resumes.

```

```
