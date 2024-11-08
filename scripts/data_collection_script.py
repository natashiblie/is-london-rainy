import argparse
import json
from data_collection_utils import get_historical_data

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Collect historical rainfall data for a specified city and date range.")
    
    # Add arguments
    parser.add_argument("country_code", type=str, help="Country code (e.g., 'SG' for Singapore')")
    parser.add_argument("city_name", type=str, help="City name (e.g., 'Singapore')")
    parser.add_argument("--start_date", type=str, default="2023-01-01", help="Start date in YYYY-MM-DD format (default: '2023-01-01')")
    parser.add_argument("--end_date", type=str, default="2023-12-31", help="End date in YYYY-MM-DD format (default: '2023-12-31')")
    parser.add_argument("--output_file", type=str, default="data/multicity_historical.json", help="Output file path (default: 'data/multicity_historical.json')")

    # Parse arguments
    args = parser.parse_args()

    # Collect the historical data using the provided arguments
    rainfall_data = get_historical_data(args.country_code, args.city_name, start_date=args.start_date, end_date=args.end_date)

    # Save data to JSON file
    with open(args.output_file, "w") as file:
        json.dump(rainfall_data, file)
    
    print(f"Data for {args.city_name}, {args.country_code} saved to {args.output_file}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()