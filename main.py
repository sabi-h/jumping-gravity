import os
import time
from datetime import datetime
from pprint import pprint

import requests
from google.cloud import bigquery

from settings import TOKEN, PROJECT_ID
from symbols import SYMBOLS
from utils import stream_insert_rows_to_bq


BASE_URL = "https://sandbox.iexapis.com/stable"
DATASET = 'stocks'
TABLENAME = 'quotes'


def get_latest_price(symbol: str) -> float:
	url = f"{BASE_URL}/stock/{symbol}/quote/latestPrice?token={TOKEN}"
	response = requests.request("GET", url, headers={}, data={})
	return response.json()


def get_top3_highest_priced_symbols(symbols: list) -> list:
	"""
	Gets the top 3 highest priced symbols.

	Parameters
	----------
	symbols : list of str
		list of stock symbols

	Returns
	-------
	list of str
	"""
	result = [(symbol, get_latest_price(symbol)) for symbol in symbols]
	sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
	return [x[0] for x in sorted_result[:3]]


def main():
	symbols = get_top3_highest_priced_symbols(SYMBOLS)

	client = bigquery.Client(project=PROJECT_ID)
	table = client.get_table(f'{DATASET}.{TABLENAME}')

	while True:

		rows_to_insert = []
		time_now = datetime.now()

		rows = [(symbol, time_now, get_latest_price(symbol)) for symbol in symbols]
		errors = stream_insert_rows_to_bq(client=client, table=table, rows=rows)

		print(f'{time_now}: inserted rows...', f'errors: {errors}', end='\n\n')

		time.sleep(8)


if __name__ == '__main__':
	main()













