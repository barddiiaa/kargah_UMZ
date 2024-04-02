def solve_puzzles(puzzles):
    with open(puzzles,'r') as file:
           words = file.readlines()
    boolean_list = []
    for word in words:
            word = word.strip()
            if 'true' in word. lower() or 'false' in word. lower():
                  if word.startswith("'"):
                       word = word[1:]
                  if word.endswith("'"):
                       word = word[:-1]


            boolean_list.append(eval(word))
            
            return boolean_list

print(solve_puzzles('puzzles.txt'))
