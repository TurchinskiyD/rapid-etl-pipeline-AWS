
# AWS Lambda функції

Цей каталог містить код для двох AWS Lambda-функцій, що обробляють файли з даними нерухомості Zillow у S3.

---

## 📂 copy-raw-json-file-lambda-func.py

**Що робить:**
- Копює новий JSON-файл із landing S3-бакету (`for-rapid-etl-pipelin-backet`) до копіювального бакету (`for-rapid-copy-raw-json-bucket`).

**Сценарій спрацювання:**
- Подія `ObjectCreated:*` у бакеті `for-rapid-etl-pipelin-backet`

**Призначення:**
- Забезпечує резервне зберігання JSON до обробки.

---

## 📂 transform-to-csv-lambda-func.py

**Що робить:**
- Читає JSON-файл із S3 скопйований ламбдою, обрабляє масив `results`, обирає поля та конвертує у CSV.
- Завантажує CSV-файл у бакет `for-rapid-cleaned-data-bucket`

**Вибрані колонки:**
- `zipcode`, `city`, `homeType`, `homeStatus`, `livingArea`, `bathrooms`, `bedrooms`, `price`, `zestimate`

**Сценарій спрацювання:**
- Подія `ObjectCreated:*` у бакеті `for-rapid-copy-raw-json-bucket`

**Призначення:**
- Трансформує JSON у CSV для подальшого завантаження в Redshift

---

## 🔗 Рекомендації

- Створи події S3 (trigger) для кожної функції.
- Ролі IAM мають містити тільки необхідні привілеї до S3.
- Перевіряй обєм та формат JSON перед обробкою.
