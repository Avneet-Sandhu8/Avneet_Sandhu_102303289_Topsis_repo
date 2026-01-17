# topsis.py
# TOPSIS Assignment – Part I
# Name: Avneet Sandhu
# Roll No: 102303289

import sys
import pandas as pd
import numpy as np


def main():

    # Step 0: Check number of inputs

    if len(sys.argv) != 5:
        print("Usage:")
        print("python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    output_file = sys.argv[4]


    # Step 1: Read file (File not found handling)

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)


    # Step 2: Minimum 3 columns check

    if df.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)


    # Step 3: Numeric check (2nd to last column)

    for col in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"Error: Column {col} must contain numeric values only")
            sys.exit(1)


    # Step 4: Parse weights and impacts

    weights = weights_str.split(",")
    impacts = impacts_str.split(",")

    if len(weights) != len(df.columns) - 1:
        print("Error: Number of weights must be equal to number of criteria")
        sys.exit(1)

    if len(impacts) != len(df.columns) - 1:
        print("Error: Number of impacts must be equal to number of criteria")
        sys.exit(1)

    for i in impacts:
        if i not in ["+", "-"]:
            print("Error: Impacts must be either + or -")
            sys.exit(1)

    weights = np.array(list(map(float, weights)))


    # Step 1 : Convert categorical to numeric

    alternatives = df.iloc[:, 0]
    X = df.iloc[:, 1:]


    # Step 2.1: Vector Normalization

    root_sum_squares = np.sqrt((X ** 2).sum())


    # Step 2.2: Normalized Decision Matrix

    normalized_decision_matrix = X / root_sum_squares


    # Step 3.1 & 3.2: Weight Assignment

    weighted_normalized_decision_matrix = normalized_decision_matrix * weights


    # Step 4: Find Ideal Best and Ideal Worst

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted_normalized_decision_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_normalized_decision_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_normalized_decision_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_normalized_decision_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)


    # Step 5: Euclidean Distance

    S_plus = np.sqrt(((weighted_normalized_decision_matrix - ideal_best) ** 2).sum(axis=1))
    S_minus = np.sqrt(((weighted_normalized_decision_matrix - ideal_worst) ** 2).sum(axis=1))


    # Step 6: Performance Score

    performance_score = S_minus / (S_plus + S_minus)


    # Step 7: TOPSIS Rank

    result = df.copy()
    result["Topsis Score"] = performance_score
    result["Rank"] = performance_score.rank(ascending=False).astype(int)


    # Save output file

    result.to_csv(output_file, index=False)
    print("Result saved successfully in", output_file)


if __name__ == "__main__":
    main()

