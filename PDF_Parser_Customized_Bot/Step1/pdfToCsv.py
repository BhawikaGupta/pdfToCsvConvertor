#!/usr/bin/env python
# coding: utf-8

import tabula
import pandas as pd
import sys

def convertPdfToExcel(fileLocation):
    df = tabula.read_pdf(fileLocation, stream="True",pages='1')
    df = df[0].fillna('')
    df['2016.1'], df['Particulars.1'] = df['2016 Particulars'].str.split(" ",1).str
    df.drop(['Unnamed: 0'], axis = 1)
    df = df[['Particulars', '2015','2016.1','Particulars.1','Unnamed: 1','2015.1','2016']]
    df = df.fillna('')
    df = df.rename(columns={"Unnamed: 1": "", "2016.1": "2016", "2015.1":"2015", "Particulars.1":"Particulars"})
    csvLocation = fileLocation.replace(".pdf",".csv")
    df.to_csv (csvLocation, index = False, header=True)

if __name__ == '__main__':

    fileLocation = sys.argv[1]
    convertPdfToExcel(fileLocation)
