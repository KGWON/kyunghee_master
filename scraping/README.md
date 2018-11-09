# Scraping(crawling) with selenium

#### Implicit Wait *VS* Explicit Wait

- Implicit Wait: It will try lookup the element again and again for the specified amount of time before throwing an `NoSuchElementException` if the element could not have been found. It does **only** this and can't be forced into anything else - it waits for elements to show up.
- It is more extendible in the means that you can set it up to wait for **any condition** you might like. Usually, you can use some of the prebuilt [`ExpectedConditions`](http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/support/ui/ExpectedConditions.html) to wait for elements to become clickable, visible, invisible, etc., or just write your own condition that suits your needs.

```python
# 모든 태그가 존재 하는지 10초간 검사한다. 10초 이전에 모든 태그가 존재상태이면 다음 코드로 넘어가고 10초가 지나면 NoSuchElementException 에러를 발생시킨다.
driver.implicitly_wait(10)

# 특정 태그가 존재하는지 10초간 검사한다. 10초 이전에 발견되면 다음 코드로 넘어가고 10초가 지나면 NoSuchElementException 에러를 발생시킨다.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea#source")))
```



#### 제이쿼리를 이용하여 부모노드의 텍스트만 가져오기(자식 노드의 텍스트는 제외).

- http://www.joongboo.com/news/articleView.html?idxno=1275788

- 기사의 본문 내용을 긁어 오기 위해서 `$('#article-view-content-div').text()`를 한 결과 아래와 같은 결과를 얻었음. 자바스크립트 태그까지 긁혀서 나옴...

  > 가평군은 오는 10월 말까지 만 19세 이상 성인 900여 명을 대상으로 ‘2018년 지역사회 건강조사’를 실시한다.
  >  14일 군에 따르면 지역보건의료 계획 및 건강정책 수립에 필요한 건강통계 산출을 위해 실시하는 이번 조사는 한양대학교 산악협력단과 함께 무작위 표본 추출방식으로 선정된 표본가구를 직접 방문해 1:1 면접 방식으로 이뤄진다.
  >  건강조사에서는 흡연, 음주, 신체활동 등 건강행태와 예방접종여부, 의료이용, 사고 및 중독 등 200여 개의 설문문항을 조사할 예정이다.
  >  군 관계자는 “조사된 모든 내용은 건강도시 가평군의 보건의료사업을 시행하기 위한 기초자료로 지역주민의 건강수준 향상에 기여할 것”이라고 말했다.
  >  장학인기자 
  >
  > var from = document.referrer;
  > document.write("<iframe name='ifrnt' width='100%' height='70' id='ifrnt' src='http://www.dreamsearch.or.kr/servlet/adHashtag?from="+escape(from)+"&u=2012090332839&us=18372&s=19110' frameBorder='0' marginWidth='0' marginHeight='0' scrolling='no' ></iframe>");
  >
  >
  >
  >
  > ​		
  > ​	
  >
  > 저작권자 © 중부일보 무단전재 및 재배포 금지
  >
  >
  > ​		
  > ​			
  > ​				
  > ​											
  > ​									
  >
  > 장학인
  >
  >
  > ​		
  >
  > ​	
  > var from=document.referrer; document.write("<iframe name='ifrad' width='640' height='107' id='ifrad' src='http://www.dreamsearch.or.kr/servlet/adBanner?from="+escape(from)+"&u=2012090332839&us=18109&s=18862&iwh=640_107&igb=75&cntsr=3&cntad=1' frameBorder='0' marginWidth='0' marginHeight='0' scrolling='no' ></iframe>")

- 이를 해결하기 위해서는 아래와 같은 제이쿼리 문법 사용.

- `$('#article-view-content-div').contents().not($('#article-view-content-div').children()).text()`

- Rselenium 으로 하려면

- ```
  driver$execute()
  ```

- 

## Reference

[stack overflow - 묵시적 대기 vs 명시적 대기](https://stackoverflow.com/questions/11244697/difference-between-webdriver-wait-timeout-and-implicitlywait-timeout)