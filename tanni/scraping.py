"""
File Name : scraping.py
Designer : Kaito Akizuki
Date : 2020/07/01, pm9:50
"""

from urllib import request
from bs4 import BeautifulSoup
from .models import Subject, Course

def time_scraping(url):
	# get html
	html = request.urlopen(url)

	# set BeautifulSoup
	soup = BeautifulSoup (html, "html.parser")

	week_name = ["mon", "tue", "wed", "thu", "fri", "sat", "oth"]

	print ("時間割\n")

	cnt = 0
	for week in range(7):
		print("\n" + week_name[week] + "\n")
		#get ClassInfo
		temp = soup.find_all("table", id = week_name[week])
		for time in range (6):
			# 1限 ( row = 0 )
			print ( "\n" )
			print ( time + 1, end = "" )
			print ( "限\n" )
			for i in temp:
				for k in i.find_all ( "td", row = time ):
					for j in k.find_all ( "a", target = "_blank" ):
						title = j.string
						print("授業名 :", j.string)
					for l in k.find_all ( "td", colspan = "2" ):
						teacher = l.string
						print("教員名 :", teacher, "\n")
					if not Course.objects.filter(year=2020, term=1, week=week+1, period=time+1).exists():
						if Subject.objects.filter(title=title).exists():
							subject_id = Subject.objects.filter(title=title).first()
							course = Course(subject_id=subject_id, year=2020, term=1, week=week+1, period=time+1, place="豊洲", teacher=teacher)
							course.save()
							cnt += 1
	
	return cnt
						

def syllabus_scraping(url, group):
	# get html
	html = request.urlopen ( url )
   	# set BeautifulSoup
	soup = BeautifulSoup ( html, "html.parser" )

	# get ClassInfo
	# Subjects = soup.find_all ( "tr", attrs = { "class", "subject" } )
	Subjects = soup.find_all ( "tbody" )

	# kind_tanni = { "◎":"必修", "○":"選択必修", "△":"選択", "□":"自由", "☆":"必須認定" }
	print ( "シラバス\n" )

	cnt = 0
	for i in Subjects:
		for j in i.find_all ( "tr", attrs = { "class", "subject" } ):
			title = j.contents[3].string
			print ( "授業名 : ", title)

			print ( "必修状況 : ", end = "" )
			required = ""
			for k in j.find_all ( align = "CENTER" ):
				required = k.text
				print ( k.text, end = "" )
					
			print ( "\nコマ数 : ", end = "" )
			unit = 1
			if j.contents[15].string is None:
				unit = int(j.contents[11].string)
				print ( j.contents[11].string )
			elif ( j.contents[14].string == "1" ) or ( j.contents[14].string == "2" ) or ( j.contents[14].string == "3" ):
				unit = int(j.contents[14].string)
				print ( j.contents[14].string )
			else:
				unit = int(j.contents[15].string)
				print ( j.contents[15].string )

			print ( "単位数 : ", j.contents[5].string, "\n" )
			credit = j.contents[5].string
			# 卒研,海外実習コマ数 -> 14, 通常コマ数 -> 15, 情報工学実習コマ -> 11
			# print ( "11 ->", j.contents[11].string )
			# print ( "14 ->", j.contents[14].string )
			# print ( "15 ->", j.contents[15].string )

			if not Subject.objects.filter(title=title).exists():
				subject = Subject(title=title, group=group, required=required, unit=unit, credit=credit)
				subject.save()
				cnt += 1

	return cnt
			

#if __name__ == "__main__":
	# time_scraping()
	#syllabus_scraping()
