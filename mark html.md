# 制作网页的步骤

- 1.初始化(引入外部css)

- 2.观察有没有`公共`common(不变的)部分，有就先提取出来做(`先引用`！字体图标在自己css的前面！)

`图标`不需要放到img文件夹中，需要放到`当前目录`下。

1.多次使用，节约代码。
2.方便维护，统一修改。

> ctrl + F5 网页强制刷新

- 3.确定页面版心(页面大致在哪个中间:宽度+margin:0 auto;) index-首页

- 4.分析每块的结构

  (类需要在css中 .类才可以生效)

  (要清楚给谁加，清楚谁是父元素)

  (ul>li li只要是一整块元素，就需要加li标签)

  (结构/状态伪类不可以光写first-child,还需要写清楚是具体的哪个元素a/p?)

  (`单行`一般`父盒子`设置高度，子盒子不设置；`多行`一般子盒子设置高度，`父盒子`不设置，二者刚好相反)

  (分清楚，是否可以写成一个部分，一个部分就多类名`写一起`，空格隔开。不是就是，`嵌套`关系。)?
  
  (css找定位的时候class="xxx"->.xxx|如果是input->input就可以 标签选择器)
  
  (如果遇到上下只是细微差距，只需要多类名标签 class="box-bd hot"->class="box-bd fresh"来分别开再修改)
  
  (/* 两端对齐** /  justify-content: space-between;  / *居中对齐 */ align-items: center;)
  
  (display:flex ->要设置高度才有效!)
  
  (行内元素变成定位则可设置宽、高)
  
- 名词

position:absolute、relative  /display:block、inline-block

 transition:all 0.2s 过渡 | transform:translateY(-83px); 转换

- 



# 设计稿的快捷键技巧

- 按住空格，鼠标可以拖动页面
- 鼠标先点住一条线，再悬浮在另外一个线上可以看高度
-  Figma，可以按住 `Alt` 键，鼠标 hover 到元素上，就能看到和相邻元素的边距 px。



