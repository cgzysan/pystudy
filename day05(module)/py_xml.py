#!/usr/bin/env python3
# by ysan

import xml.etree.cElementTree as ET

tree = ET.parse('xml_test.xml')
root = tree.getroot()
print(root, root.tag)


# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update', 'yes')

tree.write('xml_test.xml')

# 删除
for country in root.iter('country'):
    rank = int(country.find('rank').text)
    if rank > 40:
        root.remove(country)

tree.write('xml_test.xml')

# 创建xml文档
new_xml = ET.Element("friends")

info = ET.SubElement(new_xml, "info", attrib={"color": "red"})
name = ET.SubElement(info, "name")
name.text = "peng"
age = ET.SubElement(info, "age")
age.text = "25"

info2 = ET.SubElement(new_xml, "info", attrib={"color": "blue"})
name = ET.SubElement(info2, "name")
name.text = "deng"
age = ET.SubElement(info2, "age")
age.text = "22"

et = ET.ElementTree(new_xml)    # 生成文档对象
et.write("py_xml.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)    # 打印生成的格式
