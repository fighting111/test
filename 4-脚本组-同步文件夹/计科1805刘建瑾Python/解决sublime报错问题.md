# 解决在sublime上查看案例报错问题
### 除turtle库案例外，这些案例均在IDLE上完成，可能使用sublime会报错。
### 原因是Python在默认状态下不支持源文件的编码，即中文注释的问题。
#### 有以下三种解决方式：
1. 在文件头部添加如下代码：`# coding = utf-8`
2. 在文件头部添加如下两行代码：

        #!/usr/bin/python
        # -*-coding:utf-8-*-
3. 在文件头部添加如下两行代码：

        #!/usr/bin/python
        # vim:set fileencoding=utf-8: