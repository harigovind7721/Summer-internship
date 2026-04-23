import csv

try:
    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        with open("sales_summary.csv", "w", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["month", "amount", "category"])

            for row in reader:
                try:
                    month = row[0]
                    amount = int(row[1])

                    if amount < 0:
                        raise ValueError("Negative value")

                    if amount >= 80000:
                        category = "High"
                    elif amount >= 50000:
                        category = "Medium"
                    else:
                        category = "Low"

                    writer.writerow([month, amount, category])

                except ValueError:
                    continue

except FileNotFoundError:
    print("File not found")