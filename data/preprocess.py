import pandas as pd

def fill_empty_cells_with_zero(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Fill NaN (empty) values with 0
    df.fillna(0, inplace=True)

    # Save the updated dataframe back to CSV
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

# Example usage
fill_empty_cells_with_zero('global-data-on-sustainable-energy.csv', 'global-data-on-sustainable-energy.csv')
