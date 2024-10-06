def main():
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    
    parser.add_argument(
        '-f', '--format', 
        help='set format of output',
        metavar='FORMAT'
    )
    
    args = parser.parse_args()

    with open(args.first_file, 'r') as file1:
        file1_data = json.load(file1)

    with open(args.second_file, 'r') as file2:
        file2_data = json.load(file2)

    # tmp - for testing
    print('Data from the first file:', file1_data)
    print('Data from the secosnd file:', file2_data)

if __name__ == '__main__':
    main()
