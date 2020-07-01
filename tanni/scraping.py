"""
File Name : scraping.py
Designer : Kaito Akizuki
Date : 2020/07/01, pm9:50
"""

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

	print ( "時間割\n" )

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
						print ( "授業名 :", j.string )
					for l in k.find_all ( "td", colspan = "2" ):
	  					print ( "教員名 :", l.string, "\n" )

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

	# kind_tanni = { "◎":"必修", "○":"選択必修", "△":"選択", "□":"自由", "☆":"必須認定" }
	print ( "シラバス\n" )

	for i in Subjects:
		for j in i.find_all ( "tr", attrs = { "class", "subject" } ):
			print ( "授業名 : ", j.contents[3].string )
			print ( "必修状況 : ", end = "" )

			for k in j.find_all ( align = "CENTER" ):
				print ( k.text, end = "" )
					
			print ( "\nコマ数 : ", end = "" )

			if j.contents[15].string is None:
				print ( j.contents[11].string )
			elif ( j.contents[14].string == "1" ) or ( j.contents[14].string == "2" ) or ( j.contents[14].string == "3" ):
				print ( j.contents[14].string )
			else:
				print ( j.contents[15].string )

			print ( "単位数 : ", j.contents[5].string, "\n" )

			# 卒研,海外実習コマ数 -> 14, 通常コマ数 -> 15, 情報工学実習コマ -> 11
			# print ( "11 ->", j.contents[11].string )
			# print ( "14 ->", j.contents[14].string )
			# print ( "15 ->", j.contents[15].string )

if __name__ == "__main__":
	Time_Scraping ( )
	Syllabus_Scraping ( )
