import re
log_lines = []
output = []

file_name = 'PU1203_C.TXT'
#with open(file_name, 'r') as f: #encoding = 'Big5'
with open(file_name,'r', encoding = 'Big5') as f:
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
    #print(log_lines)

new_log_list = log_lines[::-1]
value = None
cnt = 0
new = []

for line in new_log_list: #時間倒序確認
    print(line)

for line in new_log_list:
    log_time = line[0]
    log_event = line[1]
    log_ID = line[3]
    st_amt = line[5]

    if log_event =='PRO':
        cnt = 0
            #print('磨耗量為: '+ str(value))
            #print('時間= '+ log_time + ' PRO= '+log_ID)
    else:
        cnt += 1
        if cnt ==1 and log_event =='ST1':
            first_line = st_amt
        else:
            new.append(st_amt)
            last_line = new[-1]
            value = int(first_line)-int(last_line)
    if cnt == 0:
        result_output = '磨耗量為: '+ str(value)
        print(result_output) #結果輸出
        output.append(result_output)
        result_output = '時間= '+ log_time + ' PRO= '+log_ID
        print(result_output) #結果輸出
        output.append(result_output)

with open('output.txt','w') as fout:
    for line in output:
        fout.write(line + '\n')
