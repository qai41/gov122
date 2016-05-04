#-*-coding:utf8-*-
import scrapy
from scrapy.http import FormRequest # 模拟HTML表单POST  
import simplejson
import datetime         # python返回当天日期
from gov122.items import Gov122Item


class GovSpider(scrapy.spiders.Spider):
    name = "gov122"             # scrapy crawl gov122来启动爬虫
    allowed_domains = ["ha.122.gov.cn"]
    start_urls = ["http://ha.122.gov.cn/m/examplan/getExamPlanDetail"]
    

    def parse(self, response):
        url = "http://ha.122.gov.cn/m/examplan/getExamPlanDetail"
        global items
        items = []
        
        #----python返回当天日期----#
        now = datetime.datetime.now()
        start_time = now.strftime("%Y-%m-%d")
        #----python返回当天日期----#

        smx_formdata = []
        # 增加考场的函数
        def add_formdata(self):
        	smx_formdata.append(self)
        	return smx_formdata

        # 列举了以下考场：1.三门峡考练考场科目一；2.渑池县车管所科目一考场；3.义马科目一考场；4.三门峡市交警支队科目二考场(隐藏)；
        # 5.三门峡科目二交通考场；6.三门峡科目二渑池车管所考场；7.三门峡渑池友谊考场；8.三门峡支队科目三小车考场； 9.三门峡渑池小车科目三考场；
        #10.三门峡科目二全顺考场C2；11.三门峡市交警支队科目四考场；12.三门峡科目二全顺考场B2；13.三门峡B2科目三；14.三门峡C2科目三。
        # 下面2行增加查询三门峡考练考场科目一
        kao_lian_1 = {'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112101', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(kao_lian_1)
        # 渑池县车管所科目一考场
        mian_chi_1 = {'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112181', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(mian_chi_1)
        # 义马科目一考场
        yi_ma_1 = {'fzjg': '%E8%B1%ABM', 'kskm': '1','ksdd': '4112131', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(yi_ma_1)
        # 三门峡市交警支队科目二考场
        #kao_lian_2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112201', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        #add_formdata(kao_lian_2)
        # 三门峡科目二交通考场
        jiao_tong_2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112208', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(jiao_tong_2)
        # 三门峡科目二渑池车管所考场
        mian_chi_2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112211', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(mian_chi_2)
        # 三门峡渑池友谊考场
        you_yi_2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '411210', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(you_yi_2)
        # 三门峡支队科目三小车考场
        kao_lian_3 = {'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112302', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(kao_lian_3)
        # 三门峡渑池小车科目三考场
        mian_chi_3 = {'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112304', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(mian_chi_3)
        # 三门峡科目二全顺考场C2
        quan_shun_c2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112207', 'kscx': 'C2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(quan_shun_c2)
        # 三门峡市交警支队科目四考场
        kao_lian_4 = {'fzjg': '%E8%B1%ABM', 'kskm': '4','ksdd': '4112101', 'kscx': 'C1','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(kao_lian_4)
        # 三门峡科目二全顺考场B2
        quan_shun_b2 = {'fzjg': '%E8%B1%ABM', 'kskm': '2','ksdd': '4112207', 'kscx': 'B2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(quan_shun_b2)
        # 三门峡B2科目三
        kao_lian_b2_3 = {'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112312', 'kscx': 'B2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(kao_lian_b2_3)
        # 三门峡C2科目三
        kao_lian_c2_3 = {'fzjg': '%E8%B1%ABM', 'kskm': '3','ksdd': '4112302', 'kscx': 'C2','startTime': start_time, 'endTime': '2116-06-03','zt': '0'}
        add_formdata(kao_lian_c2_3)

        # 遍历所有考场
        for each in smx_formdata:
            yield FormRequest(url,formdata=each,callback=self.after_parse)


    def after_parse(self, response):
        sites = simplejson.loads(response.body)                 # 转换成字典
        
        for each in sites.get("data"):
            item = Gov122Item()
            item["kcmc"] = each["kcmc"]        # 考场名称："三门峡市XXX考场"
            item["kskm"] = each["kskm"]        # 考试科目
            item["kscx"] = each["kscx"]        # 考试车型：C1/C2/B2
            item["kkrs"] = each["kkrs"]        # 考试计划人数
            item["kscc"] = each["kscc"]        # 考试场次：上午/下午
            item["ksrq"] = each["ksrq"]        # 考试日期：格式2016-05-20
            # 打印：三门峡市XXX考场C1----科目1----2016-04-11(上午)----400人
            print "%s%s----%s%s----%s(%s)----%s%s"%(each["kcmc"],each["kscx"],u'\u79d1\u76ee',each["kskm"],each["ksrq"],each["kscc"],each["kkrs"],u'\u4eba')
            items.append(item)
        return items
