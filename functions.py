def process_sql_file(file_name):
    file, string = open(file_name, "r"), ''

    # for line in file, remove comments, space out '(' and ')', add line to output string:
    for line in file:
        line = line.rstrip()
        line = line.split('//')[0]
        line = line.split('--')[0]
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        string += ' ' + line
    file.close()

    # remove multi-line comments:
    while string.find('/*') > -1 and string.find('*/') > -1:
        l_multi_line = string.find('/*')
        r_multi_line = string.find('*/')
        string = string[:l_multi_line] + string[r_multi_line + 2:]

    string = string.lower()
    
    # remove extra whitespaces and make list
    words = string.split()

    return words


def find_table_names(words, rm_cte=False):
    table_names = set()
    previous_word = ''
    ctes = set()

    for word in words:
        if rm_cte and word == 'as':
            ctes.add(previous_word)

        if previous_word == 'from' or previous_word == 'join':
            if word != '(':
                if rm_cte and word not in ctes:
                    table_names.add(word)
                if not rm_cte:
                    table_names.add(word)

        previous_word = word

    return sorted(list(table_names))


#  this function assumes that the .sql file does not have any syntax errors:
def find_table_names_from_sql_file(file_name, rm_cte=False):
    words = process_sql_file(file_name)
    return find_table_names(words, rm_cte=rm_cte)
