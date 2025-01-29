# **SQL Interview Question: Transform Test Scores into Columns**

## **Question:**  
You are given two tables, `Users` and `Tests`, which store user information and their test scores. Your task is to write an SQL query that displays `user_id`, the scores for `test_1`, `test_2`, `test_3`, and the `total_test_score` for each user.

---

## **Schema:**

### **Users Table**
| Column   | Data Type | Description                 |
|----------|----------|-----------------------------|
| user_id  | INT (PK) | Unique identifier for users |

### **Tests Table**
| Column    | Data Type | Description                           |
|-----------|----------|---------------------------------------|
| user_id   | INT (FK) | References `Users.user_id`           |
| test_name | VARCHAR  | Name of the test (`test_1`, `test_2`, `test_3`) |
| test_score | INT     | Score obtained in the test           |

---

## **Sample Data:**

### **Users Table**
| user_id |
|---------|
| 1       |
| 2       |
| 3       |

### **Tests Table**
| user_id | test_name | test_score |
|---------|----------|------------|
| 1       | test_1   | 85         |
| 1       | test_2   | 90         |
| 1       | test_3   | 78         |
| 2       | test_1   | 70         |
| 2       | test_2   | 88         |
| 2       | test_3   | 92         |
| 3       | test_1   | 75         |
| 3       | test_3   | 80         |

---

## **Expected Output:**

| user_id | test_1 | test_2 | test_3 | total_test_score |
|---------|--------|--------|--------|------------------|
| 1       | 85     | 90     | 78     | 253              |
| 2       | 70     | 88     | 92     | 250              |
| 3       | 75     | 0      | 80     | 155              |

---

## **Expected SQL Query:**
```sql
SELECT 
    u.user_id,
    COALESCE(MAX(CASE WHEN t.test_name = 'test_1' THEN t.test_score END), 0) AS test_1,
    COALESCE(MAX(CASE WHEN t.test_name = 'test_2' THEN t.test_score END), 0) AS test_2,
    COALESCE(MAX(CASE WHEN t.test_name = 'test_3' THEN t.test_score END), 0) AS test_3,
    COALESCE(SUM(t.test_score), 0) AS total_test_score
FROM Users u
LEFT JOIN Tests t ON u.user_id = t.user_id
GROUP BY u.user_id;


# **Follow-Up Questions:**

## **1. How would you modify the query if the number of test types (**``**, **``**, etc.) is dynamic and unknown?**

If the test types are dynamic, a **static SQL query won't be sufficient**. Instead, you would need to **generate a dynamic SQL query** that retrieves all distinct `test_name` values and pivots them dynamically.

### **Example approach in MySQL / PostgreSQL:**

- Fetch distinct test names:
  ```sql
  SELECT DISTINCT test_name FROM Tests;
  ```
- Use this list to dynamically generate the `CASE WHEN` statements.
- Execute the generated SQL query.

### **Dynamic PIVOT in SQL Server:**

```sql
DECLARE @cols AS NVARCHAR(MAX), @query AS NVARCHAR(MAX);

SELECT @cols = STRING_AGG(QUOTENAME(test_name), ',') FROM (SELECT DISTINCT test_name FROM Tests) AS t;

SET @query =
'SELECT user_id, ' + @cols + ', COALESCE(SUM(test_score), 0) AS total_test_score
FROM
(
    SELECT user_id, test_name, test_score FROM Tests
) src
PIVOT
(
    MAX(test_score) FOR test_name IN (' + @cols + ')
) p
GROUP BY user_id';

EXEC sp_executesql @query;
```

This approach ensures that new test types are handled dynamically without modifying the SQL query.

---

## **2. Can you optimize this query for large datasets with indexing or a different approach?**

For better performance on large datasets:

### **Indexes:**

Create indexes on `Tests.test_name`, `Tests.user_id`, and `Tests.test_score` to speed up filtering and aggregation.

```sql
CREATE INDEX idx_tests_user ON Tests (user_id);
CREATE INDEX idx_tests_name ON Tests (test_name);
```

### **Partitioning:**

If the dataset is massive, consider partitioning the `Tests` table by `user_id` to optimize queries.

### **Materialized Views:**

If frequent reports are needed, use a **materialized view** to store pre-aggregated test results.

---

## **3. How would you handle cases where a user hasn't taken any tests?**

The current query already handles this by using a **LEFT JOIN** between `Users` and `Tests`.

- If a user has no tests, `COALESCE(MAX(...), 0)` ensures missing test scores appear as `0`.
- The total score will also be `0`.

### **Example case:**

| user\_id | test\_1 | test\_2 | test\_3 | total\_test\_score |
| -------- | ------- | ------- | ------- | ------------------ |
| 4        | 0       | 0       | 0       | 0                  |

---

## **4. Can this be achieved using PIVOT in databases that support it (e.g., SQL Server)?**

Yes, SQL Server supports **PIVOT**, which is a more efficient way to transform rows into columns.

### **Example query using PIVOT in SQL Server:**

```sql
SELECT user_id, test_1, test_2, test_3,
       COALESCE(test_1, 0) + COALESCE(test_2, 0) + COALESCE(test_3, 0) AS total_test_score
FROM (
    SELECT user_id, test_name, test_score FROM Tests
) src
PIVOT (
    MAX(test_score) FOR test_name IN (test_1, test_2, test_3)
) p;
```

This approach avoids `CASE WHEN` statements and improves readability and maintainability.

---

These follow-up questions help assess a candidate’s ability to handle **dynamic queries, indexing, performance optimization, and SQL pivoting techniques**. Let me know if you need further refinements! 🚀


