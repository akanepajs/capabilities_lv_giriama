import pandas as pd

def extract_csv_subset(input_file, output_file, start_row, num_rows):
    """
    Extract a subset of rows from a CSV file and save to a new file.
    
    Parameters:
    - input_file: Path to the original CSV file
    - output_file: Path to save the extracted subset
    - start_row: The row number to start extracting from (0-indexed)
    - num_rows: Number of rows to extract
    """
    # Read the CSV file
    df = pd.read_csv('/content/mmlu_shuffled_all.csv')
    
    # Extract the specified subset of rows
    subset = df.iloc[start_row:start_row + num_rows]
    
    # Save the subset to a new CSV file
    subset.to_csv(output_file, index=False)
    
    print(f"Extracted {num_rows} rows starting from row {start_row}")
    print(f"Saved to {output_file}")

# Example usage
input_file = 'mmlu_shuffled_all.csv'  # Replace with your actual input file name
output_file = 'mmlu_shuffled_113-500.csv'

extract_csv_subset(input_file, output_file, start_row=112, num_rows=388)
