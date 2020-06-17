# Sparse Array

#### 1️⃣ Solution Summary

The main idea around this specific implementation is to create a better performing solution than that of nested for loops between the strings and queries inputs through utilizing a hashtable that will be populated initially with each value in the queries table as the key and number of instances in the strings array as the value (initialized first to 0).

Through using a hashtable I was able to only use a single for loop to query through the strings array since hashtables have almost a 0(1) time complexity for key lookup

---

### Technologies Used

- Python

---

## 2️⃣ Challenge Information

| Title        | Challenge URL | Time Complexity | Space Complexity | Difficulty |
| ------------ | ------------- | --------------- | ---------------- | ---------- |
| Sparse Array |               | O(mn)           | O(n)             | Easy       |

## 3️⃣ Time / Space Complexity

### Time Complexity

- O(n)

- Rationale:

### Space Complexity

- O(n)

- Rationale:
