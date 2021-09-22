import calendar

list_months = []
for x in range(1, 13):
    list_months.append(calendar.month_name[x])

for ele in list_months:
    if ele[0] in ['m',"M"]:
        print(ele)

print(calendar.month_name[1:13])