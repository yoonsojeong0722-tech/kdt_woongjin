# kdt-woongjin 

안녕하세요 저는 윤소정입니다.  


이건 고양이구요...
GIPHY 에서 가져왔어요. 
이미지 링크 삽입 방법. 

![](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NDFqNmxqb2M4N3pzZTNjdnF0aWNtb3dhcjNoMjR1bG05d29oZWRjcSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/UmnWEKDFoPmcZHmwFl/giphy.gif)

---
260106 화

깃허브 사용 목적은 협업, 충돌 방지, 트래킹 관리 

source 라는 개념도 깃과 같은 개념

Devops 
CI/CD - 배포 관련, 지속성

깃 유료 툴을 쓰기도 한다.

---

터미널에서 
open . 
실행하면 데스크탑이 열림

---
단축키
컨트롤(커맨드) s : 저장
커맨드 k + v : 안티그래비티에서 프리뷰 열기 

---
https://giphy.com/


혈당관리 클루코핏   

---

- API 개념
REST API 

- HTTP 메소드   
GET 방식:  조회
POST 방식:  생성
PUT 방식:  수정
DELETE 방식:  삭제     

---

공공데이터 파라미터 설명 확인 

![]()

토큰 개념: 최소한의 의미 단위  
비용 산정이 가능함

---
SUPABASE 

timestamp  사용법 
(now() at time zone 'utc') 에서   
'utc' 부분을 삭제하고 'Asia/Seoul'로 변경하면 한국 시간으로 변경됨

---
타임존.   
시간, 날짜 UTC.   
글로벌 회사면 특히.   
북미 일본 유럽   

---
구매전환율이 높은 것 
금액조건 없이 무료배송/ 무료배송 (금액 조건부 무료)

1. 지표이해  
구매전환율이란 웹사이트 방문자 중 실제 구매를 완료한 고객의 비율  
(구매 횟수 / 총 방문 수) x 100  
즉 방문 대비 구매한 횟수.눈팅만 하지 않고 바로바로 구매로 전환.  

당연히 무료배송이 높지 않을까   
왜냐하면 배송비라는 추가비용을 결제하지 않아도 되니까 구매에 대한 부담이 낮아서 구매 전환율이 높아질 것 같다. 

그런데 이게 다라면 너무 허전, 뻔한데. 
생각해볼 부분.   
배송비용 외에 다른 조건은 모두 동일한거겠지?  
 
 "구매전환"만 보면 그럴 것 같은데. 천원만 사도 무료배송이니까. 

 구매 횟수는 이용기간에 따라 달라짐. 
 신규 가입자보다 가입기간이 오래된 가입자의 구매횟구가 높겠지. 

 방문횟수도 마찬가지. 물론 절대적이진 않겠지만.   
 3년전 가입했으나 방문일은 10일, 그중 구매전환은 5회인 고객 A 
 1년전 가입했으나 방문일은 100일, 그중 구매전환은 20회인 고객 B   

 구매전환율 지표로만 보면 A: 50%, B: 20%    
 가입기간 대비라는 지표도 복합적으로 사용해야할 것 같음.   

 AB 테스트를 한다면 배송금액 외에 다른 조건은 모두 동일해야 함.

 1년전 가입, 방문일은 100일, 금액무관 무료배송, 구매전환 횟수 
 1년전 가입, 방문일 100일, 3만원 이상시 무료배송, 구매전환 횟수 

 ---

 오랜만에 DBeaver   
 user : 
 password : postgrespasswordyoon.sojeong0722

 connection test 굿 
 완료.   

 Supabase 연결 정보 수집

Supabase 대시보드에서 [Project Settings] → [Database] 이동    
Connection Info 섹션에서 다음 정보 확인:    
Host: db.xxxxx.supabase.co    
Port: 5432    
Database: postgres  
User: postgres  
Password: 프로젝트 생성 시 설정한 비밀번호 (분실 시 리셋 가능)  

연결 정보 입력:  
Host: Supabase에서 복사한 Host 주소  
Port: 5432  
Database: postgres  
Username: postgres  
Password: 본인의 Supabase DB 비밀번호  
Show all databases 체크 해제 (선택사항)  
Test Connection 버튼 클릭하여 연결 확인  

---

[1월 7일 수요일]

지하철 실시간 열차위치정보 API ENDPOINT
http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimePosition/0/5/1호선

---

요청인자
변수명	타입	변수설명	값설명
KEY	String(필수)	인증키	OpenAPI 에서 발급된 인증키
TYPE	String(필수)	요청파일타입	xml : xml, xml파일 : xmlf, 엑셀파일 : xls, json파일 : json
SERVICE	String(필수)	서비스명	realtimePosition
START_INDEX	INTEGER(필수)	요청시작위치	정수 입력 (페이징 시작번호 입니다 : 데이터 행 시작번호)
END_INDEX	INTEGER(필수)	요청종료위치	정수 입력 (페이징 끝번호 입니다 : 데이터 행 끝번호)
subwayNm	STRING(필수)	지하철호선명	지하철호선명
출력값
No	출력명	출력설명
공통	list_total_count	총 데이터 건수 (정상조회 시 출력됨)
공통	RESULT.CODE	요청결과 코드 (하단 메세지설명 참고)
공통	RESULT.MESSAGE	요청결과 메시지 (하단 메세지설명 참고)
1	subwayId	지하철호선ID
(1001:1호선, 1002:2호선, 1003:3호선, 1004:4호선, 1005:5호선 1006:6호선, 1007:7호선, 1008:8호선, 1009:9호선, 1063:경의중앙선, 1065:공항철도, 1067:경춘선, 1075:수인분당선 1077:신분당선, 1092:우이신설선, 1032:GTX-A)
2	subwayNm	지하철호선명
3	statnId	지하철역ID
4	statnNm	지하철역명
5	trainNo	열차번호
6	lastRecptnDt	최종수신날짜
7	recptnDt	최종수신시간
8	updnLine	상하행선구분
(0 : 상행/내선, 1 : 하행/외선)
9	statnTid	종착지하철역ID
10	statnTnm	종착지하철역명
11	trainSttus	열차상태구분
(0:진입 1:도착, 2:출발, 3:전역출발)
12	directAt	급행여부
(1:급행, 0:아님, 7:특급)
13	lstcarAt	막차여부
(1:막차, 0:아님)

----

해당 데이터를 HTTP REST API로 호출해서 Supabase(Postgres DB)에 입력하게 하려고 해.

적재하는데 필요한 정보가 무엇인지 알려주고, 데이터의 컬럼명도 직관적(e.g. updnLine -> updown_line)이고 해당 데이터로 할 수 있는 데이터분석 리스트와 각 리스트의 개별 목적에 맞게 자세하게 분석 프로젝트로 세우고 싶어. 데이터분석의 목적은 원할한 지하철 운행이 되는지 모니터링하고 싶어.

신규 내부 프로젝트로 폴더를 만들어서 구축해줘.