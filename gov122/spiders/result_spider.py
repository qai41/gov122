#-*-coding:utf8-*-
import scrapy
from scrapy.http import FormRequest # 模拟HTML表单POST  
import simplejson
import datetime         # python返回当天日期
from gov122.items import ResultItem


class ResultSpider(scrapy.spiders.Spider):
    name = "gov122_result"             # scrapy crawl gov122_result 来启动爬虫
    allowed_domains = ["ha.122.gov.cn"]
    start_urls = ["http://ha.122.gov.cn/m/examplan/getExamPlanResult"]
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Referer": "http://ha.122.gov.cn/views/examplanpub.html"
    }
    

    def parse(self, response):
        url="http://ha.122.gov.cn/m/examplan/getExamPlanResult"
        global items
        items = []

        #----python返回当天日期----#
        now = datetime.datetime.now()
        start_time = now.strftime("%Y-%m-%d")
        #----python返回当天日期----#

        smx_result_formdata = []
        # 增加考场的函数
        def add_result_formdata(self):
                smx_result_formdata.append(self)
                return smx_result_formdata

        # 科目一
        #result_formdata_1 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        #add_result_formdata(result_formdata_1)
        result_formdata_1_b = {'page': '1', 'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_1_b)
        result_formdata_1_c = {'page': '2', 'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_1_c)
        result_formdata_1_d = {'page': '3', 'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_1_d)
        # 科目二C1
        #result_formdata_2_c1 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        #add_result_formdata(result_formdata_2_c1)
        result_formdata_2_c1_b = {'page': '1', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_2_c1_b)
        result_formdata_2_c1_c = {'page': '2', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_2_c1_c)
        result_formdata_2_c1_d = {'page': '3', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_2_c1_d)
        # 科目二b2
        result_formdata_2_b2 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'B2','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_2_b2)
        # 科目二c2
        result_formdata_2_c2 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '', 'kscx': 'C2','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_2_c2)
        # 科目三b2
        result_formdata_3_b2 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'B2','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_3_b2)
        # 科目三c1
        #result_formdata_3_c1 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        #add_result_formdata(result_formdata_3_c1)
        result_formdata_3_c1_b = {'page': '1', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_3_c1_b)
        result_formdata_3_c1_c = {'page': '2', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_3_c1_c)
        result_formdata_3_c1_d = {'page': '3', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_3_c1_d)
        # 科目三c2
        result_formdata_3_c2 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '', 'kscx': 'C2','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_3_c2)
        # 科目四
        #result_formdata_4 = {'page': '0', 'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        #add_result_formdata(result_formdata_4)
        result_formdata_4_b = {'page': '1', 'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_4_b)
        result_formdata_4_c = {'page': '2', 'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_4_c)
        result_formdata_4_d = {'page': '3', 'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '2'}
        add_result_formdata(result_formdata_4_d)

        # 遍历所有
        for each in smx_result_formdata:
            yield FormRequest(url,formdata=each,callback=self.after_parse2)


    def after_parse2(self, response):
        sites = simplejson.loads(response.body)                 # 转换成字典
        result_sites = sites.get("data")

        for each in result_sites.get("content"):
            item = ResultItem()
            item["kcmc"] = each["kcmc"]        # 考场名称："三门峡市XXX考场"
            item["ksdd"] = each["ksdd"]        # 考场名称：kcdd
            item["kscx"] = each["kscx"]        # 考试车型：C1/C2/B2
            item["kscc"] = each["kscc"]        # 考试场次：上午/下午
            item["kskm"] = each["kskm"]        # 考试科目
            item["ksrq"] = each["ksrq"]        # 考试日期：格式2016-05-20
            item["xh"] = each["xh"]            # xh 用于后续生成查询学员列表的网址
            item["ztStr"] = each["ztStr"]      # 51/120公布的人数

            # 打印需要的考场公布信息{4112101:三门峡市交警支队科目四考场, 4112181:渑池县车管所科目一考场, 4112131:义马科目一考场, 4112208:三门峡科目二交通考场, 4112211:三门峡科目二渑池车管所考场, 411210:三门峡渑池友谊考场, 4112302:三门峡支队科目三小车考场, 4112304:三门峡渑池小车科目三考场, 4112207:三门峡科目二全顺考场B2C2}
            the_list = ['4112101', '4112181', '4112131', '4112208', '4112211', '411210', '4112302', '4112304', '4112207']
            if each["ksdd"] in the_list:
                print "|%s|%s|%s|%s| %s"%(format((u'\u79d1\u76ee'+each["kskm"]), '^5'), format((each["ksrq"]+'('+each["kscc"])+')', '^16'), 
                                    format((each["ztStr"]+u'\u4eba'), '^10'), format(u'\u5df2\u516c\u5e03', '^4'), (each["kcmc"]+each["kscx"]))
                # 打印：三门峡市XXX考场C1----科目1----2016-04-11(上午)----395/400人----已公布
                #print "%s%s----%s%s----%s(%s)----%s%s----%s"%(each["kcmc"],each["kscx"],u'\u79d1\u76ee',each["kskm"],each["ksrq"],each["kscc"],each["ztStr"],u'\u4eba',u'\u5df2\u516c\u5e03')
            items.append(item)
        return items
