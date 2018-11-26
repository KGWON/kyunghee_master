## 1. 전방탐색(lookahead)

*참고) 여기서 전방은 '==>' 방향을 말함.*



#### 긍정전방탐색(positive lookahead)

 `(?=찾으려는문자열)맞을때소비할문자열`

매 문자열(string)마다 바로 **뒤**의 문자열이 찾으려는 문자열이 **맞는지(TRUE)** 검증하고, 만약 맞으면(TRUE) 찾으려는 문자열을 매치시키고 틀리면(FALSE) 다음 문자열로 넘어가면서 하위문자열을 소비(consume)하는 방법.



예문:

> http://www.naver.com
> https://www.regexp.tutorial.kgwon
> ftp://abc.de

정규표현식:

> (?=:).+

결과:

<img src="./miscellaneous/긍정전방탐색.png" width="60%" height="60%">



### 부정전방탐색(negatie lookahead)

`(?!찾으려는문자열)아닐때소비할문자열`

매 문자열(string)마다 바로 **뒤**의 문자열이 찾으려는 문자열이 **아닌지(FALSE)** 검증하고, 만약 아니면(FALSE) 찾으려는 문자열을 매치시키고 맞으면(TRUE) 다음 문자열로 넘어가면서 하위문자열을 소비(consume)하는 방법.



예문:

> http://www.naver.com
> https://www.regexp.tutorial.kgwon
> ftp://abc.def



정규표현식:

> (?!:).



결과:

<img src="./miscellaneous/부정전방탐색.png" width="60%" height="60%">



## 2. 후방탐색(lookbehind)

*참고) 여기서 후방은 '<=='* 방향을 말함.



#### 긍정후방탐색(positive lookbehind)

`(?<=찾으려는문자열)맞을때소비할문자열`

매 문자열(string)마다 바로 **앞**의 문자열이 찾으려는 문자열이 **맞는지(TRUE)** 검증하고, 만약 맞으면(TRUE) 찾으려는 문자열을 매치시키고 틀리면(FALSE) 다음 문자열로 넘어가면서 하위문자열을 소비(consume)하는 방법.



예문:

> http://www.naver.com
> https://www.regexp.tutorial.kgwon
> ftp://abc.de

정규표현식:

> (?<=:).+

결과:

<img src="./miscellaneous/긍정후방탐색.png" width="60%" height="60%">



#### 부정후방탐색(negative lookbehind)

`(?<!찾으려는문자열)아닐때소비할문자열`

매 문자열(string)마다 바로 **앞**의 문자열이 찾으려는 문자열이 **아닌지(FALSE)** 검증하고, 만약 아니면(FALSE) 찾으려는 문자열을 매치시키고 맞으면(TRUE) 다음 문자열로 넘어가면서 하위문자열을 소비(consume)하는 방법.



예문:

> http://www.naver.com
> https://www.regexp.tutorial.kgwon
> ftp://abc.de

정규표현식:

> (?<!:).+

결과:

<img src="./miscellaneous/부정후방탐색.png" width="60%" height="60%">





## 레퍼런스

[전방탐색과 후방탐색](http://minsone.github.io/regex/regexp-lookaround)

[regex101.com](https://regex101.com/)

