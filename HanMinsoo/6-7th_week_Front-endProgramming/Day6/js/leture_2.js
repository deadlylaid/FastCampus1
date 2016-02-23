//Javascirpt기본 문법 정리
//클라이언트환경에서 문서의 접근/조작/처리 과정 실습
//문서에 존재하는 대상(요소)를 선택합니다.
//선택된 대상에 조작을 가하거나 이벤트에 따라 프로그래밍 되도록 설계합니다.

//Variable 변수 - var
//$,@
//var html, head, body;

//변수 선언
var html;
var head;
var body;

//Legacy DOM == DOM lever 0 구식코드
//변수에 값을 할당(여기서 값이란 문서 객체를 말한다.)
// html = document.documentElement;
// head = document.head;
// body = document.body;

//Dom level 1 더 나중에 나온 코드
// html = document.getElementsByTagName('html');
// head = document.getElementsByTagName('head');
// body = document.getElementsByTagName('body');

// console.log('html' , html.item(0));
// console.log('head', head);
// console.log('body', body);


// var all_div = document.getElementsByTagName('div');
// console.log(all_div.length);



//배열 데이터 유형이가진 메소드
//.push(), .shift(),
//console.log(!all_div.push);




//Html 요소의 속성으로 대상을 식별하는 메소드
// var page = document.getElementById('page');
// var header = document.getElementById('header');
// var footer = document.getElementById('footer');
// console.log(page, navigation, footer);



//class속성을 선택하는 방법
// var container = document.getElementsByClassName('container');
// console.log(container[0]);



//DOM Selection API
// var page = document.querySelector('#page');
// var container = document.querySelector('.container');
// var page_title = page.querySelector('.page_title');
// var page_title = document.querySelector('#page .page_title');



//클래스던 ID던 상관없이 선택하는 방법 qeryselector를 쓰자
// var divs = document.querySelector('div');
// console.log(divs);

/*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
*(선택자를 이용해서) 선택 후, 조작
*생성
*제거
*변경
*복사
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*/

// var first_child_of_body = document.body.querySelector(':first_child_of_body');
var first_child_of_body = document.body.querySelector('body *:first-child');
// console.log(first_child_of_body);

console.log(first_child_of_body.id);

/*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
console.log(first_child_of_body.class);
class는 예약어이기 때문에 
class를 불러오고 싶다면 className을 써야한다.
GET할 때는
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*/
// console.log(first_child_of_body.className);


// //SET
// first_child_of_body.id= 'document_page';
// first_child_of_body.className = 'wrapper';

var first_child_of_body_id = first_child_of_body.getAttribute('id');
var first_child_of_body_class= first_child_of_body.getAttribute('class');

// console.log(first_child_of_body_id);
// console.log(first_child_of_body_class);


var app_name = document.body.getAttribute('data-ng-app');
console.log(app_name);

document.body.setAttribute('data-ng-app', 'MemoryGameApp');

var page = document.querySelector('.page container');
console.log(page);