#!/usr/bin/env python
# coding=utf-8
import re

sample = '''
<td>学年</td><td>学期</td><td>课程代码</td><td>课程名称</td><td>课程性质</td><td>课程归属</td><td>学分</td><td>绩点</td><td>平时成绩</td><td>期中成绩</td><td>期末成绩</td><td>实验成绩</td><td>成绩</td><td>辅修标记</td><td>补考成绩</td><td>重修成绩</td><td>学院名称</td><td>备注</td><td>重修标记</td><td>课程英文名称</td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BH04227</td><td>JAVA Web技术</td><td>必修课</td><td>&nbsp;</td><td>3.0</td><td>   4.00</td><td>92</td><td>&nbsp;</td><td>92</td><td>96</td><td>93</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RL04911</td><td>UML及其应用</td><td>选修课</td><td>&nbsp;</td><td>2</td><td>   4.00</td><td>97.5</td><td>&nbsp;</td><td>89</td><td>&nbsp;</td><td>92</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BS04921</td><td>操作系统实践</td><td>必修课</td><td>&nbsp;</td><td>2.5</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>91</td><td>96</td><td>94</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>1BS15001</td><td>公益劳动</td><td>必修课</td><td>&nbsp;</td><td>1.0</td><td>   4.00</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>91</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>校内劳动</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>1BH16001</td><td>毛泽东思想和中国特色社会主义理论体系概论</td><td>必修课</td><td>&nbsp;</td><td>4.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>87</td><td>&nbsp;</td><td>94</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>政治理论教育学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0BH04226</td><td>软件测试技术</td><td>必修课</td><td>&nbsp;</td><td>2</td><td>   4.00</td><td>98</td><td>&nbsp;</td><td>89</td><td>98</td><td>92</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BH04926</td><td>软件工程</td><td>必修课</td><td>&nbsp;</td><td>3.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>87</td><td>98.4</td><td>93</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RH04214</td><td>数据库安全</td><td>选修课</td><td>&nbsp;</td><td>2.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>92</td><td>100</td><td>96</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BS04228</td><td>移动应用开发实践</td><td>必修课</td><td>&nbsp;</td><td>2.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>&nbsp;</td><td>100</td><td>100</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RH04221</td><td>中间件技术</td><td>选修课</td><td>&nbsp;</td><td>2.0</td><td>   3.00</td><td>90</td><td>&nbsp;</td><td>83</td><td>85</td><td>85</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机学院</td><td>&nbsp;</td><td>0</td><td></td>
	</tr>
</table>
'''

if_match = re.findall(r'(<td>(.*)</td>){3}<td>(.*)</td><td>(.*)</td><td>&nbsp;</td>(<td>(.*)</td>){6}<td>([0-9]*)</td><td>0</td>', sample)
for i in if_match:
	print i



