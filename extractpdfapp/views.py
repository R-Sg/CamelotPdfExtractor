from django.shortcuts import render
import camelot
from django.http.response import JsonResponse


# PDF file to extract tables from
pdf_file = "/home/developer/Desktop/table.pdf"
csv_file = "/home/developer/Desktop/table.csv"

def extract_pdf(self):
	"""
	Use to read the table from pdf and print in dataframe.
	"""
	try:
		# extract tables in the PDF file
		tables = camelot.read_pdf(pdf_file)
		# print number of tables extracted
		print("Total tables extracted:", tables.n)
		# print the first table as Pandas DataFrame
		print(tables[0].df)
		return JsonResponse({"success":"just see your terminal for result."})
	except Exception as e:
		raise JsonResponse({"fail":e})


def table_to_csv(self):
	"""
	Use to export the table data into csv file.
	"""
	try:
		# extract all the tables in the PDF file
		tables = camelot.read_pdf(pdf_file)
		# export the table to a CSV file
		tables[0].to_csv(csv_file)
		return JsonResponse({"success":"table added successfully into csv."})
	except Exception as e:
		raise JsonResponse({"fail":e})