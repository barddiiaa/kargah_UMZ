def interpret_statement(statement, suspect_truth):
    if isinstance(statement, bool):
        return statement
    if 'not' in statement:
        mentioned_suspect = statement.split(' ')[1]
        return not suspect_truth[mentioned_suspect]
    return suspect_truth[statement]

def evaluate_suspect(suspect, statements):
    suspect_truth = {s: s == suspect for s in statements}
    
    true_count = 0
    false_count = 0
    for s in statements:
        for statement in statements[s]:
            if interpret_statement(statement, suspect_truth):
                true_count += 1
            else:
                false_count += 1
    return true_count == false_count

def guilty(sus):
    for suspect in sus.keys():
        if evaluate_suspect(suspect, sus):
            print(f'{suspect} is the thief')

sus = {
    'a': [False, 'b', True],
    'b': ['not d', 'not a', 'not b'],
    'c': [True, 'not b', True],
    'd': ['d', False, 'a']
}

guilty(sus)