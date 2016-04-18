#-*-coding:utf8-*-
import scrapy
from scrapy.http import FormRequest	# 模拟HTML表单POST	
import json
import datetime			# python返回当天日期
from gov122.items import Gov122Item


class GovSpider(scrapy.spiders.Spider):
    name = "gov122"				# scrapy crawl gov122来启动爬虫
    allowed_domains = ["ha.122.gov.cn"]
    start_urls = ["http://ha.122.gov.cn/m/examplan/getExamPlanDetail"]
    

    def parse(self, response):
        url = "http://ha.122.gov.cn/m/examplan/getExamPlanDetail"
        
        #----python返回当天日期----#
        now = datetime.datetime.now()
        start_time = now.strftime("%Y-%m-%d")
        #----python返回当天日期----#

        # 列举了以下考场：1.三门峡考练考场科目一；2.渑池县车管所科目一考场；3.义马科目一考场；4.三门峡市交警支队科目二考场(隐藏)；
        # 5.三门峡科目二交通考场；6.三门峡科目二渑池车管所考场；7.三门峡渑池友谊考场；8.三门峡支队科目三小车考场； 9.三门峡渑池小车科目三考场；
        #10.三门峡科目二全顺考场C2；11.三门峡市交警支队科目四考场；12.三门峡科目二全顺考场B2；
        # 下面的FormRequest模拟查询三门峡考练考场科目一
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112101', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询渑池县车管所科目一考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112181', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询义马科目一考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112131', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡市交警支队科目二考场
        #yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112201', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse2)
        # 下面的FormRequest模拟查询三门峡科目二交通考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112208', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡科目二渑池车管所考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112211', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡渑池友谊考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '411210', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡支队科目三小车考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112302', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡渑池小车科目三考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112304', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡科目二全顺考场C2
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112207', 'kscx': 'C2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡市交警支队科目四考场
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '4112101', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)
        # 下面的FormRequest模拟查询三门峡科目二全顺考场B2
        yield FormRequest(url,formdata={'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112207', 'kscx': 'B2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'},callback=self.after_parse)


    def after_parse(self, response):
        sites = json.loads(response.body_as_unicode())	# 网站返回的是JSON数据，这句用来转换
        items = []
        for each in sites.get("data"):
            item = Gov122Item()
            kcmc = each.get("kcmc")		# 考场名称："三门峡市XXX考场"
            kscx = each.get("kscx")                 # 考试车型：C1/C2/B2
            kskm = each.get("kskm")             # 考试科目
            kkrs = each.get("kkrs")		# 考试计划人数
            kscc = each.get("kscc")		# 考试场次：上午/下午
            ksrq = each.get("ksrq")		# 考试日期：格式2016-05-20
            # 打印：三门峡市XXX考场C1----KeMu1----2016-04-11(上午)----400;
            print "%s%s----KeMu%s----%s(%s)----%s"%(kcmc,kscx,kskm,ksrq,kscc,kkrs)

            # 若要收集Item，将爬取结果保存到数据库或进行其他操作。增加以下代码，并参照Scrapy文档拓展功能
            #item["kcmc"] = each["kcmc"]        # 考场名称："三门峡市XXX考场"
            #item["kskm"] = each["kskm"]        # 考试科目
            #item["kscx"] = each["kscx"]        # 考试车型：C1/C2/B2
            #item["kkrs"] = each["kkrs"]        # 考试计划人数
            #item["kscc"] = each["kscc"]        # 考试场次：上午/下午
            #item["ksrq"] = each["ksrq"]        # 考试日期：格式2016-05-20
            #items.append(item)
        #return items