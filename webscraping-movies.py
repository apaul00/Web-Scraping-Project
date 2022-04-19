from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


# webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = "https://www.boxofficemojo.com/year/2022/"

page = urlopen(webpage)

soup = BeautifulSoup(page, "html.parser")

title = soup.title

print(title.text)
##
##
##
##
movie_table = soup.find("table")
# print(movie_table)

movie_rows = movie_table.findAll("tr")
# print(movie_rows[1])

for x in range(1, 6):
    td = movie_rows[x].findAll("td")
    ranking = td[0].text
    title = td[1].text
    release_date = td[3].text
    gross = td[5].text
    total_gross = td[7].text

    # print(gross)
    # input()

wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "Box Office Report"

# write headings
MySheet["A1"] = "No."
MySheet["A1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["A"].width = 5
MySheet["B1"] = "Movie Title"
MySheet["B1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["B"].width = 30
MySheet["C1"] = "Release Date"
MySheet["C1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["C"].width = 25
MySheet["D1"] = "Gross"
MySheet["D1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["D"].width = 16
MySheet["E1"] = "Total Gross"
MySheet["E1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["E"].width = 20
MySheet["F1"] = "% of Total Gross"
MySheet["F1"].font = Font(size=16, bold=True)
MySheet.column_dimensions["F"].width = 26


for x in range(1, 6):
    td = movie_rows[x].findAll("td")
    ranking = td[0].text
    title = td[1].text
    gross = int(td[5].text.replace(",", "").replace("$", ""))
    total_gross = int(td[7].text.replace(",", "").replace("$", ""))

    percent_gross = round((gross / total_gross) * 100, 2)

    MySheet["A" + str(x + 1)] = ranking
    MySheet["B" + str(x + 1)] = title
    MySheet["C" + str(x + 1)] = release_date
    MySheet["D" + str(x + 1)] = gross
    MySheet["E" + str(x + 1)] = total_gross
    MySheet["F" + str(x + 1)] = str(percent_gross) + "%"
wb.save("BoxOfficeReport.xlsx")
