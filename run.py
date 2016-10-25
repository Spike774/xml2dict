# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import csv

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse('oct9 export for convert1.xml')
collection = DOMTree.documentElement
if collection.hasAttribute("Document"):
   print "Root element : %s" % collection.getAttribute("Document")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("Placemark")

# 准备写入csv的文档
places_csv = file('places.csv', 'wb')
writer = csv.writer(places_csv)

# 打印每部电影的详细信息
for movie in movies:
    print "*****Place*****"
    if movie.hasAttribute("name"):
        print "Name: %s" % movie.getAttribute("name")

    # type = movie.getElementsByTagName('type')[0]
    # print "Type: %s" % type.childNodes[0].data
    # format = movie.getElementsByTagName('format')[0]
    # print "Format: %s" % format.childNodes[0].data
    # rating = movie.getElementsByTagName('rating')[0]
    # print "Rating: %s" % rating.childNodes[0].data
    # description = movie.getElementsByTagName('description')[0]
    # print "Description: %s" % description.childNodes[0].data
    names = movie.getElementsByTagName('name')[0]
    print "Placemark: %s" % names.childNodes[0].data
    coordinates = movie.getElementsByTagName('coordinates')[0]
    print "Coordinate: %s" % coordinates.childNodes[0].data
    writer.writerows([(names.childNodes[0].data, coordinates.childNodes[0].data)])

places_csv.close()