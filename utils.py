from google.cloud import bigquery


def stream_insert_rows_to_bq(client: bigquery.client.Client, table: str, rows: list) -> list:
	"""
	Inserts rows into BigQuery

	Parameters
	----------
	client : google.cloud.bigquery.client.Client
		BigQuery Client

	table_id : str
		if of the table {dataset}.{tablename} e.g. stocks.quotes

	rows : list of dicts
		List of dictionaries to insert into table

	Returns
	-------
	List of Errors (if any).
	"""
	errors = client.insert_rows(table, rows)

	if not all(x==[] for x in errors):
		print('Error: Not all rows inserted...')

	return errors


