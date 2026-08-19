#5 IP访问日志分析
# 访问日志字符串
log = "192.168.1.100|/home|12; 10.0.0.55|/login|5; 192.168.1.100|/products|45; 172.16.3.20|/home|8; 10.0.0.55|/cart|33; 192.168.1.100|/login|7; 172.16.3.20|/products|29; 10.0.0.55|/home|6"

# IP黑名单判定规则列表
blacklist = {"10.0.0.55", "192.168.1.100", "10.7.0.9"}

#1.将log切割成列表
records = log.split("; ")
print(records)

#2.遍历收集IP地址到ip_list
ip_list = []
for i in records:
     ip=i.split("|")
     ip_list.append(ip[0])
print(ip_list)

#3.使用集合获取所有去重后的访问页面路径
home_list = []
for home in records:
    home_word = home.split("|")
    home_list.append(home_word[1])
print(set(home_list))

#4.从ip_list中筛选属于黑名单的ip，生成visited_black_ips
visited_black_ips = [ips for ips in ip_list if ips in blacklist]
print(set(visited_black_ips))

#5.计算黑名单IP的总访问次数
print(len(visited_black_ips))

#6.找出响应时间大于30ms的记录所在的页面路径
route_list = []
for path in records:
    path_list = path.split("|")
    if int(path_list[2]) > 30:
        route_list.append(path)
print(route_list)

