import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

def Creating_workbook(data):
    try:
        #creating a virtual workbook:
        wb = openpyxl.Workbook()
        sheet = wb.active

        #We create our data/ your data can get from API
        print(data)

        #We need to add the headers first:
        Column_titles = data[0].keys()
        sheet.append(list(Column_titles))

        #Excel is taking the data as string, forcing the convertion to int:
        for item in data:
            item['Rank'] = int(item['Rank'])

        #Adding the data to the file:
        for item in data:
            sheet.append(list(item.values()))

        max_row = len(data)+1
        #Creating a chart:
        refObj = openpyxl.chart.Reference( sheet, min_col=2, min_row=1,max_col =2, max_row =11)
        categories = openpyxl.chart.Reference( sheet, min_col=1, min_row=2, max_row =11)
        #seriesObj = openpyxl.chart.Series(refObj, title = 'Bitcoin Ranking')


        #Chossing the data
        chartObj = openpyxl.chart.BarChart()
        chartObj.add_data(refObj, titles_from_data=True)
        chartObj.set_categories(categories)
        #chartObj = openpyxl.chart.LineChart()
        #chartObj = openpyxl.chart.PieChart()

        chartObj.title = 'My Chart'
        #chartObj.append(seriesObj)
        sheet.add_chart(chartObj,'C5')
        wb.save('Test.xlsx') #"Excel/samplechart.xlsx"
        print('Done')
        return
    except:
        return