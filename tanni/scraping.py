from django.shortcuts import render
from urllib import request
from bs4 import BeautifulSoup
import re
import regex

def Time_Scraping ( ):
	# url
	url = "http://timetable.sic.shibaura-it.ac.jp/table/2020/Timetable1L0113.html"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	weeks = [ "mon", "tue", "wed", "thu", "fri", "sat", "oth" ]

	for week in weeks:
		print ( "\n" + week + "\n" )
		#get ClassInfo
		temp = soup.find_all ( "table", id = week )
		for time in range ( 0, 6 ):
			# 1限 ( row = 0 )
			print ( "\n" )
			print ( time + 1, end = "" )
			print ( "限\n" )
			for i in temp:
				for k in i.find_all ( "td", row = time ):
					for j in k.find_all ( "a", target = "_blank" ):
						print ( j.string, "\n" )

def Syllabus_Scraping ( ):
	#url
	url = "http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01131.html.ja"
	#get html
	html = request.urlopen ( url )
	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	#get ClassInfo
	# Subjects = soup.find_all ( "tr", attrs = { "class", "subject" } )

	Subjects = soup.find_all ( "tbody" )

	kind_tanni = { "◎":"必修", "○":"選択必修", "△":"選択", "□":"自由", "☆":"必須認定" }

	for i in Subjects:
		for j in i.find_all ( "tr", attrs = { "class", "subject" } ):
			print ( "授業名 : ", j.contents[3].string )
			# print ( j.contents[9].string )
			# for k in range ( 6, 14 ):
			# 	if j.contents[k].string is not None:
			# 		print ( k )
			# 		print ( j.contents[k].string )

			print ( "必修状況 : " )
			for k in range ( 6, 14 ):
				if j.contents[k].string is not None:
					# print ( k )
					print ( j.contents[k].string )
			for l in j.find_all ( colspan = "2" ):
				if ( "◎" ) in l:
					if l.text is not "None":
						print ( l.text )
				if ( "△" ) in l:
					if l.text is not "None":
						print ( l.text )
					
			if j.contents[6].string is not "None":
				print ( j.contents[6].string )
				print ( "コマ数 : ", j.contents[15].string )
				print ( "単位数 : ", j.contents[5].string, "\n" )

			# for k in j.find_all ( colspan = "2" ):
			# 	if "◎" in k:
			# 		print ( k.text )
			
			# for k in range ( 0, 20 ):
			# 	for l in kind_tanni:
			# 		if ( j.contents[k] == l):
			# 			print ( l )
	
	#print ClassInfo
	# for subject in Subjects:
	# 	subject.td.decompose ( ) # tdタグを除去
	# 	print ( "講義名 : ", end = '' )
	# 	print ( subject.contents[0], subject.td.string )
	# 	subject.td.decompose ( ) # tdタグを除去
	# 	print ( "単位数 : ", end = '' )
	# 	print ( subject.contents[1], subject.td.string, "\n" )

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


if __name__ == "__main__":
	#Time_Scraping ( )
	Syllabus_Scraping ( )
