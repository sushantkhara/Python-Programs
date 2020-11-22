"""
                    1
                1       1
            1       2       1
        1       3       3       3
    1       4       6       4       1
1       5       10      10      5       1

"""
numberOfRows = 7


def format_number(number):
  if number<10:
    return "  "+str(number) + " "
  else:
    return " " + str(number) + " "


row = [1]
print("  " * 7 + format_number(row[0]))
row.append(1)
print("  " * 6 + format_number(row[0]) + format_number(row[1]))
row.append(2)
print("  " * 5 + format_number(row[0]) + format_number(row[1]+row[0]) + format_number(row[1]))
row.append(3)
print("  " * 4 + format_number(row[0]) + format_number(row[3]) +format_number(row[3]) + format_number(row[1]))
row.append(4)
print("  " * 3 + format_number(row[0]) + format_number(row[4]) + format_number(row[4]+row[2]) +format_number(row[4]) +
      format_number(row[1]))
row.append(5)
print("  " * 2 + format_number(row[0]) + format_number(row[5]) + format_number(row[5]+row[5]) + format_number(row[5]
                        + row[5]) + format_number(row[5]) + format_number(row[1]))
row.append(6)


