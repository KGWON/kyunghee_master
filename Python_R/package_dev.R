if (!require("devtools")) install.packages("devtools") ; library(devtools)
if (!require("roxygen2")) install.packages("roxygen2") ;  library(roxygen2)

## working directory를 설정한다.
setwd("/Users/ku/googleDrive/development/nncrawl")

## package directory를 생성한다.
create("/Users/ku/googleDrive/development/nncrawl")

## working directory는 유지한 채로 ./R/ 하위에 패키지에 포함할 사용자 정의 함수들을 작성한다.

## document를 생성한다. (help() 함수를 사용했을 때 나오는 document에 관한 것.)
document()

## 개발한 로컬 패키지를 설치한다.
install(pkg="R")

## 패키지 로딩 및 테스트
library(nncrawl)