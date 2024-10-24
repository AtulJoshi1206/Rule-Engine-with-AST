# 🚀 Rule Engine Project

## 📚 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Test Cases](#test-cases)
- [Snapshots](#snapshots)
- [Conclusion](#conclusion)

---

## Project Overview
The **Rule Engine Project** aims to create a dynamic rule engine capable of evaluating user eligibility based on various attributes, such as **age**, **department**, **income**, and **spending**. This project employs an **Abstract Syntax Tree (AST)** for logical operations and rule management.

### Objectives
- **Create Rules**: Define rules using logical operators.
- **Combine Rules**: Merge multiple rules into a cohesive unit.
- **Evaluate Rules**: Assess rules against provided JSON data.
- **Modify Rules**: Update existing rules seamlessly.

---

## Features
✨ **Key Features of the Project**:
- **Create Rule**: Define rules with complex logical conditions using AND/OR operators.
- **Combine Rules**: Merge multiple rules into one, optimizing rule evaluation.
- **Evaluate Rule**: Test rules against specific data inputs for eligibility verification.
- **Modify Rule**: Easily update existing rules with new expressions.

---

## 🛠 Technologies Used
| Technology         | Description                                           |
|--------------------|-------------------------------------------------------|
| **Python**         | Main programming language for backend development     |
| **Flask**          | Web framework for building the API                   |
| **MongoDB Atlas**  | NoSQL database for storing rules and evaluations      |
| **HTML/CSS/JavaScript** | Frontend technologies for user interface          |
| **Requests**       | Library for API testing and integration               |

---

## Installation
### Steps to Set Up the Project:
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd rule-engine-project
   ```
   
2. **Install Required Packages**:
   ```bash
   pip install Flask pymongo
   ```
   
3. **Set Up MongoDB Atlas**:
   - Create a MongoDB Atlas account.
   - Update connection details in the Flask application.

4. **Run the Flask Application**:
   ```bash
   python app.py
   ```

---

## Usage
1. **Open the GUI** in your web browser.
2. **Fill out the forms** to:
   - **Create Rules**: Enter logical expressions and submit.
   - **Combine Rules**: Provide comma-separated rule IDs.
   - **Evaluate Rules**: Input a rule ID along with JSON data.
   - **Modify Rules**: Update existing rules with new expressions.

---

## 📡 API Endpoints
| Endpoint                    | Method | Description                                                  | Request Body                                      |
|-----------------------------|--------|--------------------------------------------------------------|--------------------------------------------------|
| `/create_rule`              | POST   | Creates a new rule based on the provided rule string        | `{ "rule_string": "<rule_expression>" }`        |
| `/combine_rules`            | POST   | Combines multiple rules into one                             | `{ "rule_ids": ["<rule_id_1>", "<rule_id_2>"] }` |
| `/evaluate_rule`            | POST   | Evaluates a specific rule against provided data             | `{ "rule_id": "<rule_id>", "data": <json_data> }` |
| `/modify_rule`              | POST   | Modifies an existing rule with a new expression             | `{ "rule_id": "<rule_id>", "new_rule_string": "<new_rule_expression>" }` |

---

## 🧪 Test Cases
### Create Rule
- **Input**: 
  - Rule String: `(age > 30 AND department = 'Sales')`
- **Output**: 
  - Response: `{'ast': '<AST representation>', 'id': '6719b0eaf49d41c79d088beb'}`

### Combine Rules
- **Input**: 
  - Rule IDs: `6719b0eaf49d41c79d088beb, 6719b154f49d41c79d088bec`
- **Output**: 
  - Response: `{'combined_ast': '<Combined AST representation>', 'id': '6719b196f49d41c79d088bed'}`

### Evaluate Rule
- **Input**: 
  - Rule ID: `6719b196f49d41c79d088bed`
  - Data: `{"age": 35, "department": "Sales", "salary": 60000, "experience": 6}`
- **Output**: 
  - Response: `{'result': True}`

### Modify Rule
- **Input**: 
  - Rule ID: `6719b0eaf49d41c79d088beb`
  - New Rule String: `(age > 40 AND department = 'HR')`
- **Output**: 
  - Response: `{'message': 'Rule updated successfully'}`

---

## 📸 Snapshots

### Create Rule
![Create Rule](https://github.com/user-attachments/assets/b6694b63-38af-4fef-b92b-cf0da57b7010)

### Combine Rules
![Combine Rules](https://github.com/user-attachments/assets/aaf63288-f91d-48c0-92ac-4757baaeafb6)

### Evaluate Rule
![Evaluate Rule](https://github.com/user-attachments/assets/f3bf5174-5a68-49f1-b204-5eab49987bd1)

### Modify Rule
![Modify Rule](https://github.com/user-attachments/assets/65960ef5-fa89-441b-bd25-0025bfcb61b5)

### Simple UI
![Simple UI](https://github.com/user-attachments/assets/7c4d5228-afa6-4a7c-b5bb-55c9cf8819de)

### Process
![Process](https://github.com/user-attachments/assets/08cda11f-cc72-4b46-bd14-4fe0f6228b67)

### Database
![Database](https://github.com/user-attachments/assets/a1034a29-336b-4805-9489-08e60ef98db9)

---

## Conclusion
The **Rule Engine Project** showcases the capability to dynamically create, combine, evaluate, and modify rules through a user-friendly interface. It meets all assignment criteria and serves as a robust solution for eligibility determination based on user-defined conditions.

### 🎉 Thank you for exploring the Rule Engine Project! 
Feel free to contribute, suggest improvements, or report issues!

---
