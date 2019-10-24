import re
import time
log_lines = []

file_name = input('請將LOG檔案放入同一資料夾後，輸入檔名(如:PU1203_C.TXT)')
#file_name = 'PU1203_C.TXT'
#with open(file_name, 'r') as f: #encoding = 'Big5'
with open(file_name,'r', encoding = 'Big5') as f:
#with open(file_name,'r', encoding = 'utf-8') as f:
    for line in f:
        event=re.split('\t|,',line)

        if len(event) < 5:
            continue
        event_1 = event[1]

        if event_1 == 'PRO' or event_1 == 'ST1'or event_1 == 'ST2':
            log_lines.append(event[0:6])

new_log_list = log_lines[::-1]
value1 = None
value2 = None
cnt1 = 0
cnt2 = 0
new_lines1 = None
new_lines2 = None
new_lines3 = None
new1 = []
new2 = []
output = []

#時間倒序確認
#for line in new_log_list:
    #print(line)

for line in new_log_list:
    log_time = line[0]
    log_event = line[1]
    log_ID = line[3]     #產品名稱
    st_amt = line[5]     #刀刃露出量

    if log_event =='PRO':
        cnt =0
        cnt1 = 0
        cnt2 = 0

        #結果印出
        #print('ST1磨耗='+str(value1))
        #print('ST2磨耗='+str(value2))
        #print('時間= '+ log_time + ' PRO= '+log_ID)

        new_line1 = 'ST1磨耗='+str(value1)
        output.append(new_line1)
        new_line2 ='ST2磨耗='+str(value2)
        output.append(new_line2)
        new_line3 = '時間= '+ log_time + ' PRO= '+log_ID
        output.append(new_line3)

    elif log_event == 'ST1':
        cnt1 += 1
        if cnt1 == 1:
            first_line = st_amt
        else:
            new1.append(st_amt)
            last_line = new1[-1]
            value1 = int(first_line)-int(last_line)

    elif log_event == 'ST2':
        cnt2 += 1
        if cnt2 ==1:
            first_line2 = st_amt
        else:
            new2.append(st_amt)
            last_line2 = new2[-1]
            value2 = int(first_line2)-int(last_line2)
print('結果已輸出至"output.txt"檔案')
time.sleep(3)

with open('output.txt','w',encoding = 'utf-8') as fout:
    for line in output:
        fout.write(line + '\n')
