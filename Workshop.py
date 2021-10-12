def calculate(operator, num_1, num_2):
    if operator == '+': 
        return int(num_1) + int(num_2)
    if operator ==  '-':
        return int(num_1) - int(num_2)
    if operator ==  'x':
        return int(num_1) * int(num_2)
    if operator ==  '/':
        return float(num_1) / float(num_2)

def calculate_and_print(self, operator, num_1, num_2):
    print(self.calculate(operator, num_1, num_2))

def process_line(line):
    sections = line.split(' ')
    return calculate(sections[1], sections[2], sections[3])

with open("step_3.txt", 'r') as file:
    file_input = file.read().splitlines()



#total = 0
#for line in file_input:
#    total += process_line(line)
#
#print(total)

completed_commands = []
current_line = 0
matched_command = ''

while(matched_command == ''):
    line_to_process = file_input[current_line]
    
    for command in completed_commands:
        if command == line_to_process:
            matched_command = command

    completed_commands.append(line_to_process)

    commands = line_to_process.split(' ')
    if commands[1] == 'calc':
        current_line = int(calculate(commands[2], commands[3], commands[4]))
    else:
        current_line = int(commands[1])

print(line_to_process)
print(current_line)