

def read_file(filename):
    with open(filename) as text_file:
        lines = text_file.readlines()
    
    return lines



def read_file(filename):
    lines = []
    with open(filename) as text_file:
        for line in text_file:
            lines.append(line)
    
    return lines
