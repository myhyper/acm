import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006.txt")
tc = int( f.readline() )
if debug: import time
#data_hash = [["000","083","830","061","064","072","079","006","500","583","610","642","649","720","791","794","007","835","836","837","838","008","050","005","726","727","728","507","508","550","055","561","564","572","579","056","057","615","616","617","618","058","505","506","725","556","557","558","555",],["000","083","830","836","837","838","005","006","007","008","050","061","064","072","079","500","583","610","642","649","720","791","794","835","505","506","507","508","550","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","555","556","557","558",],["000","083","830","005","006","007","008","050","061","064","072","079","500","583","610","642","649","720","791","794","835","836","837","838","550","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","505","506","507","508","555","556","557","558",],["000","083","830","005","006","007","008","050","061","064","072","079","500","583","610","642","649","720","791","794","835","836","837","838","055","056","057","058","505","506","507","508","550","561","564","572","579","615","616","617","618","725","726","727","728","555","556","557","558",],["200","283","910","942","949","205","206","207","208","250","261","264","272","279","915","916","917","918","255","256","257","258",],["000","083","830","005","006","007","008","050","061","064","072","079","500","583","610","642","649","720","791","794","835","836","837","838","505","506","507","508","550","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","556","557","558","555",],["100","183","420","491","494","105","106","107","108","150","161","164","172","179","425","426","427","428","155","156","157","158",],["200","283","910","942","949","205","206","207","208","250","261","264","272","279","915","916","917","918","255","256","257","258",],["300","383","305","306","307","308","350","361","364","372","379","355","356","357","358",],["100","183","420","491","494","105","106","107","108","150","161","164","172","179","425","426","427","428","155","156","157","158",]]
data_hash = [["830","083","000","005","050","008","838","837","836","835","007","720","610","583","500","006","061","064","072","079","642","649","791","794","506","505","550","508","507","726","727","728","055","561","564","572","579","056","057","615","616","617","618","058","725","556","557","558","555",],["830","083","000","835","720","610","583","500","050","008","007","006","005","838","837","836","061","064","072","079","642","649","791","794","550","508","507","506","505","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","555","556","557","558",],["830","083","000","838","837","836","835","720","610","583","500","050","008","007","006","005","061","064","072","079","642","649","791","794","508","507","506","505","550","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","555","556","557","558",],["830","083","000","838","837","836","835","720","610","583","500","050","008","007","006","005","061","064","072","079","642","649","791","794","550","508","507","506","505","055","056","057","058","561","564","572","579","615","616","617","618","725","726","727","728","555","556","557","558",],["910","283","200","942","949","250","208","207","206","205","261","264","272","279","915","916","917","918","255","256","257","258",],["830","083","000","838","837","836","835","720","610","583","500","050","008","007","006","005","061","064","072","079","642","649","791","794","550","508","507","506","505","561","564","572","579","615","616","617","618","725","726","727","728","055","056","057","058","556","557","558","555",],["420","183","100","491","494","150","108","107","106","105","161","164","172","179","425","426","427","428","155","156","157","158",],["910","283","200","942","949","250","208","207","206","205","261","264","272","279","915","916","917","918","255","256","257","258",],["383","300","350","308","307","306","305","361","364","372","379","355","356","357","358",],["420","183","100","491","494","150","108","107","106","105","161","164","172","179","425","426","427","428","155","156","157","158",]]
# a->b 로 가는 비용을 계산한다.
def get_val(idx):
    arr1 = [5,6,7,8]
    if idx in arr1: return 2
    if idx == 3: return 0
    return 1
# a->b 로 갈 수 있는지 체크 한다. (병력체크)
def check(a,b, idx):
    x = idx
    sx = idx-1
    dx = idx+1
    x += l
    sx += l
    dx += l
    x %= l
    sx %= l
    dx %= l

    up = w[0][x] + w[1][x] <= n
    up3 = w[0][dx] + w[1][dx] <= n
    left1 = w[0][sx] + w[0][x] <= n
    left2 = w[1][sx] + w[0][x] <= n
    right1 = w[0][dx] + w[0][x] <= n
    right2 = w[1][dx] + w[1][x] <= n
    if 0==a and not up: return False
    if 1==a and not left1: return False
    if 2==a and not left2: return False
    if 3==a and not (left1 and left2): return False
    if 4==a and not (left1 and right2): return False
    if 8==a and not (right1 and right2): return False
    if 9==a and not (left2 and right1): return False
        
    if 0==b and not up3: return False
    if 3==b and not (left1 and left2): return False
    if 6==b and not right1: return False
    if 7==b and not right2: return False
    if 8==b and not (right1 and right2): return False
    
    return True
    #return check_ab(a,b)
# 노드 관계에 의해 a->b 로 갈 수 있는지 체크 한다.
def check_ab(a,b):
    arr1 = [0,1,2,3,5]
    arr2 = [0,5,6,7,8]
    if a in arr1 and b in arr2:
        return True
    if 8 == a and 3 == b:
        return True
    if (4==a or 7==a) and (2==b or 9==b):
        return True
    if (6==a or 9==a) and (1==b or 4==b):
        return True
    return False

if debug: start_time = time.process_time()
for t in range(tc):
    ip = f.readline()
    if '\n' ==ip: ip = f.readline()
    l,n = map(int, ip.split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    if debug: cnt = 1
    ans = 0
    first = -1
    last = -1
    skip = 0
    ans_val = 0
    for i in range(l):
        if 0 < skip:
            skip -= 1
            continue
        if debug: cnt = 0
        if -1 is not last:
            bb = 5
            min_val = 9990999
            for j in range(len(data_hash[last])): # Hash table
                b = int(data_hash[last][j][0])
                c = int(data_hash[last][j][1])
                if i+1 == l:  # no dp version
                    if -1 != first and c != first: continue
                if check(last,b,i+0):
                    if check(b,c,i+1):
                        if debug: cnt += 1
                        #if i < l-1 and c == 0 or c == 3:
                        #    bb = c
                        #    skip = 1
                        #    ans+= get_val(b) + get_val(c)
                        #else:
                        #    bb = b
                        #    ans += get_val(b)
                        #break
                        val = get_val(last)+get_val(b)+get_val(c)
                        if val <min_val:
                            min_val = val
                            bb = b
            last = bb
            ans += get_val(bb)
        else:
            bb = 5
            min_val = 9990999
            for m in range(len(data_hash)):
                a = m
                for j in data_hash[m]: #node
                    b = int(j[0])
                    c = int(j[1])
                    if i+1 == l:  # no dp version
                        if -1 != first and c != first: continue
                    else:
                        if -1 != last and a != last: continue
                    if check(a,b,i+0) and \
                        check(b,c,i+1):
                        if debug: cnt += 1
                        val = get_val(a)+get_val(b)+get_val(c)
                        if val <min_val:
                            min_val = val
                            bb = b
            last = bb
            ans += get_val(bb)
            if first == -1: first = bb
    print(ans)
if debug:
    print(" {} seconds".format(time.process_time() - start_time))