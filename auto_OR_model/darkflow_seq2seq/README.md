## 논문컨셉

- YOLO + seq2seq + OR model
  - YOLO를 통해 이미지의 객체를 탐지한 후 그 결과를 seq2seq 모델에 인풋시켜 원하는 sentence를 생성
  - sentence를 이용하여 이미지에 가장 적합한 OR model을 추천하고 최적의 해를 찾는 기능을 자동화하여 엑셀파일로 출력
    

## Implement TODO

- [x] seq2seq 모델 구현
- [ ] darkflow(YOLO v2의 텐서플로우 버전)의 결과를 seq2seq 모델에 인풋시키는 코드 구현
- [ ] seq2seq 모델의 출력 문장을 통해 적합한 OR 모델을 제시 (교수님 부분)
- [ ] seq2seq 모델의 출력 문장을 query로 하여 DB에서 관련 수치를 꺼낸 후 수송모델의 틀을 짜는 코드 구현

