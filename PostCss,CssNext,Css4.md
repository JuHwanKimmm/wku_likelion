# Css-master-class

## PostCss , CssNext , Css4



### parcel

parcel 홈페이지에서 보고 설정해야함



서버열때 오류있으면 서버아예안열림

npm init -y    로 nodejs파일 인스톨하고

스크립트작성한다

css파일 링크해주고

~~~
npm run 스크립트이름
*터미널에서
~~~

실행해주면 서버열리고 주소나온다.



### Post css

https://preset-env.cssdb.org/

css사용시 다양한 기능 제공

~~~
npm install postcss-preset-env
~~~

명령어로 설치

설치후 js파일에서 객체를 사용할지를 설정해주어야 한다.

~~~
 "postcss":{
    "plugins":{
      "postcss-preset-env":{
        "stage":0
      }
    }
  }
~~~

를 추가하여 사용할스테이지를 설정한다.



테스트소스를 붙여놓고 확인한다ㄱ 끗



### CSS Variables & cuntum-selector

##### Variables

css에서 미리 지정해두고 다른곳에서 호출 할 수 있게 해준다.

상위디렉토리에 미리 지정해두고 다른곳에서 호출해서 쓴다

색깔 스타일 폰트 등 다양하게 쓸수잇다

*미리지정해서 매번 색깔,폰트등의속성을 불러내서 사용하는것

~~~html
:root{
    --변수:속성;
}
*으로 지정하고

var(--변수);
*로 사용한다
~~~

##### Custom-selector

변수들을지정해서 원하는변수들을 통채로 바꾼다

~~~html
@costum-selector:--변수 아이템,아이템;
	*으로 생성하고

:--변수{
    변경할요소
}
*사용한다
~~~



### Custom-media & media query ranges

윈도우의 크기가 특정영역안에 진입하게되면 지정된설정대로 바뀌도록 설정 할 수 있다.

~~~
@custom-media --변수(진입영역);   *이부분에서 논리연산자로 원하는영역 설정가능
	*으로 지정하고
@medio (--변수){
    원하는설정;
}
	*으로 사용한다
	
~~~



### Color-mod

색상선택시 상대적인 색상을 지정 할 수 있다.

~~~
color-mod(색상 속성(정도%));

~~~

속성으로는 

hue , saturation , lightness , whiteness , blackness 가 있다.



gray는

~~~
gray(정도)
~~~

로 사용한다 왜쓰는지는모르겟다.



System-ui.   ?



### Nesting Rules

<img width="432" alt="2018-12-31 6 41 15" src="https://user-images.githubusercontent.com/46123567/50551614-2036d380-0cc7-11e9-8d92-002f65ed1962.png">



css에서는 하위로 내려가면서 상세속성을 지정해 줄 수 있다.

세부적으로 지정하는것이 다른조건보다 더 상위조건을 가진다는점을 기억해야한다.







사용싸이트정리

www.Flexbodfroggy.com flex box 연습

www.cssgridgarden.com css연습

www.flatuicolors.com 색깔추출

