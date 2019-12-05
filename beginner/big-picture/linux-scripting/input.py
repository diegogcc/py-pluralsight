import json
with open('input.json', 'r') as input:
    obj = json.load(input)
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + '\n')