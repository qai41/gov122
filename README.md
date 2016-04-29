# [Gov122](http://azacai.com/scrapypa-qu-jia-shi-ren-kao-shi-yu-yue-ji-hua/)

2016年4月1日起,公安部令[第139号]开始实施，申请驾照的驾驶人驾照考试均在 `122.gov.cn` 网站自主网上预约。以河南省辖区三门峡市为例，网站每天公布10天左右的考试计划，[手动查询地址](http://ha.122.gov.cn/views/examplanpub.html)。同时考试预约结果公布[手动查询地址](http://ha.122.gov.cn/views/examappointpub.html)。现编写爬虫代码，批量查询。


## Table of contents

* [Quick start](#quick-start)


## Quick start

Several quick start options are available:

* 系统环境采用 Ubuntu 14.04 ，安装 Scrapy 使用官方发布的软件包：
```
1. $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
2. $ echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
3. $ sudo apt-get update && sudo apt-get install scrapy
4. 如果你要升级 Scrapy ，请重复步骤 3
```
* Clone the repo: `git clone https://github.com/qukaile/gov122.git`.
* `$ cd gov122`.
* 查询计划: `$ scrapy crawl gov122 --nolog`.
* 查询结果: `$ scrapy crawl gov122_result --nolog`.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
gov122/
├── gov122/
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│        ├── __init__.py
│        ├── result_spider.py
│        └── my_spider.py
├── LICENSE
├── README.md
└── scrapy.cfg
```
