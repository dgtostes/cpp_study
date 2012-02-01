#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
import datetime

def process_date(date_string):
	'''
	recieves a date string in this format mm/dd/yyyy
	and return a datetime.date object
	'''
	if '-' in date_string:
		date_string = date_string.replace('-','/')
	date_list = date_string.split("/")
	day = int(date_list[1])
	month = int(date_list[0])
	year = int(date_list[2])
	return datetime.date(year,month,day)

def process_history(history_string):
	history_string = history_string+"-"
	history_list = history_string.split("-")
	return history_list[0].strip()

def procces_line(line):
	line = line.replace('"', '')
	line_list = line.split(",")
	dic_line = {}
	if line_list[2] == 'S A L D O' or \
		line_list[2] == 'Saldo Anterior' or \
	    line_list[0] == 'Data':
			return None
	else:
		try:
			dic_line['date'] = process_date(line_list[0])
		except:
			dic_line['date'] = None
			
		try:
			dic_line['origin'] = line_list[1]
		except:
			dic_line['origin'] = None
			
		try:
			dic_line['history'] = process_history(line_list[2])
		except:
			dic_line['history'] = None
			
		try:
			dic_line['hist_detail'] = line_list[2]
		except:
			dic_line['hist_detail'] = None
			
		try:
			dic_line['doc_number'] = line_list[4]
		except:
			dic_line['doc_number'] = None
			
		try:
			dic_line['value'] = float(line_list[5])
		except:
			dic_line['value'] = None
			
		dic_line['line'] = line
		
			
			
	return dic_line

def generate_info_list(data_source):
	f = open(data_source, 'r')
	i = f.readline()
	list_info = []
	while i:
		dic_line = procces_line(i)
		if dic_line:
			list_info.append(dic_line)
		i = f.readline()
	return list_info
		
if __name__ == "__main__":
	#print process_date("12/01/2011")
    #transact_list = generate_info_list("extrato20120131-1520.csv")
    #for  trans in transact_list:
		#try:
			#print "%s - %s - R$ %.2f" % (trans['date'].strftime('%d/%m/%Y'),
										#trans['history'],
										#trans['value'])
		#except:
			#pass
	pass

