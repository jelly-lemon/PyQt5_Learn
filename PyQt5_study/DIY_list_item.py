import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# 自定义的item 继承自QListWidgetItem
class customQListWidgetItem(QListWidgetItem):
    def __init__(self, name, img):
        super().__init__()
        # 自定义item中的widget 用来显示自定义的内容
        self.widget = QWidget()
        # 用来显示name
        self.nameLabel = QLabel()
        self.nameLabel.setText(name)
        # 用来显示avator(图像)
        self.avatorLabel = QLabel()
        # 设置图像源 和 图像大小
        self.avatorLabel.setPixmap(QPixmap(img).scaled(50, 50))
        # 设置布局用来对nameLabel和avatorLabel进行布局
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.avatorLabel)
        self.hbox.addWidget(self.nameLabel)
        self.hbox.addStretch(1)
        # 设置widget的布局
        self.widget.setLayout(self.hbox)
        # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        self.setSizeHint(self.widget.sizeHint())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 主窗口
    w = QWidget()
    w.setWindowTitle("QListWindow")
    # 新建QListWidget
    listWidget = QListWidget(w)
    listWidget.resize(300, 300)

    # 新建两个自定义的QListWidgetItem(customQListWidgetItem)
    item1 = customQListWidgetItem("鲤鱼王", "./img/head.jpg")
    item2 = customQListWidgetItem("可达鸭", "./img/head.jpg")

    # 在listWidget中加入两个自定义的item
    listWidget.addItem(item1)
    listWidget.setItemWidget(item1, item1.widget)
    listWidget.addItem(item2)
    listWidget.setItemWidget(item2, item2.widget)

    # 绑定点击槽函数 点击显示对应item中的name
    listWidget.itemClicked.connect(lambda item: print(item.nameLabel.text()))

    w.show()
    sys.exit(app.exec_())