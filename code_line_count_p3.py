#! Python 3.5
import os
import sys

# from distutils.core import setup
# import py2exe

# http://www.iplaypython.com/code/c137.html
# weng, 2016-11-29 2040
# weng, 2018-10-24 0132 program can be used in python3 and idea IDE.

class LineCount:
    def trim(self, linestring):
        if not linestring:
            return ''
        lines = linestring.expandtabs().splitlines()

        indent = sys.maxsize
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))

        trimmed = [lines[0].strip()]
        if indent < sys.maxsize:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())

        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)

        return '\n'.join(trimmed)

    # 对一个文件的行数进行统计
    def FileLineCount(self,filename):
        (filepath, tempfilename) = os.path.split(filename)
        (shotname, extension) = os.path.splitext(tempfilename)
        if extension == '.cs' or extension == '.cpp' or extension == '.h' or extension == '.py':  # file type

            # 去除designer的影响
            if 'Designer.cs' in tempfilename:
                return

            try:
                file = open(filename, 'r',  encoding='ISO-8859-1') # gbk or some other type
            except Exception as e:
                file = open(filename, 'r', encoding='utf-8')   # utf-8,encoding='utf-8'
            finally:
                pass

            self.sourceFileCount += 1
            lineCount = 0
            commentCount = 0
            blankCount = 0
            codeCount = 0

            while True:
                eachLine = "";
                try:
                    eachLine = file.readline()  # find bug
                except Exception as e2:
                    print(filename, e2)
                    # 'utf-8' codec can't decode byte 0xb5 in position 2223: invalid start byte
                    # python3默认的就是unicode编码。
                    # FIXED BY WENG OF: file = open(filename, 'r',  encoding='ISO-8859-1')

                if not eachLine:
                    break
                if eachLine != " ":
                    eachLine = eachLine.replace(" ", "")  # remove space
                    eachLine = self.trim(eachLine)  # remove tabIndent
                    if eachLine.find('//') == 0:  # LINECOMMENT
                        commentCount += 1
                    else:
                        if eachLine == "":
                            blankCount += 1
                        else:
                            codeCount += 1
                lineCount = lineCount + 1
            file.close()
            self.all += lineCount
            self.allComment += commentCount
            self.allBlank += blankCount
            self.allSource += codeCount
            self.PrintFilesPathRelative(filename)

            # print(filename)
            # print ('           Total      :',lineCount)
            # print ('           Comment    :',commentCount)
            # print ('           Blank      :',blankCount)
            # print ('           Source     :',codeCount)
        else:
            pass #other type file



    # 输出文件或文件夹的路径
    def PrintFilesPathRelative(self, filename):
        # nPos = len(self.filename)
        # nPos += 1
        # relatative_fullPath = '..\\' + filename[nPos:]
        relatative_fullPath = '.\\' +  filename[self.nPos:]
        print(relatative_fullPath)

    # 调用的计算主函数
    def CalulateCodeCount(self, filePath):
        if os.path.isdir(filePath):
            if not filePath.endswith('\\'):
                filePath += '\\'
            for file in os.listdir(filePath):
                file_or_path = filePath + file
                # path
                if os.path.isdir(file_or_path):

                    # ignore debug file
                    if "Debug" in file_or_path \
                            or 'BaseCommon' in file_or_path or 'DataOperate' in file_or_path:
                        continue
                    # ignore some dir
                    # if "nplot" in file_path: # and  ~ ('NControl' in file_path)
                    #    continue


                    # print the relative path
                    self.PrintFilesPathRelative(file_or_path)
                    self.CalulateCodeCount(file_or_path)
                else:
                    # file
                    self.FileLineCount(file_or_path)
        else:
            self.FileLineCount(filePath)

    # Open File
    def __init__(self):
        self.all = 0
        self.allComment = 0
        self.allBlank = 0
        self.allSource = 0
        self.sourceFileCount = 0

        self.code_dir = input('Enter file name: ')

        # nPos
        nPos = len(self.code_dir)
        if self.code_dir.endswith('\\'):
            nPos -=1
        nPos +=1
        self.nPos = nPos

        # get files
        self.CalulateCodeCount(self.code_dir)
        if self.sourceFileCount == 0:
            print('No Code Files')
            pass;
        print('\n')
        print('*****************  All Files  **********************')
        print('    Code Dir   :', self.code_dir)
        print('    Files      :', self.sourceFileCount)
        print('    Total      :', self.all)
        print('    Comment    :', self.allComment)
        print('    Blank      :', self.allBlank)
        # print('    Bracket     :', self.bracketCount)
        print('    Source     :', self.allSource)
        print('\n    Code Rato  :%6.2f%%'%(float(self.allSource)/self.all*100))
        print('****************************************************')


# setup( 

#     version = "0.0.1", 
#     description = "LineCount", 
#     name = "LineCount", 

#     console = ["LineCount.py"], 
#     ) 

myLineCount = LineCount()
# D:\WorkArts\ZJECMS
# D:\WorkArts\ZJECMS\DBFSR
