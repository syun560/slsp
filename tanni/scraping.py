from django.shortcuts import render
from urllib import request
from bs4 import BeautifulSoup

def scraping ( ):
	#url
	url = "http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01131.html.ja"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	#get ClassInfo
	Subjects = soup.find_all ( "tr", attrs = { "class", "subject" } )

	print ( "専門科目\n" )
	
	#print ClassInfo
	for subject in Subjects:
		subject.td.decompose ( ) # tdタグを除去
		print ( "講義名 : ", end = '' )
		print ( subject.contents[0], subject.td.string )
		subject.td.decompose ( ) # tdタグを除去
		print ( "単位数 : ", end = '' )
		print ( subject.contents[1], subject.td.string, "\n" )

	#url
	url = "http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01161.html.ja"

	#get html
	html = request.urlopen ( url )

	#set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	#get ClassInfo
	Subjects = soup.find_all ( "tr", attrs = { "class", "subject" } )
	
	print ( "共通数理科目\n" )

	#print ClassInfo
	for subject in Subjects:
		subject.td.decompose ( ) # tdタグを除去
		print ( "講義名 : ", end = '' )
		print ( subject.contents[0], subject.td.string )
		subject.td.decompose ( ) # tdタグを除去
		print ( "単位数 : ", end = '' )
		print ( subject.contents[1], subject.td.string, "\n" )

if __name__ == "__main__":
	scraping ( )
