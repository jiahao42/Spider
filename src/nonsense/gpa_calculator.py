#!/usr/bin/env python
# coding=utf-8
import wx, sqlite3,sys

'''
TODOLIST:
1.把数据库的表建好
1.做好删除课程功能
2.统计平均绩点
3.筛选选修课
4.将绩点转换成4分制
'''


class CourseManger(wx.Frame):  # 框架类

	def __init__(self, parent, title, size):
		wx.Frame.__init__(self, parent=parent, title=title, size=size)  # 初始化超类WX.Frame
		self.UIinit()  # 初始化UI
		self.Show()
		self.Centre()  # 打开程序显示在屏幕中心
		self.BindFunc()
		self.db = CourseDb()
		self.coursesList = self.db.getdb()
		

	def UIinit(self):  # UI初始化函数
		bkg = wx.Panel(self)  # 设置背景
		self.help_info = wx.Button(bkg, -1, u'帮助信息')  # 设置按钮
		self.show_all_course = wx.Button(bkg, -1, u'所有课程')
		self.reset_course = wx.Button(bkg, -1, u'清空课程')
		self.add_course = wx.Button(bkg, -1, u'添加课程')
		self.exit_program = wx.Button(bkg, -1, u'退	   出')
		self.course_calc = wx.Button(bkg, -1, u'计算绩点')
		self.content = (wx.TextCtrl(bkg, style=wx.TE_MULTILINE))  # 设置文本框
		self.course_name = wx.TextCtrl(bkg, -1, u'课程名称')
		self.course_credit = wx.TextCtrl(bkg, -1, u'学分')
		self.course_grade = wx.TextCtrl(bkg, -1, u'绩点')
		self.course_optional = wx.CheckBox(bkg, -1, u'选修')
		self.course_delete = wx.TextCtrl(bkg, -1, u'课程名称')
		self.course_delete_button = wx.Button(bkg, -1, u'删除课程')
		self.author = wx.StaticText(bkg,-1,'Created by James')

		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(self.help_info, proportion=1, flag=wx.ALL, border=2)  # 添加按钮到布局
		box.Add(self.show_all_course, proportion=1, flag=wx.ALL, border=2)
		box.Add(self.course_calc, proportion=1, flag=wx.ALL, border=2)
		box.Add(self.reset_course, proportion=1, flag=wx.ALL, border=2)
		box.Add(self.exit_program, proportion=1, flag=wx.ALL, border=2)

		info_box = wx.BoxSizer(wx.HORIZONTAL)
		info_box.Add(self.course_name, proportion=5, flag=wx.Centre | wx.ALL, border=2)
		info_box.Add(self.course_credit, proportion=2, flag=wx.Centre | wx.ALL, border=2)
		info_box.Add(self.course_grade, proportion=2, flag=wx.Centre | wx.ALL, border=2)
		info_box.Add(self.course_optional, proportion=1, flag=wx.Centre | wx.ALL, border=2)
		info_box.Add(self.add_course, proportion=2, flag=wx.Centre | wx.ALL, border=2)

		delete_box = wx.BoxSizer(wx.HORIZONTAL)
		delete_box.Add(self.course_delete, proportion=4, flag=wx.Centre | wx.ALL, border=2)
		delete_box.Add(self.course_delete_button, proportion=2, flag=wx.Centre | wx.ALL, border=2)
		delete_box.Add(self.author,proportion = 2,flag = wx.TOP|wx.LEFT,border=20)

		right_box = wx.BoxSizer(wx.VERTICAL)
		right_box.Add(info_box, proportion=0, flag=wx.TOP | wx.ALL, border=2)
		right_box.Add(delete_box, proportion=0, flag=wx.TOP | wx.ALL, border=2)
		right_box.Add(self.content, proportion=10, flag=wx.EXPAND | wx.ALL, border=2)

		vbox = wx.BoxSizer(wx.HORIZONTAL)
		vbox.Add(box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
		vbox.Add(right_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
		bkg.SetSizer(vbox)

	def BindFunc(self):  # 绑定函数
		self.Bind(wx.EVT_BUTTON, self.HelpInfo, self.help_info)
		self.Bind(wx.EVT_BUTTON, self.CoursesInfo, self.show_all_course)
		self.Bind(wx.EVT_BUTTON, self.reset, self.reset_course)
		self.Bind(wx.EVT_BUTTON, self.AddCourse, self.add_course)
		self.Bind(wx.EVT_BUTTON, self.quit, self.exit_program)
		self.Bind(wx.EVT_BUTTON,self.DelCourse,self.course_delete_button)
		self.Bind(wx.EVT_BUTTON,self.CalcGrade,self.course_calc)

	def HelpInfo(self, event):
		help_info = u"绩点管理助手 "
		self.content.SetValue(help_info)
		
	def reset(self,event):
		self.db.cu.execute("delete from course")
		self.coursesList = self.db.getdb()
	def CoursesInfo(self, event):
		if len(self.coursesList) > 0:
			text = ''
			for course in self.coursesList:
				text = text + u'课程名称: ' + unicode(course[0]) + u',  学分: ' + unicode(course[1]) + u',  成绩: ' + course[2] +  u',  是否选修: '
				if course[3] == 0:
					text += u'否' + '\n'
				else:
					text += u'是' + '\n'
			self.content.SetValue(text)
		else:
			self.content.SetValue(u"没有课程")

	def CalcGrade(self,event):
		sum_credit = 0
		sum_grade = 0
		sum_course = 0
		self.coursesList = self.db.getdb()
		self.non_option_coursesList = self.db.get_non_option()
		for course in self.coursesList:
			sum_course += 1
			sum_grade += float(course[1]) * float(course[2])
			sum_credit += float(course[1])
		text = ''
		text += u"课程总数: "
		text += str(sum_course) + '\n'
		text += u"总学分为: "
		text += str(sum_credit) + '\n'
		text += u"总学分绩点为: " + str(sum_grade) + '\n'
		text += u"所有课程的平均绩点为: "
		text += str(sum_grade/sum_credit) + '\n\n\n'
		sum_grade = 0
		sum_credit = 0
		for course in self.non_option_coursesList:
			sum_grade += float(course[1]) * float(course[2])
			sum_credit += float(course[1])
		text += u"必修课修课的学分为: " + str(sum_credit) + '\n'
		text += u"必修课学分绩点为: " + str(sum_grade) + '\n'
		text += u"必修课的平均绩点为: "
		text += str(sum_grade/sum_credit) + '\n\n\n'
		
		sum_grade = 0
		sum_credit = 0
		for course in self.non_option_coursesList:
			sum_grade += float(course[1]) * int(float((course[2])))
			sum_credit += float(course[1])
		text += u"必修课修课的学分为(4分制): " + str(sum_credit) + '\n'
		text += u"必修课学分绩点为(4分制): " + str(sum_grade) + '\n'
		text += u"必修课的平均绩点为(4分制): "
		text += str(sum_grade/sum_credit)
			
			
		self.content.SetValue(text)
		
		
			
			
	def CourseCount(self, event):
		text = u'一共有' + str(len(self.coursesList)) + u'门课程'
		self.content.SetValue(text)

	def AddCourse(self, event):
		name = self.course_name.GetValue()
		credit = self.course_credit.GetValue()
		grade = self.course_grade.GetValue()
		optional = self.course_optional.GetValue()
		info = [name,credit,grade,optional]
		self.db.cu.execute("insert into course values (?,?,?,?)",info)
		self.db.cx.commit()
		self.coursesList = self.db.getdb()

	def DelCourse(self, event):
		name = self.course_delete.GetValue()
		self.db.cu.execute("delete from course where name='" + unicode(name) + "'")
		self.db.cx.commit()
		self.coursesList = self.db.getdb()

	def quit(self, event):
		sys.exit()


class CourseDb(object):  # 数据库类
	def __init__(self):
		# self.cx=sqlite3.connect(':memory:')#创建数据库于内存，如果要创建数据库文件，传入path参数
		self.cx = sqlite3.connect('course.db')
		self.cu = self.cx.cursor()  # 创建数据库游标
		#  表中三项数据 课程名称 课程学分 课程绩点 是否选修
		self.cu.execute("create table if not exists course (name,credit,grade,optional)")  # 建表

	def getdb(self):
		self.cu.execute("select * from course")  # 数据库查询
		self.coursesList = self.cu.fetchall()  
		# 获取查询结果。这里返回的是列表。每一项为数据库的一行，格式为元组。[(?,?,?),(?,?,?)]这样的格式
		return self.coursesList
	def get_non_option(self):
		self.cu.execute("select * from course where optional=0")
		self.coursesList = self.cu.fetchall()
		return self.coursesList

class Cmapp(wx.App):  # 程序类
	def OnInit(self):
		Coursedata = CourseDb().getdb()
		c = CourseManger(parent=None, title="CourseManger", size=(600, 400))
		return True


if __name__ == '__main__':
	app = Cmapp()

	app.MainLoop()
