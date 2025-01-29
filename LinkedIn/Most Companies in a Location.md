# **Interview Question: SQL Query for Most Companies in a Location**

## **Question:**  
You are given the following database schema for tracking locations, companies, and employees:

## **Schema:**

1. **`location`**  
   - `location_id` (Primary Key)  
   - `location_name` (VARCHAR)  

2. **`companies`**  
   - `company_id` (Primary Key)  
   - `company_name` (VARCHAR)  
   - `location_id` (Foreign Key referencing `location.location_id`)  

3. **`employee`**  
   - `employee_id` (Primary Key)  
   - `employee_name` (VARCHAR)  
   - `company_id` (Foreign Key referencing `companies.company_id`)  

## **Sample Data:**

### **Location Table**
| location_id | location_name  |
|------------|---------------|
| 1          | New York      |
| 2          | San Francisco |
| 3          | Chicago       |

### **Companies Table**
| company_id | company_name | location_id |
|------------|-------------|-------------|
| 101        | ABC Corp     | 1           |
| 102        | XYZ Ltd      | 1           |
| 103        | LMN Inc      | 2           |
| 104        | PQR Co       | 1           |
| 105        | DEF Group    | 3           |

### **Employee Table**
| employee_id | employee_name | company_id |
|------------|--------------|------------|
| 201        | John Doe      | 101        |
| 202        | Jane Smith    | 102        |
| 203        | Alice Brown   | 103        |
| 204        | Bob Johnson   | 104        |
| 205        | Charlie Lee   | 105        |

## **Problem Statement:**  
Write an SQL query to retrieve the `company_name` and `employee_name` for the location that has the **highest number of companies**.

---

## **Expected Output (Based on Sample Data)**  
Since **New York (location_id = 1)** has the most companies (**3 companies: ABC Corp, XYZ Ltd, PQR Co**), the expected result would be:

| company_name | employee_name |
|-------------|--------------|
| ABC Corp    | John Doe     |
| XYZ Ltd     | Jane Smith   |
| PQR Co      | Bob Johnson  |

---

## **Expected SQL Query:**
```sql
WITH LocationRank AS (
    SELECT location_id
    FROM companies
    GROUP BY location_id
    ORDER BY COUNT(company_id) DESC
    LIMIT 1
)
SELECT c.company_name, e.employee_name
FROM companies c
JOIN employee e ON c.company_id = e.company_id
WHERE c.location_id = (SELECT location_id FROM LocationRank);
```


# **Follow-Up Questions:**

## **1. How would you modify the query if multiple locations have the same highest number of companies?**  
If multiple locations have the same highest number of companies, we need to modify the query to return all such locations. Instead of using `LIMIT 1`, we should use a subquery to find the maximum company count and then filter locations matching that count.

### **Example Query:**
```sql
WITH LocationCompanyCount AS (
    SELECT location_id, COUNT(company_id) AS company_count
    FROM Companies
    GROUP BY location_id
)
SELECT c.company_name, e.employee_name
FROM Companies c
JOIN Employees e ON c.company_id = e.company_id
WHERE c.location_id IN (
    SELECT location_id FROM LocationCompanyCount
    WHERE company_count = (SELECT MAX(company_count) FROM LocationCompanyCount)
);
```
This ensures all locations with the highest company count are considered.

---

## **2. Can you optimize this query for large datasets?**  
For better performance on large datasets:

### **Indexes:**  
Create indexes on `Companies.location_id`, `Companies.company_id`, and `Employees.company_id` to speed up filtering and joins.
```sql
CREATE INDEX idx_companies_location ON Companies (location_id);
CREATE INDEX idx_companies_id ON Companies (company_id);
CREATE INDEX idx_employees_company ON Employees (company_id);
```

### **Partitioning:**  
If the dataset is massive, consider partitioning the `Companies` table by `location_id` and the `Employees` table by `company_id`.

### **Materialized Views:**  
If frequent reports are needed, use a **materialized view** to store pre-aggregated results.
```sql
CREATE MATERIALIZED VIEW LocationCompanySummary AS
SELECT location_id, COUNT(company_id) AS company_count
FROM Companies
GROUP BY location_id;
```

---

## **3. How would you write this query using a different approach, such as a JOIN instead of CTE?**  
A **JOIN-based approach** can be used instead of a **CTE** to get the highest number of companies per location:

### **Example Query:**
```sql
SELECT c.company_name, e.employee_name
FROM Companies c
JOIN Employees e ON c.company_id = e.company_id
JOIN (
    SELECT location_id, COUNT(company_id) AS company_count
    FROM Companies
    GROUP BY location_id
    HAVING COUNT(company_id) = (
        SELECT MAX(company_count)
        FROM (SELECT location_id, COUNT(company_id) AS company_count FROM Companies GROUP BY location_id) AS subquery
    )
) lc ON c.location_id = lc.location_id;
```
This approach ensures we retrieve employees from all locations with the maximum number of companies.

---

These follow-up questions help assess a candidate’s ability to handle **dynamic queries, indexing, performance optimization, and alternative SQL approaches**. Let me know if you need further refinements! 🚀


