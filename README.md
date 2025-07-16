# 📊 A/B Testing Analysis API

## 🎯 Project Overview

This project demonstrates an end-to-end A/B test analysis workflow, from data cleaning to statistical testing and API deployment.

**Goal:**
Determine whether a new landing page improves conversion rates compared to the old page using a two-sided z-test.

The project includes:

* Data cleaning and preprocessing
* Conversion rate calculations
* Statistical significance testing (z-test)
* Visualizations (Python)
* A FastAPI endpoint to automate the analysis

---

## 🗂️ Dataset

**File:** `ab_data.csv`
**Columns:**

* `user_id`: Unique user identifier
* `timestamp`: Timestamp of page view
* `group`: Assigned group (`control` or `treatment`)
* `landing_page`: Page shown (`old_page` or `new_page`)
* `converted`: Whether the user converted (`0` or `1`)

---

## 🔍 Problem Statement

Test whether showing the **new landing page** increases conversion rates relative to the old page.

* **Null Hypothesis (H0):** Conversion rate (control) = Conversion rate (treatment)
* **Alternative Hypothesis (H1):** Conversion rates differ

---

## 🧹 Data Cleaning

Key preprocessing steps:
✅ Remove rows with duplicate `user_id` (keeping the first occurrence)
✅ Verify consistency between `group` and `landing_page`
✅ Confirm final group sizes are balanced

After cleaning, there were \~286,000 unique users.

---

## 📈 Statistical Analysis

**Test Used:** Two-sided z-test for proportions

Steps:

1. Calculate conversion rates:

   * Control: \~12.03%
   * Treatment: \~11.88%
2. Compute pooled conversion rate.
3. Calculate Standard Error (SE).
4. Compute z-score:

   $$
   z = \frac{p_t - p_c}{SE}
   $$
5. Compute p-value:

   $$
   p = 2 \times (1 - \Phi(|z|))
   $$

   where $\Phi$ is the CDF of the standard normal distribution.

---

**Results:**

* **Difference in conversion:** \~ -0.14%
* **Z-score:** \~ -1.20
* **P-value:** \~0.23

✅ **Interpretation:**
Since p > 0.05, we fail to reject the null hypothesis. There is **no statistically significant difference** in conversion rates between the two pages.

---

## 📊 Visualizations

Two plots were generated using Matplotlib:

1. **Conversion Rates by Group:**

   * Bar chart comparing control and treatment rates.

2. **Difference in Conversion Rates with Confidence Interval:**

   * Error bar showing 95% confidence interval.

---

## 🧪 FastAPI Endpoint

The project includes an API endpoint to analyze new datasets.

**Route:**

```
POST /ab_test
```

**Description:**

* Accepts a CSV file in the same format (`ab_data.csv`).
* Returns JSON with:

  * Control conversion rate
  * Treatment conversion rate
  * Difference
  * Pooled conversion rate
  * Standard Error
  * Z-score
  * P-value

---

## 🚀 How to Run the API Locally

1️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

2️⃣ **Start the API:**

```bash
uvicorn main:app --reload
```

3️⃣ **Visit the Swagger UI:**

```
http://127.0.0.1:8000/docs
```

4️⃣ **Upload a CSV and get results!**

---

## 🛠 Example API Response

```json
{
  "Control conversion rate ": 0.1203,
  "Treatment conversion rate": 0.11884,
  "Difference": -0.00145,
  "Pooled conversion rate": 0.11957,
  "Standard Error": 0.0012,
  "Z-score": -1.20838,
  "P value": 0.2269
}
```

---

## 📚 Business Recommendation

Since the observed difference in conversion rates was not statistically significant, there is no evidence that the new landing page outperforms the old one. The recommendation is to **retain the existing page** or test alternative designs in future experiments.

---

## ✨ Future Improvements

* Deploy the API to a cloud platform (Render/AWS)
* Add an endpoint returning graph images
* Build a Streamlit dashboard for interactive analysis
* Support multiple variants (A/B/C testing)

---

## 🙌 Acknowledgements

Dataset adapted from Udacity A/B Testing project materials.

---

## 📇 Contact

Feel free to connect if you have questions or would like to discuss improvements!

---
