from ipaddress import ip_network
from pprint import pprint
import yaml

class CommReqExpand():

    def filters(self):
        return {
            'req_expand': self.CommReqExpand,
        }    

    def expand(self):
        with open('testcase.yml') as file:
            testcase = yaml.safe_load(file)['req_r_to_l']
        testcase_true =  [i for i in testcase if i['req'] in 'true']
        expanded_testcase = []

        for case in testcase_true:
            case1 = case.copy()
            case2 = case.copy()
            if '/' in case['src_ip_real']:
                case1.update( {'src_ip_real': format(list(ip_network(case['src_ip_real']).hosts())[0])} )
                case2.update( {'src_ip_real': format(list(ip_network(case['src_ip_real']).hosts())[-1])} )
            elif '/' in case['dst_ip_real']:
                case1.update( {'dst_ip_real': format(list(ip_network(case['src_ip_real']).hosts())[0])} )
                case2.update( {'dst_ip_real': format(list(ip_network(case['src_ip_real']).hosts())[-1])} )
            elif '-' in case['src_ip_real']:
                case1.update( {'src_ip_real': case['src_ip_real'].split('-')[0]} )
                case2.update( {'src_ip_real': case['src_ip_real'].split('-')[1]} )
            elif '-' in case['dst_ip_real']:
                case1.update( {'dst_ip_real': case['dst_ip_real'].split('-')[0]} )
                case2.update( {'dst_ip_real': case['dst_ip_real'].split('-')[1]} )
            else:
                expanded_testcase.append( case )  
                continue              
            expanded_testcase.append( case1 )
            expanded_testcase.append( case2 )
        return  expanded_testcase

pprint(CommReqExpand().expand())
