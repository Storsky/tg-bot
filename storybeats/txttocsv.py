import csv

new_dict = {}
counter = 0
storybeat = ''
with open('Harry.txt', 'r', encoding="utf8") as text:
    stripped = (line.strip() for line in text)
    for line in stripped:
        if line == '':
            continue
        else:
            words=line.split(' ')
            if words[0] == 'Page' or words[0] == 'Go' and words[1] == 'to':
                if storybeat != '':
                    new_dict[counter] = {name: storybeat}
                    counter+=1
                    storybeat = ''
                name = line
                
            else:
                storybeat += line + ''



with open('log.csv', 'w', encoding='utf8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('id', 'name', 'thread'))
    for dict_item in new_dict:
        for item in new_dict[dict_item]:
            writer.writerow((dict_item, item, new_dict[dict_item][item]))


           
            
            