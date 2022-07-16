# 辞書のリストを基に新しい辞書のリストを作る。固定値も入れられるパターン
from pprint import pprint
import yaml

class CommReqExpand():

    new_key_value = [
        {
            'key': 'inside_local',
            'fixed_value': 'src_ip_real',
        },
        {
            'key': 'inside_global',
            'value': 'src_ip_public',
        },
        {
            'key': 'outside_local',
            'value': 'dst_ip_public',
        },
        {
            'key': 'outside_global',
            'value': 'dst_ip_real',
        },
    ]
    
    def filters(self):
        return {
            'new_dict': self.CommReqExpand,
        }    

    def new_dict(self):
        with open('testcase_new_dict.yml') as file:
            testcase = yaml.safe_load(file)['req_r_to_l']
        testcase_true =  [i for i in testcase if i['req'] in 'true']
        new_key_testcase = []
            
        for case in testcase_true:
            _dict = {}
            for i in self.new_key_value:
                if 'fixed_value' in i:
                    _dict.update( {i['key']: i['fixed_value'] } )
                else:
                    _dict.update( {i['key']: case[i['value']] } )                    
            new_key_testcase.append(_dict)  
        return new_key_testcase

pprint(CommReqExpand().new_dict())