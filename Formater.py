# Import necessary libraries
import csv          # For handling CSV file operations
import json         # For handling JSON file operations
import xml.etree.ElementTree as ET  # For handling XML file operations
import sys          # For accessing command-line arguments

def convert_to_csv(input_file, output_file):
    """
    Convert a tab-delimited file to CSV format
    
    Args:
        input_file: Path to the input tab-delimited file
        output_file: Path where the CSV output will be saved
    """
    # Open input file with latin-1 encoding to handle special characters
    # Open output file with utf-8 encoding for standard compatibility
    with open(input_file, 'r', encoding='latin-1', errors='replace') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        # Create a CSV reader that uses tabs as delimiters
        reader = csv.reader(infile, delimiter='\t')
        # Create a CSV writer with default comma delimiter
        writer = csv.writer(outfile)
        # Iterate through each row in the input file and write to output
        for row in reader:
            writer.writerow(row)

def convert_to_json(input_file, output_file):
    """
    Convert a tab-delimited file to JSON format
    
    Args:
        input_file: Path to the input tab-delimited file
        output_file: Path where the JSON output will be saved
    """
    # Open input file with latin-1 encoding to handle special characters
    with open(input_file, 'r', encoding='latin-1', errors='replace') as infile:
        # Create a CSV DictReader that uses tabs as delimiters
        # This automatically uses the first row as field names
        reader = csv.DictReader(infile, delimiter='\t')
        # Convert all rows to a list of dictionaries
        data = [row for row in reader]
    
    # Write the data to a JSON file with pretty formatting (indent=4)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)

def convert_to_xml(input_file, output_file):
    """
    Convert a tab-delimited file to XML format
    
    Args:
        input_file: Path to the input tab-delimited file
        output_file: Path where the XML output will be saved
    """
    # Open input file with latin-1 encoding to handle special characters
    with open(input_file, 'r', encoding='latin-1', errors='replace') as infile:
        # Create a CSV DictReader that uses tabs as delimiters
        reader = csv.DictReader(infile, delimiter='\t')
        
        # Create the root XML element
        root = ET.Element("root")
        
        # For each row in the CSV, create an item element with child elements for each field
        for row in reader:
            # Create an item element for this row
            item = ET.SubElement(root, "item")
            
            # Add each field as a child element of the item
            for key, value in row.items():
                child = ET.SubElement(item, key)
                child.text = value
        
        # Create an ElementTree from the root element
        tree = ET.ElementTree(root)
        
        # Write the XML tree to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            tree.write(output_file, encoding='utf-8')

def main():
    """
    Main function that processes command-line arguments and calls the appropriate conversion function
    """
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <-c|-j|-x>")
        sys.exit(1)

    # Get the input file and format flag from command-line arguments
    input_file = sys.argv[1]
    format_flag = sys.argv[2]

    # Determine which conversion function to call based on the format flag
    if format_flag == "-c":
        output_file = "output.csv"
        convert_to_csv(input_file, output_file)
    elif format_flag == "-j":
        output_file = "output.json"
        convert_to_json(input_file, output_file)
    elif format_flag == "-x":
        output_file = "output.xml"
        convert_to_xml(input_file, output_file)
    else:
        # If an invalid flag was provided, show an error message
        print("Invalid format flag. Use -c for CSV, -j for JSON, or -x for XML.")
        sys.exit(1)
    
    # Inform the user that the conversion is complete
    print(f"Conversion complete. Output saved to {output_file}")

# This block ensures that the main() function is only called when the script is run directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
