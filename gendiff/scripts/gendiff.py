from gendiff.parser import parse


def generate_diff(file_path1, file_path2):
    file1_data = parse(file_path1)
    file2_data = parse(file_path2)

    differences = {}
    all_keys = sorted(file1_data.keys() | file2_data.keys())
    for key in all_keys:
        if key in file1_data and key in file2_data:
            if file1_data[key] != file2_data[key]:
                differences[key] = (
                    'changed', file1_data[key], file2_data[key])
            else:
                differences[key] = ('same', file1_data[key])
        elif key in file1_data:
            differences[key] = ('removed', file1_data[key])
        else:
            differences[key] = ('added', file2_data[key])
    return format_diff(differences)


def format_diff(differences):
    result = []
    for key, value in differences.items():
        if value[0] == 'removed':
            result.append(f"  - {key}: {value[1]}")
        elif value[0] == 'added':
            result.append(f"  + {key}: {value[1]}")
        elif value[0] == 'changed':
            result.append(f"  - {key}: {value[1]}")
            result.append(f"  + {key}: {value[2]}")
        elif value[0] == 'same':
            result.append(f"    {key}: {value[1]}")
    return "{\n" + "\n".join(result) + "\n}"


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        metavar='FORMAT'
    )
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()
