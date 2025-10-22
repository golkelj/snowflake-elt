# ❄️ Snowflow ELT Pipeline (Airflow + dbt + Snowflake)

A modern end-to-end **ELT (Extract, Load, Transform) data engineering pipeline** orchestrated with **Apache Airflow**, transformed with **dbt**, and warehoused in **Snowflake** to have customer data viable for analytics. This project demonstrates staging & marts layering, CI/CD-friendly modular dbt models, and repeatable automation for analytics engineering, using the Cloud via Snowflake.


*NOTE: I did not have massive amount of data laying around so I used premade datasets

---

## 🚀 Project Overview

| Step | Tool | Description |
|------|------|-------------|
| 🟦 Extract | Airflow | Extracts raw CSV/API data (or scheduled ingestion) |
| 🟨 Load | Snowflake | Raw data is landed into Snowflake as-is |
| 🟩 Transform | dbt | Data is refined into staging → intermediate → marts |
| 🔁 Orchestrate | Airflow DAG | Executes dbt in a layered order |
| ✅ Test | dbt tests | Ensures data quality across layers |

---

