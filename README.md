Welcome to SPCC
====

![python](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10-blue)

文件结构
----

- `src` 源码
  - `setup.py`
  - `test.py`
  - `spcc`
    - `__init__.py`
    - `operations.py`
- `docs` 算法文档
- `tests` 单元测试
- `.gitignore` 忽略文件
- `.github/workflow` 工作流文件
  - `markdownlint.yml` markdown语法检查
  - `pylint.yml` python语法检查

文档格式
----

- 文档采用Markdown格式编写，以“Github Flavored Markdown （GFM）”为格式标准。参考指南：
  1. [指南](https://www.markdownguide.org/)
  2. [指南中译](https://www.markdown.xyz/)
  3. [GFM语法标准](https://github.github.com/gfm/)
- 本项目关于Markdown格式的约定
  - 使用SETEXT风格的标题格式，即

  ```markdown
  一级标题
  ========
  
  二级标题
  --------
  ```

  - 使用LaTeX风格的数学公式格式，即

  ```markdown
  内联公式（inline math） $\hat{C}_{pk}$ 
  
  段落公式（display math）
  
  \[f(x) = ax + b\]
  ```

  - 无编号列表只使用“-”标识，即

  ```markdown
  - 列表项1
  - 列表项2
    - 二级列表项
      - 三级列表项
  ```

  - 段落代码使用“```”标识，不使用缩进标识，需要标明语言，即
  
  ````markdown
  ```python
  print("hello world")
  ```
  ````
  
  - 使用“*”作为强调，即
  
  ```markdown
  正常文字， **加粗** 文字， *斜体* 文字
  ```

  - 如果没有特殊原因，不使用制表符（tab），不使用原始HTML代码。
- Markdown编辑工具使用[VisualStudio Code编辑器](https://code.visualstudio.com/download),安装以下插件：
  - 预览工具：Markdown Preview Enhanced
  - 快捷操作：Markdown All in One
  - 格式检查：markdownlint
- VisualStudio Code编辑器使用教程
  - [VisualStudio Code](https://code.visualstudio.com/docs/languages/markdown)
  - [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)
  - [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown)
  - [markdownlint](https://github.com/DavidAnson/vscode-markdownlint)
- 所编写文档，应通过[markdownlint](https://github.com/DavidAnson/vscode-markdownlint)的格式检查
