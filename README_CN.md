# Stroop实验 

![image-20240130193625956](https://cdn.jsdelivr.net/gh/Sean652039/pic_bed@main/uPic/image-20240130193625956.png)

![image-20240130193612656](https://cdn.jsdelivr.net/gh/Sean652039/pic_bed@main/uPic/image-20240130193612656.png)

## 简介
本项目使用Python中的Pygame库实现了一个Stroop测试实验。Stroop测试是一种心理学任务，用于测量参与者在被要求忽略文字含义、仅关注打印文字颜色时的反应时间。

## 依赖项
- Python 3.x
- Pygame库（使用 `pip install pygame` 安装）

## 文件与模块

### `Stroop.py`
这个脚本包含Stroop测试实验的核心功能。包括以下内容：

1. **初始化:**
   - 导入必要的模块 (`pygame`, `sys`)。
   - 从`Settings`模块导入`settings`类。
   - 从`Functions`模块导入功能函数。

2. **Stroop测试执行:**
   - 定义`run_exper`函数，设置Pygame窗口，显示介绍屏幕，并使用`Functions`模块中的`run1`函数启动Stroop测试。

3. **Pygame窗口设置:**
   - 初始化Pygame并设置窗口。

4. **介绍屏幕:**
   - 显示包含Stroop测试标题和说明的介绍屏幕。

5. **事件处理与开始测试:**
   - 等待按键触发以启动Stroop测试。
   - 调用`run1`函数执行Stroop测试。

6. **依赖项:**
   - 需要Python 3.x和Pygame库。

### `Settings.py`
这个模块定义了一个包含Pygame窗口参数的`settings`类，例如屏幕宽度和高度。

### `Functions.py`
这个模块包含在Stroop测试中使用的函数，包括：
   - `run1`：实现主要的Stroop测试逻辑。
   - `textshow`：在Pygame窗口上显示文本。

## 使用方法
1. 安装 Python 3.x。
2. 使用 `pip install pygame` 安装 Pygame库。
3. 运行 `Stroop.py` 脚本。

## Stroop测试流程
1. 参与者被要求按任意键开始Stroop测试。
2. 第一阶段将单词的背景颜色作为参考呈现。参与者在每个单词后按下空格键。
3. 完成第一阶段后，记录平均时间，并显示第二阶段的说明。
4. 第二阶段将单词的文本颜色作为参考。参与者再次在每个单词后按下空格键。
5. 完成后，记录第二阶段的平均时间。
6. 结果显示，实验结束。

