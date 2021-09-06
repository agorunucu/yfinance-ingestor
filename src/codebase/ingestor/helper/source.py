import pandas as pd


def get_ticker_names():
    print(pd.read_csv("gs://bux-bi-assignment-agorunucu/de_assignment_product_list.txt", delimiter="|"))
