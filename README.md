本仓库存放了《GRE 核心词汇考法精析》和《GRE 核心词汇助记与精练》两本电子书的 Anki 整合版卡组，以及将电子书转换为 Anki 卡组的 Python 源码，适合于希望快速通过 GRE 考试的同学们使用。版权归《GRE 核心词汇考法精析》系列书籍作者陈琦及其团队所有，本卡组仅供学习交流，不可用于任何商业目的。

要使用本卡组，你有两种选择：

# 简单粗暴版

从[微云分享链接](https://share.weiyun.com/5iSh6jY)下载整个卡组，导入 Anki 即可。该卡组包含完整的考法精析、助记和单词发音。

# 极客折腾版

如果你懂得一点 Python，你可以下载本仓库，定制属于自己的卡组。但是，出于上传压力，本仓库不包含从发音词典中获得的音频文件。如果你希望通过运行本仓库中的代码来获得自己的 Anki 卡组，那么你需要首先下载约 500 M 的[音频压缩文件](https://share.weiyun.com/5otF24v)，解压后将其中的所有音频文件移动到 `input/pron` 中。解压后文件数量约为 14 万个，因此需要较长时间（虽然我们只会用到其中的 2900 个左右）。

本仓库的文件结构为：

- `pretreat_word.py`：预处理《GRE 核心词汇考法精析》电子书（主要是修正一些错误）；
  - 输入文件：`input/word_raw.txt`
  - 输出文件：`input/word.txt`
- `pretreat_mnemo.py`：预处理《GRE 核心词汇助记与精练》电子书（同上）；
  - 输入文件：`input/mnemo_raw.txt`
  - 输出文件：`input/mnemo.txt`
- `convert_word.py`：将《GRE 核心词汇考法精析》解析为单词及其释意并保存为 `json` 文件；
  - 输入文件：`input/word.txt`
  - 输出文件：`input/word_json.txt`
- `convert_mnemo.py`：将《GRE 核心词汇助记与精练》解析为单词及其助记并保存为 `json` 文件；
  - 输入文件：`input/mnemo.txt`
  - 输出文件：`input/mnemo_json.txt`
- `generate_import.py`：将两份 `json` 文件中的键值对转化为 Anki 导入文本文件格式，并从 `input/pron` 中添加音频。
  - 输入文件：`input/word_json.txt`，`input/mnemo_json.txt`，`input/pron.dsl.dz`，`input/pron/*`
  - 输出文件：`output/anki_import.txt`，`output/audio/*`