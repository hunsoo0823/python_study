import asyncio
import time
from urllib.request import urlopen

URL_LIST = ["https://google.com" for _ in range(1,100+1)]

#async지만 내부가 block인 경우
async def url_request(url): #비동기 함수를 만들기 위해선 async def를 사용
    res = urlopen(url)
    return res.status

async def main():
    futures = [asyncio.ensure_future(url_request(url))for url in URL_LIST] # async에서 사용되는 객체를 만듬
    result = await asyncio.gather(*futures) # 모든 async가 끝날때 까지 기다림
    result_len = len(result)
    success_count = result.count(200)
    print("상태 변환 리스트 갯수: {}".format(result_len))
    print("요청 성공 : {}".format(success_count))
    print("요청 실패 : {}".format(result_len - success_count))

start_ = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end_ = time.time()
print("걸린 시간 : {}".format(end_ - start_))