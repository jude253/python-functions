#  this function assumes that the .sql file does not have any syntax errors

def find_table_names_from_sql_file(file_name) -> list:
    s = process_sql_file(file_name)
    table_names = find_table_names(s)
    return table_names


def process_sql_file(file_name) -> str:
    file, s = open(file_name, "r"), ''

    # for line in file, remove comments, space out '(' and ')', add line to output string:
    for line in file:
        line = line.rstrip()
        line = line.split('//')[0]
        line = line.split('--')[0]
        line = line.split('#')[0]
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        s += ' ' + line
    file.close()

    # remove multi-line comments:
    while s.find('/*') > -1 and s.find('*/') > -1:
        l_multi_line, r_multi_line = s.find('/*'), s.find('*/')
        s = s[:l_multi_line] + s[r_multi_line + 2:]

    # remove extra whitespaces
    s = ' '.join(s.split())

    return s


def find_table_names(s) -> list:
    table_names = set()

    # find next closest 'from ' or 'join ', take tablename after it (assuming it isn't '('
    while s.find('from ') > -1 or s.find('join ') > -1:
        # find next closest 'from ' or 'join ' index
        next_from_index, next_join_index = float('inf'), float('inf')
        if s.find('from ') > -1:
            next_from_index = s.find('from ')
        if s.find('join ') > -1:
            next_join_index = s.find('join ')
        next_keyword_index = min(next_from_index, next_join_index)

        # set remaining string to be slice starting after next 'from ' or 'join ':
        s = s[next_keyword_index + 5:]

        # find index of next whitespace in remaining string:
        next_space_index = s.find(' ')

        # save table_name as slice from start of remaining string until next whitespace
        table_name = s[:next_space_index]

        # set remaining string as slice starting after end of table_name
        s = s[next_space_index:]

        # if the table_name isn't the start of a subquery, save it to the output list, table_names
        if table_name != '(':
            table_names.add(table_name)

    return list(sorted(table_names))

