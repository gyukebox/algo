## Sorting HOWTO

### 1. 개노답 삼형제

- 버블 소트 (N ^ 2): 인접한거만 비교를해요
- 삽입 소트 (N ^ 2): 인덱스를 두개를 두면서, 적절한 위치에 꽂아요
- 선택 소트 (N ^ 2): 최솟값부터 찾아서 그냥 넣어요

### 2. 똑똑한 형제들

#### 퀵 소트 (N \* log N)

1. 아무거나 하나 뽑아요
2. ex) 18
3. 18 보다 작은거 왼쪽, 큰거 오른쪽

```
[[18 보다 작은거] 18 [18 보다 큰거]]
```

4. 이렇게 새로 나온 배열들에 대해서 무한반복

—> 분할 정복

#### 힙 소트 (N log N)

#### 머지 소트 (N \* log N)

1. 다 쪼개요
2. 부분 정렬해서 올려요

--> 분할 정복 (재귀)

### 3. 도박

#### 기수 소트 (Radix sort) (N ~ N^2)

—> 자릿수로 먼저 한다음 해요

#### 카운팅 소트 (N ~ N^2)