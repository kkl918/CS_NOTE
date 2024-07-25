import os
import matplotlib.pyplot as plt
import numpy as np


script_path = os.path.dirname(__file__)

f_in_path   = r'C:\Users\mini\Documents\test.csv'

f_in        = [i.strip() for i in open(f_in_path, 'r').readlines()]

date_row    = f_in[0].split(',')[2:]

NN          = len(f_in)-1

jump_row    = 4


def plot_R9(x, y, std1, std2, std3, chart_title, bar_title1, bar_title2, bar_title3):
    fig, ax = plt.subplots()
    
    ax.errorbar(x, y, yerr=std3, label=bar_title3)
    ax.errorbar(x, y, yerr=std2, label=bar_title2)
    ax.errorbar(x, y, yerr=std1, label=bar_title1)
    ax.set_title(chart_title)
    plt.legend(loc='lower right')
    plt.savefig(os.path.join(script_path, chart_title+'.png'))


for index, row in enumerate(f_in):
    if row.split(',')[1] == 'mean' and index == 1:
        tool_name  = row.split(',')[0]
        chart_name = tool_name+' R9 mean & STD'
        mean_row   = [float(i) for i in f_in[index].split(',')[2:]]
        std_1_row  = [float(i) for i in f_in[index+jump_row].split(',')[2:]]
        std_3_row  = [3*float(i) for i in f_in[index+jump_row].split(',')[2:]]
        std_4_row  = [4*float(i) for i in f_in[index+jump_row].split(',')[2:]]
        std_5_row  = [5*float(i) for i in f_in[index+jump_row].split(',')[2:]]
        std_6_row  = [6*float(i) for i in f_in[index+jump_row].split(',')[2:]]
        # print(mean_row)
        # print(std_3_row)

        plot_R9(date_row, mean_row, std_3_row, std_4_row, std_5_row, chart_name, '3 sigma', '4 sigma', '5 sigma')

x = np.arange(0.1, 4, 0.1)
y = np.exp(-1.0 * x)



plt.show()

