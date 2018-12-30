# Css-master-class

## Css-Grid

grid가 필요한 이유

###### 테이블단위로 묶지 않고 작업할시

<img width="1020" alt="2018-12-30 4 20 19" src="https://user-images.githubusercontent.com/46123567/50541479-42a6ef00-0bea-11e9-85bd-88997c861870.png">

위의 이미지에서와 같이 새로운 열에 객체가 모자를때 뜻하지않은 모양의 레이아웃이 잡힐경우를 대비해서 grid가 생겨남



그리드에서는 행 열 속성을 지정 할 수 있다.

행 열 속성을 지정하는 방법은

```html
grid-template-columns: 크기;
grid-template-rows: 크기;

```

로 지정이 가능하다

객체사이의 거리는

~~~html
grid-gap: 크기;
~~~



로 지정이 가능하다



### Auto columns & Row

```html
grid-auto-row:
grid-auto-columns:
```

으로 지정가능하다

다른경우로

~~~html
grid-auto-flow:속성;
~~~

으로 지정 가능한데 이때 속성에 row 나 columns를 넣어 행 열 지정이 가능하다



### Grid-Template-Areas

~~~
grid-template-areas:"이름"
~~~

style에 이름을 지정 한 후 각각의 객체에

~~~
grid-area:이름;
~~~

을 넣어 매칭시키면 원하는 객체를 어디서든지 이름만 매칭시킨다면 해당객체를 원하는 영역에 주입이 가능하다

각각의속성들을 지정해주지 않아도 자동으로 위치를 맞추는 장점이 있다.



### fr & repeat

fr은 내부객체들이 상대적으로 자리를 차지하는것을 지정 해 줄 수 있다.

예를들어 4개의 객체를 columns를 지정할 때

~~~
grid-template-columns:1fr 2fr 1fr 2fr;
~~~

로 지정햇다면 2 , 4 번째 객체는 1 , 3 번째 객체보다 상대적으로 2배의크기를 가지게 된다.

알아둬야할점은 모든영역을 빈공간없이 사용한다라는 것이다.



빈공간을 지정하고싶다묜 repeat 함수를 사용하면 되는데

~~~
grid-template-columns:repeat(갯수,크기);
~~~

로 생성 후 객체의갯수를 입력된객체의 크기보다 많게한다면 그만큼 남는공간이 생성된다.



### Minimal , min-content , max-content

~~~
grid-template-columns:minmax:(최소&최대크기지정,객체크기);
~~~



반응형웹을 제작할때 전체창의 크기를키우거나 줄이더라도 일정한 크기 이상,이하로 줄어들거나 커지지 않도록 객체를 컨트롤할때 사용한다.

Max-content 는 해당객체가 원하는만큼 공간을 사용 할 수 있도록 지정해 주는 것이다 title같은것들에 주로 사용한다.

Min-content 는 가능한 작은공간을 사용하도록 지정해주는 것이다.

해당기능들을통해 margin 이나 padding등 공간을 지정해주는것들을 자동으로 해결하게 해준다.



### Auto-fill , Auto-fit

~~~html
grid-template-columns:repact(auto-fit,크기);
~~~

auto-fit은 지정된크기로 객체들을 채워나가는 것이다.

객체의 갯수를 지정해주지 않아도 선택된크기되로 설정된 공간내부를 채워나가는 것이다.

객체의 횟수를지정해주지 않아도 채워나갈수있는장점이있다.

가능한 많이 채워라는뜻으로 해석 할 수있다.

크기는 minmax로 지정해주는것이 좋다



Auto-fill은 만들어둔 객체로 해당영역을 채워나가는것이 아니라 공간이 남는다면 가상의 객체로 남는공간을 채워넣는다는 차이점이 있다.



### Justify-content & Align-content & Place-content

Justify-content 는 grid 전체를 행 이동시킨다.

Align-content 는 전체를 열 이동시킨다

Place-content는 첫번째속성은 align , 두번째속성은 Justift속성을가진다 즉 동시에 행 열을 조절 할 수있다.

State , conter ,end 속성이 있다.



### Justify-items & Align-items & Place-items

gird를 이동시키는것이 아니라 객체의 위치는 그대로 두며 내부의 아이탬위치를 이동시키는 것이다

위의 content와 비슷하게 사용 할 수 있다.



### Grid start & end

객체의 시작과 끝을 지정해준다 네이밍을지정해주면 네이밍에따라서도 사용이 가능하다 *모든객체가 그럴것이라 예상

~~~
grid-row-start:시작장소;
grid-row-end:끝장소;
grid-row:시작장소 / 끝장소;    <이러케도가능
*-1은 제일 끝부분
~~~

위의형식으로 사용이 가능하다.



### Grid-area

아이템의 시작행,열 끝 행,열을 지정해 아이템의 크기를 지정 가능

spen 을 사용해 영역지정도 가능



### Self

Justify , Align , Place 에 사용 가능하며

개개인의 아이템에만 명령영역을 지정한다

다시말하면 자기자신에게만 크기 및 위치를 지정한다.

















