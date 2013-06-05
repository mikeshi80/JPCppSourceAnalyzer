JP CPP Source Analyzer
======================

This is the small utility for extracting the line number where contains Japanese charactors from the C/C++ source code, and it will ignore the Japanese charactors in the comments. It can output the results in the output.txt file.

### output.txt format
The format like following:

    ####### <file path> ######
    line number,    line stuff
    ####### <another file path> #######
    line number,    line stuff
    line number,    line stuff

### Motivition
I created this tool for internationalizing a legacy source code, we need find where the Japanese charactors is and use i18n function to replace them.

### Usage
First, please install python 2.x (2.5 above since I maybe use some features only exists on 2.5 above), and run

    python main.py <top dir> <ext file name 1> [<ext file name 2>] ...

For example, you can find the Japanese charactors line numbers in the **D:/Server** folders, including .h, .c and .cpp files

    python main.py D:/Server .h .c .cpp

### Attention
Currently the utility assume the source code which contains Japanese charators is encoded as cp932 (shift-jis), you can change it by modify the variable **encoding** in the JPAnalyzer.py

JP CPP Source Analyzer
======================

这是一个用来抽取C/C++代码中包含有日文的代码行号的小工具，它能自动略过注释中的日文。它最终将结果输出到output.txt文件中。

### output.txt格式
基本格式如下

    ####### <file path> ######
    line number,    line stuff
    ####### <another file path> #######
    line number,    line stuff
    line number,    line stuff

### 动机
我是为了一个国际化历史遗留代码的国际化而创建了这个工具。我们需要将原来写在语句中的日文抽取出来，用i18n的函数来代替。

### 用法
首先，请安装 python 2.x（最好是2.5以上的，我可能无意中使用到只有2.5才有的功能了），并且运行

    python main.py <top dir> <ext file name 1> [<ext file name 2>] ...

比如说，我们要找出所有在**D:/Server**目录下的.h, .c, .cpp文件，只要运行

    python main.py D:/Server .h .c .cpp

### 注意
目前工具假定包含日语文字的代码是cp932（也就是shift-jis）编码的，你可以通过修改JPAnalyzer.py文件中的 **encoding** 变量来修改它。

