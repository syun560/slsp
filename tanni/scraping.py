from django.shortcuts import render
from urllib import request
from bs4 import BeautifulSoup
import re
import regex

def scraping ( ):
	"""
	#url
	url = "http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01131.html.ja"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	#get ClassInfo
	Subjects = soup.find_all ( "tr", attrs = { "class", "subject" } )
	
	#print ClassInfo
	for subject in Subjects:
		subject.td.decompose ( ) # tdタグを除去
		print ( "講義名 : ", end = '' )
		print ( subject.contents[0], subject.td.string )
		subject.td.decompose ( ) # tdタグを除去
		print ( "単位数 : ", end = '' )
		print ( subject.contents[1], subject.td.string, "\n" )
	"""

	"""
	#url
	url = "http://timetable.sic.shibaura-it.ac.jp/table/2020/Timetable1L0113.html"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	#get ClassInfo
	#Subjects = soup.find_all ( "table", attrs = { "class", "tt" } )
	Subjects = soup.find_all ( "a", target = "_blank" )
	Teachers = soup.find_all ( "td", align = "RIGHT" )
	
	#print ClassInfo
	for _blank in Subjects:
		# tt.a.decompose ( ) # tdタグを除去
		print ( "講義名 : ", end = '' )
		print ( _blank.text )
		subject.td.decompose ( ) # tdタグを除去
		print ( "単位数 : ", end = '' )
		print ( subject.contents[1], subject.td.string, "\n" )

	# moji = regex.compile ( r'\p{Script=Han}+' )

	for RIGHT in Teachers:
		print ( "教員名 : ", end = '' )
		match = re.search ( r'^[\u4E00-\u9FD0]+$', '豊洲' )
		if match:
			print ( RIGHT.text )
			print ( "\n" )
		else:
			print ( "\n" )
		"""

	#url
	url = "http://timetable.sic.shibaura-it.ac.jp/table/2020/Timetable1L0113.html"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	# 月曜日
	print ( "\n月曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "mon" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 火曜日
	print ( "\n火曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "tue" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 水曜日
	print ( "\n水曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "wed" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 木曜日
	print ( "\n木曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "thu" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 金曜日
	print ( "\n金曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "fri" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 土曜日
	print ( "\n土曜日\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "sat" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# その他
	print ( "\nその他\n" )
	#get ClassInfo
	temp = soup.find_all ( "table", id = "oth" )

	# 1限 ( row = 0 )
	print ( "\n1限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "0" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 2限 ( row = 1 )
	print ( "\n2限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "1" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 3限 ( row = 2 )
	print ( "\n3限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "2" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 4限 ( row = 3 )
	print ( "\n4限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "3" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 5限 ( row = 4 )
	print ( "\n5限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "4" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )

	# 6限 ( row = 5 )
	print ( "\n6限\n" )
	for i in temp:
		for k in i.find_all ( "td", row = "5" ):
			for j in k.find_all ( "a", target = "_blank" ):
				print ( j.string, "\n" )



if __name__ == "__main__":
	scraping ( )
