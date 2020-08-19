import time
from urllib.request import urlopen

URL_LIST = ["https://google.com" for _ in range(1,100+1)]

def main():
    result = []
    for url in URL_LIST:
        res = urlopen(url) # URL_LIST에 들어있는 url에 요청을 보냄
        result.append(res.status) # 요청 결과를 result_list append
    result_len = len(result) #result list 의 길이
    success_count = result.count(200) #status 200의 갯수 카운
    print("상태 변환 리스트 갯수 : {} ".format(result_len))
    print("요청 성공 : {}".format(success_count))
    print("요청 실패 : {}".format(result_len - success_count))

start_ = time.time()
main()
end_ = time.time()
print("걸린 시간 : {}".format(end_ - start_))