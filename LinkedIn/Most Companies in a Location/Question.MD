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
