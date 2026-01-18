# TOPSIS Implementation - Avneet Sandhu (102303289)

**Name:** Avneet Sandhu  
**Roll No:** 102303289  
**Course:** Predictive Analytics  
**Group:** 3C22

---

## What is TOPSIS?

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) is a Multi-Criteria Decision Making (MCDM) method that helps in ranking alternatives based on their similarity to the ideal best solution and distance from the ideal worst solution.

### Key Concept:
- The best alternative should have the **shortest distance** from the ideal best solution
- The best alternative should have the **farthest distance** from the ideal worst solution

---

## Project Overview

This project contains:
1. **Python Package** - Command-line tool for TOPSIS calculation
2. **Jupyter Notebook** - Detailed implementation with step-by-step explanation
3. **Sample Dataset** - Mobile phone comparison data

---

## Repository Structure

```
├── topsis.py                                    # Main Python implementation
├── TOPSIS_Assignment_Avneet_102303289.ipynb    # Jupyter notebook with detailed steps
├── data.csv                                     # Input dataset
├── output.csv                                   # Results after TOPSIS
├── Topsis-Avneet-102303289.zip                 # Package distribution
└── README.md                                    # Documentation
```

---

## Methodology

### Workflow Diagram

```
Data Collection → Data Pre-Processing → Weight Assignment → TOPSIS Calculation → Ranking → Result Analysis
```

### TOPSIS Steps:

1. **Normalization**: Convert decision matrix to normalized form using vector normalization
2. **Weighted Normalization**: Multiply normalized values by their respective weights
3. **Ideal Solutions**: 
   - Ideal Best (A⁺): Best values for each criterion
   - Ideal Worst (A⁻): Worst values for each criterion
4. **Distance Calculation**: 
   - Calculate Euclidean distance from Ideal Best (S⁺)
   - Calculate Euclidean distance from Ideal Worst (S⁻)
5. **Performance Score**: 
   ```
   TOPSIS Score = S⁻ / (S⁺ + S⁻)
   ```
6. **Ranking**: Rank alternatives in descending order of TOPSIS score

---

## Jupyter Notebook Implementation

For a **detailed step-by-step implementation** with visualizations and explanations, refer to:

**[TOPSIS_Assignment_Avneet_102303289.ipynb](./TOPSIS_Assignment_Avneet_102303289.ipynb)**

The notebook includes:
- Data loading and preprocessing
- Mathematical formulas for each step
- Visualization of results
- Detailed explanation of the TOPSIS algorithm

---

## Command Line Tool Usage

### Installation from PyPI

The package is available on PyPI and can be installed using pip:

```bash
pip install Topsis-Avneet-102303289
```

### Usage

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example Command

```bash
topsis data.csv 0.2,0.2,0.2,0.2,0.2 -,+,+,+,+ output.csv
```

**Arguments:**
- `InputDataFile`: CSV file containing the decision matrix
- `Weights`: Comma-separated weights for each criterion
- `Impacts`: Comma-separated impacts (`+` for beneficial, `-` for non-beneficial)
- `ResultFileName`: Output CSV file name

---

## Sample Dataset

### Input: `data.csv`

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|------|------|-----|------|-------|
| M1        | 0.88 | 0.77 | 3.3 | 49.9 | 13.71 |
| M2        | 0.61 | 0.37 | 4.1 | 63.8 | 17.22 |
| M3        | 0.68 | 0.46 | 5.8 | 55.7 | 15.66 |
| M4        | 0.65 | 0.42 | 3.5 | 34.7 | 9.82  |
| M5        | 0.93 | 0.86 | 5.0 | 55.3 | 15.52 |
| M6        | 0.91 | 0.83 | 3.2 | 50.6 | 13.89 |
| M7        | 0.91 | 0.83 | 4.6 | 64.3 | 17.66 |
| M8        | 0.92 | 0.85 | 5.3 | 36.5 | 10.89 |

**Weights:** `0.2, 0.2, 0.2, 0.2, 0.2` (Equal importance)  
**Impacts:** `-,+,+,+,+` (P1 is non-beneficial, P2-P5 are beneficial)

---

## 📈 Results

### Output: `output.csv`

| Fund Name | P1   | P2   | P3  | P4   | P5    | Topsis Score | Rank |
|-----------|------|------|-----|------|-------|--------------|------|
| M7        | 0.91 | 0.83 | 4.6 | 64.3 | 17.66 | 0.700458     | 1    |
| M5        | 0.93 | 0.86 | 5.0 | 55.3 | 15.52 | 0.668589     | 2    |
| M3        | 0.68 | 0.46 | 5.8 | 55.7 | 15.66 | 0.588975     | 3    |
| M2        | 0.61 | 0.37 | 4.1 | 63.8 | 17.22 | 0.522999     | 4    |
| M8        | 0.92 | 0.85 | 5.3 | 36.5 | 10.89 | 0.507755     | 5    |
| M6        | 0.91 | 0.83 | 3.2 | 50.6 | 13.89 | 0.497090     | 6    |
| M1        | 0.88 | 0.77 | 3.3 | 49.9 | 13.71 | 0.475101     | 7    |
| M4        | 0.65 | 0.42 | 3.5 | 34.7 | 9.82  | 0.239258     | 8    |

### Result Summary
- **Best Alternative:** M7 (Score: 0.700458)
- **Worst Alternative:** M4 (Score: 0.239258)

---

## Input File Requirements

- ✓ File must be in **CSV format**
- ✓ First column contains object/alternative names
- ✓ Minimum **3 columns** (1 for names + 2 or more criteria)
- ✓ All criterion values must be **numeric**
- ✓ **No missing values** allowed
- ✓ At least **2 rows** of data

---

## Error Handling

The package includes comprehensive validation:

| Validation | Description |
|------------|-------------|
| Argument Count | Checks for correct number of parameters |
| File Existence | Validates input file exists |
| CSV Format | Ensures proper CSV structure |
| Minimum Columns | Validates at least 3 columns present |
| Numeric Data | Checks all criterion values are numbers |
| Weights Validation | Ensures weights match number of criteria |
| Impacts Validation | Verifies impacts are `+` or `-` only |
| Length Match | Confirms weights and impacts count matches |

---

## Links

### PyPI Package
**Install from:** [https://pypi.org/project/Topsis-Avneet-102303289/](https://pypi.org/project/Topsis-Avneet-102303289/)
