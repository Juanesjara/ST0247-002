import pandas

f = r"calles_de_medellin_con_acoso.csv"

test = pandas.read_csv(f, sep = ";")

print(test)