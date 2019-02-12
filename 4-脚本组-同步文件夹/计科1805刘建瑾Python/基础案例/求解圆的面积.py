radius = int(input('请输入想要求解的圆的半径：'))
def Area(radius):
    area = radius **2 *3.1415926
    return area
print('半径是: %d' % radius,'圆的面积是: ',Area(radius))
