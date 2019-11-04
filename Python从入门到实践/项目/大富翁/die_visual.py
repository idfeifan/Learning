# coding=utf-8
from Python从入门到实践.项目.大富翁.Die import Die
import pygal

#创建一个D6
die = Die()

#郑几次骰子，并将结果存储在一个列表中
results = []

for row_num in range(1000):
    results.append(die.roll())

#分析结果
frequencies = []

for value in range(1,die.num_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)


#结果可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6",frequencies)
hist.render_to_file('die_visual.svg')


