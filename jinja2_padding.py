from jinja2 import Template

tmp_s = 'IP is {{"%20s" % ip_addr1}}{{"%20s" % ip_addr2}}'
template = Template(tmp_s)
res = template.render(ip_addr1='10.0.0.1', ip_addr2='20.0.0.1')
print(res)