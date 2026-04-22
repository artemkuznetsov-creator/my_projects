import xml.etree.ElementTree as ET
def command_1(root):
    answer = ''
    for router in root.findall('./router'):
        name = router.findtext('name')
        if name:
            answer += name
        antennas = router.findtext('antennas')
        if antennas:
            answer += " " + antennas
        frequency = router.findtext('frequency')
        if frequency:
            answer += " " + frequency
        standard = router.findtext('standard')
        if standard:
            answer += " " + standard
        ports = router.findtext('ports')
        if ports:
            answer += " " + ports
        answer += "\n"
    print(answer)
def command_2(root):
    value = input("Введите бренд: ")
    elements = root.findall(f".//name[@brand='{value}']")
    if len(elements) > 0:
        for element in elements:
            print(element.text)
def command_3(root, tree):
    name = input("Название: ")
    article = input("Артикул: ")
    brand = input("Бренд: ")
    antennas = input("Количество антенн: ")
    frequency = input("Частота: ")
    standard = input("Стандарт WiFi: ")
    ports = input("Порты: ")

    router = ET.Element('router')
    router.set('article', article)

    name_el = ET.SubElement(router, 'name')
    name_el.set('brand', brand)
    name_el.text = name

    antennas_el = ET.SubElement(router, 'antennas')
    antennas_el.text = antennas
    frequency_el = ET.SubElement(router, 'frequency')
    frequency_el.text = frequency
    standard_el = ET.SubElement(router, 'standard')
    standard_el.text = standard
    ports_el = ET.SubElement(router, 'ports')
    ports_el.text = ports

    root.append(router)
    tree.write('data.xml', encoding='UTF-8')
def command_4(root, tree):
    article = input('Введите артикул: ')
    router = root.find(f"./router[@article='{article}']")
    if router is not None:
        root.remove(router)
        tree.write('data.xml', encoding='UTF-8')
def command_6(root, tree):
    with_usb = ET.Element('routers')
    without_usb = ET.Element('routers')
    for router in root.findall('./router'):
        ports = router.findtext('ports')
        print(ports)
        if '1xUSB' in ports:
            with_usb.append(router)
        else:
            without_usb.append(router)
        tree_with_usb = ET.ElementTree(with_usb)

        tree_without_usb = ET.ElementTree(without_usb)
        tree_with_usb.write('has_wires.xml', encoding='UTF-8')
        tree_without_usb.write('wireless.xml', encoding='UTF-8')




def main():
    XMLTree = ET.parse('data.xml')
    root = XMLTree.getroot()
    print("1: Вывод всех маршрутизаторов")
    print("2: Вывод по бренду")
    print("3: Добавление")
    print("4: Удаление")
    print("5: Выход")
    print("6: Разделить")
    while True:

        print('-' * 100)
        commands = input("Введите номер команды: ")
        if commands == '1':
            command_1(root)

        if commands == "2":
            command_2(root)
        if commands == "3":
            command_3(root, XMLTree)
        if commands == "4":
             command_4(root, XMLTree)
        if commands == "5":
            break
        if commands == "6":
            command_6(root, XMLTree)
if __name__ == '__main__':
    main()