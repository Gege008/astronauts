def reader():
    months = []
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        forrasfajl.readline()
        while True:
            sor = forrasfajl.readline().strip("\n")
            if sor == "":
                break
            date = sor.split(",")[-1]
            month = date.split("/")[0]
            months.append(month)
    return months


def counter(month):
    result = {}
    for m in month:
        if m in result:
            result[m] += 1
        else:
            result[m] = 1
    return result


def order(result):
    return list(sorted(result.items(), key=lambda item: item[1]))


def writer(ordered_result, num):
    for i in range(3):
        item = ordered_result[11 - i]
        print(f"Hónap: {item[0]} - százalékos arány: {round(100 * item[1] / num, 1)}")


def main():
    month = reader()
    result = counter(month)
    ordered_result = order(result)
    writer(ordered_result, len(month))


main()
