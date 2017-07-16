stat = dict()
with open('access.log') as f:
       for line in f:
            a = line.split(" ")
            if len(a) > 0:
                ip = a[0]
                stat[ip] = stat.get(ip, 0) + 1
print (sorted(stat.items(), key=lambda x:x[1], reverse=True)[:10])
