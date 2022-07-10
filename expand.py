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
            if '/' in case['src_ip_real']:
                expanded_testcase.append( case.update( {'src_ip_real': ip_network(case['src_ip_real'])[0]} ))
                expanded_testcase.append( case.update( {'src_ip_real': ip_network(case['src_ip_real'])[-1]} ))
                pprint('111111111111111111')
            elif '/' in case['dst_ip_real']:
                expanded_testcase.append( case.update( {'dst_ip_real': ip_network(case['dst_ip_real'])[0]}  ))
                expanded_testcase.append( case.update( {'dst_ip_real': ip_network(case['dst_ip_real'])[-1]} ))
                pprint('222222222222222222')
            elif '-' in case['src_ip_real']:
                expanded_testcase.append( case.update( {'src_ip_real': case['src_ip_real'].split('-')[0]} ))
                expanded_testcase.append( case.update( {'src_ip_real': case['src_ip_real'].split('-')[1]} ))    
                pprint('333333333333333333')
            elif '-' in case['dst_ip_real']:
                expanded_testcase.append( case.update( {'dst_ip_real': case['dst_ip_real'].split('-')[0]} ))
                expanded_testcase.append( case.update( {'dst_ip_real': case['dst_ip_real'].split('-')[1]} ))
                pprint('444444444444444444')
            else:
                expanded_testcase.append( case )                
                print('5555555555555555555')
        return  expanded_testcase

pprint(CommReqExpand().expand())
