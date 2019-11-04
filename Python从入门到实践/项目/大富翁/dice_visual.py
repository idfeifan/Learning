# coding=utf-8
from Python从入门到实践.项目.大富翁.Die import Die
import pygal

#创建一个D6
die_1 = Die()
die_2 = Die()
#郑几次骰子，并将结果存储在一个列表中
results = []

for row_num in range(1000):
    result = die_1.roll() +die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result + 1):
    frequence = results.count(value)
    frequencies.append(frequence)


#结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6 + D6",frequencies)
hist.render_to_file('dice_visual.svg')


