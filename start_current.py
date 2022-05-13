import csv
import time
import re
import os
import relaycomtradelib

text1 = '''
Set path to your oscillograms and Enter. Or just press Enter, then programm wiil seek oscillograms in same folder
'''
print(text1)
inp_path = input('')

text2 = '''
Set your output folder oscillograms with start currents and Enter. If just Enter there is will not output files, just report.csv
'''
print(text2)
inp_out = input('')

path_files = []
result_list = []

def write_to_csv(data, path):
    with open(path, 'wt') as fp:
    # Uncomment, if will be problems with encoding in Windows
    # with open(path, 'wt', newline='',encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=";")
        writer.writerows(data)
    return

path_list = []

root_folder = inp_path if inp_path else "."

for root, dirs, files in os.walk(root_folder, topdown=False):
    for name in files:
        path_list.append(os.path.join(root, name))

trig = 0
average_prev = 0
average_next = 0
path_result = []

for j, path in enumerate(path_list):
    if re.findall('\.cfg', path):
        cfg_file = path
        dat_file = path[:len(path)-4] + '.dat'
        data = relaycomtradelib.comtrade(cfg_file, dat_file, '')
        data_lenth = len(data)


        for i, item in enumerate(data):
            if i<3:
                continue
            if i < (data_lenth-5):
                average_prev =  ( abs( float(data[i-2][2]) ) + abs( float(data[i-1][2]) ) +   abs( float(data[i][2]) ) )/3
                average_next =  ( abs( float(data[i+3][2]) ) + abs( float(data[i+2][2]) ) + abs( float(data[i+1][2]) ) )/3

                if average_next > (average_prev * 5) and average_prev < 15 and average_next >= 25:
                    path_result.append([cfg_file])
                    path_result.append([dat_file])
                    break
    if (j % 10 == 0):
        print('Completed', j, 'items and found', len(path_result), 'CFG, DAT files')

if path_result:
    print('It was found files!')
    time.sleep(1)

    for i in path_result:
        print(*i)

    write_to_csv(path_result, 'report.csv')

    if inp_out:
        os.system('mkdir ' + inp_out)
        for item in path_result:
            os.system('cp ' + '"' + item[0] + '"' + ' --parents ' + inp_out)
    
else:
    print('Files with start currents not found')

print('It is done!')