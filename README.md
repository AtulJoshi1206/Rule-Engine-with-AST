# Rule Engine using Abstract Syntax Tree (AST)

## Objective:
Develop a simple 3-tier rule engine application (UI, API, Backend) to dynamically determine user eligibility based on attributes like age, department, income, spend, etc. The system leverages an Abstract Syntax Tree (AST) to represent conditional rules, enabling dynamic creation, combination, and modification of these rules.

## Technologies Used:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express.js
- **Database**: MongoDB Atlas (for cloud-based storage of rules and metadata)
- **Data Parsing and Rule Processing**: Abstract Syntax Tree (AST)
- **API Design**: RESTful API for rule creation, combination, and evaluation
- **Deployment**: [Specify if cloud or local server]

## Objective:
The purpose of this application is to:
- Create conditional rules based on user data.
- Dynamically combine and modify these rules using AST.
- Evaluate user data against the rules to determine eligibility.

---

## Data Structure:
The AST is represented using a tree-based structure where each node in the tree represents an operator (AND/OR) or an operand (conditions).

### Sample Data Structure:
- **Node fields**:
  - `type`: String indicating the node type (`"operator"` for AND/OR, `"operand"` for conditions).
  - `left`: Reference to another Node (left child).
  - `right`: Reference to another Node (right child for operators).
  - `value`: Optional value for operand nodes (e.g., number for comparisons).

---

## Data Storage:
We use **MongoDB Atlas** as the storage engine to persist rules and associated metadata.

### Sample MongoDB Schema:
```json
{
  "rule_id": ObjectId("..."),
  "rule": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
  "created_at": ISODate("..."),
  "modified_at": ISODate("...")
}
```

---

## Sample Rules:
1. **Rule 1**:
   ```plaintext
   ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
   ```

2. **Rule 2**:
   ```plaintext
   (age > 30 AND department = 'Marketing') AND (salary > 20000 OR experience > 5)
   ```

---

## API Design:
The application provides the following API endpoints:

1. **`create_rule(rule_string)`**:
   - Input: A string representing a rule (e.g., `((age > 30 AND department = 'Sales') AND salary > 50000)`).
   - Output: Node object representing the corresponding AST.

2. **`combine_rules(rules)`**:
   - Input: List of rule strings.
   - Output: Combined AST root node with minimized redundant checks.

3. **`evaluate_rule(json_data)`**:
   - Input: JSON representing a rule's AST and user data attributes (e.g., `{ "age": 35, "department": "Sales", "salary": 60000 }`).
   - Output: `True` if the user meets the rule criteria, `False` otherwise.

---

## Test Cases:

1. **Test AST Creation**:
   - Use `create_rule` to generate ASTs from the sample rules and verify the structure.

2. **Test Rule Combination**:
   - Combine multiple rules using `combine_rules` and validate the resulting AST.

3. **Test Rule Evaluation**:
   - Test `evaluate_rule` with different user data to ensure the rule evaluates correctly.

---

## Bonus Features:
- **Error Handling**: Handles invalid rule strings or missing operators.
- **Rule Modification**: Support for modifying existing rules by changing operands, operators, or adding/removing sub-expressions.
- **Validation**: Ensures that rule attributes exist within a pre-defined catalog.
- **User-Defined Functions**: Extendable to include user-defined functions for complex conditions (future scope).

---

## Screenshots:
Add screenshots showcasing:
1. Rule Creation
   - ![Rule Creation Screenshot](path_to_screenshot1)
2. Rule Combination
   - ![Rule Combination Screenshot](path_to_screenshot2)
3. Rule Evaluation
   - ![Rule Evaluation Screenshot](path_to_screenshot3)

---

## How to Run the Application:
1. Clone the repository.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up MongoDB Atlas and update the connection string in `.env`.
4. Start the server:
   ```bash
   npm start
   ```
5. Access the application via `localhost:3000` or the deployed URL.

---

## License:
[MIT License]

