# 设计目标
1. 设计一个PyQt5实现的GUI --> 转为使用PySide6实现
2. 包含功能:
   - 静态文本、按扭、图像、输入框、列表、图表、多选框、单选框
   - 选项卡(实现多窗口)、图表与数据关联、数据导入和导出
   - 功能可通过命令行调用
   - 高级可视化图、动态外部数据输入与显示(如串口输入、网络输入)
   - 提供易于使用的对外接口
3. 虚拟需求:
   - 某工业生产机器状态检测，可动态显示实时数据(实时数据模拟实现)
   - 实时数据和历史数据的图表显示，可选择时间跨度和显示数据类型
   - 提供命令行调用方式，以满足软件在无图形界面操作系统中使用
   - 数据的高级可视化图显示
4. 实际应用场景:
   - MCU的串口调试
   - 物联网设备的网络调试
   - 工业设备有线调试
   - 数据分析

# windows打包.exe
```sh
pip install pyinstaller
pip install auto-py-to-exe
auto-py-to-exe
```

# 参考资料
- [PyQt vs PySide 对比](https://geek-docs.com/pyqt/pyqt-questions/134_pyqt_pyqt_vs_pyside_comparison.html)
- [https://pypi.org/project/PyQt5/](https://pypi.org/project/PyQt5/)
- [https://wiki.python.org/moin/PyQt](https://wiki.python.org/moin/PyQt)
- [The complete PyQt5 tutorial — Create GUI applications with Python](https://www.pythonguis.com/pyqt5-tutorial/)
- [Qt for Python官方教程](https://doc.qt.io/qtforpython-6/tutorials/index.html)
- [16x16 icon](https://p.yusukekamiyamane.com/)
- [细致讲解python怎么做类型标注](http://www.coolpython.net/python_senior/data_type/py-type-hints-detail.html)
- [Python中类属性和实例属性的区别](https://zhuanlan.zhihu.com/p/624007920)
- [小白白也能学会的 PyQt 教程 —— 图像类及图像相关基础类介绍](https://cloud.tencent.com/developer/article/2289417)
- [一篇文章让你读懂PyQt5布局管理，绝对干货](https://cloud.tencent.com/developer/article/1437295)
- [全面认识 Qt Widgets、QML、Qt Quick](https://zhuanlan.zhihu.com/p/634276734)
- [Pyside | PYQT无边框设计，窗口移动和调整大小的简单写法](https://blog.csdn.net/CoderDeer/article/details/133361861)
- [6个例子快速学会python中subprocess库的使用](https://blog.csdn.net/Light2077/article/details/110913337)