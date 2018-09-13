# Scraping(crawling) with python selenium

#### Implicit Wait *VS* Explicit Wait

- Implicit Wait: It will try lookup the element again and again for the specified amount of time before throwing an `NoSuchElementException` if the element could not have been found. It does **only** this and can't be forced into anything else - it waits for elements to show up.
- It is more extendible in the means that you can set it up to wait for **any condition** you might like. Usually, you can use some of the prebuilt [`ExpectedConditions`](http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/support/ui/ExpectedConditions.html) to wait for elements to become clickable, visible, invisible, etc., or just write your own condition that suits your needs.

```python
# 모든 태그가 존재 하는지 10초간 검사한다. 10초 이전에 모든 태그가 존재상태이면 다음 코드로 넘어가고 10초가 지나면 NoSuchElementException 에러를 발생시킨다.
driver.implicitly_wait(10)

# 특정 태그가 존재하는지 10초간 검사한다. 10초 이전에 발견되면 다음 코드로 넘어가고 10초가 지나면 NoSuchElementException 에러를 발생시킨다.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea#source")))
```





## Reference

[stack overflow - 묵시적 대기 vs 명시적 대기](https://stackoverflow.com/questions/11244697/difference-between-webdriver-wait-timeout-and-implicitlywait-timeout)