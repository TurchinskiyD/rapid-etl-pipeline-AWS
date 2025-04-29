## rapid-etl-pipeline-AWS

### 🔄 Загальна структура пайплайна

Цей проєкт реалізує ETL-процес збору та обробки даних про нерухомість із Zillow API. Нижче зображено повну схему потоку даних:

![project.png](assets%2Fproject.png)

---

### 🔍 Опис етапів

1. **Zillow API (RapidAPI)** — джерело даних про житло.
2. **Airflow DAG** (запущений на EC2) виконує витяг даних і зберігає їх як JSON у бакеті S3 (Landing Zone).
3. **Lambda #1** автоматично копіює новий JSON-файл у проміжний бакет (Intermediate Zone).
4. **Lambda #2** перетворює JSON у CSV та зберігає результат у третій бакет (Transformed Zone).
5. **Airflow** контролює появу CSV-файлу й автоматично завантажує його в таблицю **Amazon Redshift**.
6. **Amazon QuickSight** використовується для візуалізації завантажених даних.

---
![Airflow_dag_old.jpg](assets%2FAirflow_dag_old.jpg)

---
![Airflow_dag1.png](assets%2FAirflow_dag1.png)

---
![Airflow_dag2.png](assets%2FAirflow_dag2.png)

---
![redshift_query.png](assets%2Fredshift_query.png)

---
![Zillow_home_sales.png](assets%2FZillow_home_sales.png)

Це асинхронний, розподілений і масштабований пайплайн, який поєднує можливості Apache Airflow, AWS Lambda, S3 та Redshift.