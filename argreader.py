import argparse


def main():
    parser = argparse.ArgumentParser(description='''
    Finds table names in .sql file(s). Must provide either .sql file paths or use -d, but not both
    ''')

    # Optional positional argument
    parser.add_argument('file_paths', type=str, nargs='*', default=False,
                        help='Used to pass in name argument')

    # Optional boolean argument
    parser.add_argument('-d', '--dialer', action='store_true',
                        help='Option runs script on all dialer .sql files')

    args = parser.parse_args()

    if args.file_paths is False and args.dialer is False:
        print('usage: cmd.py [-h] [-d] [file_paths [file_paths ...]]')
        print('cmd.py: error: either file_paths or option -d required')
    elif type(args.file_paths) == list and args.dialer is True:
        print('usage: cmd.py [-h] [-d] [file_paths [file_paths ...]]')
        print('cmd.py: error: may only specify file_paths or option -d, but not both')
    elif args.dialer:
        print(['/path/to/file1.sql', '/path/to/file2.sql', '/path/to/file3.sql'])
    else:
        for file_path in args.file_paths:
            print(file_path)


if __name__ == '__main__':
    main()
