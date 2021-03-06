import xlrd
import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def myFunc(x, a, b, c):
    return (a * (b ** (x - 1995)) + c)


def strmyFunc(a,b,c):
    eq = '(' + str(a) + '*(' + str(b) + ')^T-1995) +' + str(c)
    return eq


def dataex(file, sheetno, ynum):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(sheetno)
    x = []
    y = []
    for i in range(16, 36):
        cell_val1 = worksheet.cell(i, 0).value
        cell_val2 = worksheet.cell(i, ynum).value
        x.append(cell_val1)
        y.append(cell_val2)

    return x, y


def plotgt(nf,num, fno, ini, label, colour, xlable, ylable, title):
    plt.figure(nf)
    plt.subplot(fno)

    xdataIN, ydataIN = dataex('G:/MUN/amogh/project/GDP.xlsx', 0, num[0])
    ydataIN = np.array(ydataIN)
    xdataIN = np.array(xdataIN)
    print(xdataIN)
    print(ydataIN)
    plt.plot(xdataIN, ydataIN, colour[0] + '--', label=label[0])
    popt, pcov = curve_fit(myFunc, xdataIN, ydataIN, (ydataIN[0], ini[0], 0))
    print(popt)
    print(pcov)
    print(label[0] + title + strmyFunc(popt[0], popt[1], popt[2]))
    plt.plot(xdataIN, myFunc(xdataIN, popt[0], popt[1], popt[2]), colour[0]+'-')

    xdataSW, ydataSW = dataex('G:/MUN/amogh/project/GDP.xlsx', 0, num[1])
    ydataSW = np.array(ydataSW)
    xdataSW = np.array(xdataSW)
    print(xdataSW)
    print(ydataSW)
    plt.plot(xdataSW, ydataSW, colour[1] + '--', label=label[1])
    popt, pcov = curve_fit(myFunc, xdataSW, ydataSW, (ydataSW[0],ini[1], 0))
    print(popt)
    print(pcov)
    print(label[1] + title + strmyFunc(popt[0], popt[1], popt[2]))
    plt.plot(xdataSW, myFunc(xdataSW, popt[0], popt[1], popt[2]), colour[1]+'-')

    xdataUS, ydataUS = dataex('G:/MUN/amogh/project/GDP.xlsx', 0, num[2])
    ydataUS = np.array(ydataUS)
    xdataUS = np.array(xdataUS)
    print(xdataUS)
    print(ydataUS)
    plt.plot(xdataUS, ydataUS, colour[2]+'--', label=label[2])
    popt, pcov = curve_fit(myFunc, xdataUS, ydataUS, (ydataUS[0], ini[2], 0))
    print(popt)
    print(pcov)
    print(label[2] + title + strmyFunc(popt[0], popt[1], popt[2]))
    plt.plot(xdataUS, myFunc(xdataUS, popt[0], popt[1], popt[2]), colour[2]+'-')

    xdataBH, ydataBH = dataex('G:/MUN/amogh/project/GDP.xlsx', 0, num[3])
    ydataBH = np.array(ydataBH)
    xdataBH = np.array(xdataBH)
    print(xdataBH)
    print(ydataBH)
    plt.plot(xdataBH, ydataBH, colour[3]+'--', label=label[3])
    popt, pcov = curve_fit(myFunc, xdataBH, ydataBH, (ydataBH[0], ini[3], 0))
    print(popt)
    print(pcov)
    print(label[3] + title + strmyFunc(popt[0], popt[1], popt[2]))
    plt.plot(xdataBH, myFunc(xdataBH, popt[0], popt[1], popt[2]), colour[3]+'-')

    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    plt.legend()


countries = ('INDIA', 'SWEDEN', 'USA', 'BHUTAN')
colours = ('g', 'r', 'b', 'y')


gdp = (1, 7, 13, 19)
ini1 = (1, 1, 0.1, 1)
plotgt(1,gdp, 111, ini1, countries, colours, 'Years', 'GDP', 'GDP OF COUNTRIES')

co = (2, 8, 14, 20)
ini2 = (1, 2, 2, 1)
plotgt(2,co, 111, ini2, countries, colours, 'Years', 'CO2 EMISSION', 'CO2 EMISSION')

naturaldep = (3, 9, 15, 21)
ini3 = (0.1, 2, 2, 1)
plotgt(3,naturaldep, 111, ini3, countries, colours, 'Years', 'NATURAL DEPLETION', 'NATURAL DEPLETION')

agri = (4, 10, 16, 22)
ini4 = (1, 1, 2, 1)
plotgt(4,agri, 111, ini4, countries, colours, 'Years', 'AGRICULTURE ADDED', 'AGRICULTURE ADDED')

health = (5, 11, 17, 23)
ini5 = (1, 1, 2, 1)
plotgt(5,health, 111, ini5, countries, colours, 'Years', 'HEALTH', 'HEALTH')


plt.tight_layout()
plt.show()
