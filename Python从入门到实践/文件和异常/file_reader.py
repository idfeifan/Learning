# coding=utf-8
class Read_file():
    def readFile(self,path):
        #使用with关键字，不需要访问文件后自动关闭
        with open(path) as file_object:
            #contents = file_object.readlines()
            for i in file_object:
                print(i.rstrip())

    def excepts(self):
        print("请输入连个数字。")
        print("输入'q'退出")
        while True :
            first_number = input("\n 请输入第一个值：\n")
            if first_number == 'q':
                break
            second_number = input("\n请输入第二个值: \n")
            if first_number == 'q':
                break
            try:
                print(int(first_number) / int(second_number))
            except ZeroDivisionError:
                print('分母不能为零')
                break
    def read_alice(self,file_name):
        try:
            with open(file_name) as f_obj:
                cont = f_obj.read()
        except FileNotFoundError:
            print('文件位置不对')
        else:
            #计算文件大致包含多少个单词
            words = cont.split()
            num_words = len(words)
            print("the file %s has about %s words" %(file_name,str(num_words)))



read_file = Read_file()
read_file.read_alice('Alis')