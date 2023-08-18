import datetime

from csv import writer


async def save_temperature(date: datetime.date, temperature: float):
    with open("../../data/temperature.csv", "a") as csv:
        writer_object = writer(csv)
        writer_object.writerow([date, temperature])
        csv.close()
