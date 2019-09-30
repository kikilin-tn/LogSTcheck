import re
log_lines=[]

with open('STinput.txt', 'r') as f:
    for line in f:
        event=re.split('\t|,',line)

        if len(event) < 5:
            continue
        #print(event)
        event_1 = event[1]
        #print(event_1)
        if event_1 == 'PRO' or event_1 == 'ST1':
            #print(event)
            log_lines.append(event[0:6])
    print(log_lines)

#print ("'ST1'" in log_lines)