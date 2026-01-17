# Avneet_Sandhu_102303289_Topsis_repo
TOPSIS implementation using Python (command line program)
# TOPSIS Implementation using Python

**Name:** Avneet Sandhu  
**Roll No:** 102303289  
**Course:** Predictive Analytics  
**Assignment:** TOPSIS – Part I

---

## 1. Objective

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method using Python as a command line program, exactly following the steps and formulas provided in class.

### The program:
- Reads a CSV file
- Applies TOPSIS step-by-step
- Calculates performance scores
- Generates ranking of different mobiles
- Saves the result to an output CSV file

---

## 2. Dataset Description

The dataset contains **8 mobile phones** (M1 to M8) and their performance on different parameters (P1 to P5).

### Input File (`data.csv`) Format:

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|------|------|-----|------|-------|
| M1        | 0.88 | 0.77 | 3.3 | 49.9 | 13.71 |
| M2        | 0.61 | 0.37 | 4.1 | 63.8 | 17.22 |
| ...       | ...  | ...  | ... | ...  | ...   |

---

## 3. Methodology

### Step 1: Convert Categorical to Numeric
*(Not required here as dataset is already numeric)*

### Step 2.1: Vector Normalization
Root of sum of squares is calculated for each column.

### Step 2.2: Normalized Decision Matrix
Each value is divided by its column root sum square.

### Step 3.1: Weight Assignment
Weights are provided through command line.

### Step 3.2: Weighted Normalized Decision Matrix
Normalized matrix × weights

### Step 4: Ideal Best & Ideal Worst
Based on impacts (+ or -)

### Step 5: Euclidean Distance
Distance from ideal best and ideal worst

### Step 6: Performance Score
Calculation of TOPSIS score using distances

### Step 7: Ranking
Higher score = better rank

---

## 4. How to Run the Program 

### Command:
```bash
python topsis.py data.csv 0.2,0.2,0.2,0.2,0.2 -,+,+,+,+ output.csv
```

### Arguments:
1. **Input CSV file** - Path to the input data file
2. **Weights** - Comma-separated weights (e.g., `0.2,0.2,0.2,0.2,0.2`)
3. **Impacts** - Comma-separated impacts (`+` or `-`)
4. **Output CSV file name** - Name for the output file

---

## 5. Output

The program generates `output.csv` containing:
- **Topsis Score** - Calculated performance score
- **Rank** - Ranking based on score

### Sample Output:

| Fund Name | Topsis Score | Rank |
|-----------|--------------|------|
| M3        | 0.69         | 1    |
| M4        | 0.53         | 2    |
| M1        | 0.53         | 3    |
| ...       | ...          | ...  |

---

## 6. Validations Implemented ✓

The program includes comprehensive error handling:

-  Correct number of parameters
-  File not found handling
-  Minimum 3 columns check
-  Numeric value validation
-  Weights & impacts length check
-  Impacts must be `+` or `-`
-  Proper error messages

---

## 7. Files in Repository

| File | Description |
|------|-------------|
| `topsis.py` | Main command line program |
| `data.csv` | Input data file |
| `output.csv` | Output results file |
| `README.md` | Project documentation |

---

## Notes

- Ensure all weights sum to 1 or are proportional
- The number of weights and impacts must match the number of criteria columns
- Input data must be numeric for proper TOPSIS calculation
