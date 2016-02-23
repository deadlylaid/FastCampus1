// SET legacy 방식
// first_child_of_body.id = 'document_page';
// first_child_of_body.className = 'wrapper';

//var first_child_of_body_id = first_child_of_body.getAttribute('id');
//var first_child_of_body_class = first_child_of_body.getAttribute('class');

// // qeurySelector, getAttribute 차이점
// // querySelector는 객체를 반환하고, getAttribute는 value

// console.log(first_child_of_body_id);
// console.log(first_child_of_body_class);

// // attribute를 변경 
// document.body.setAttribute('data-ng-app', 'MemoryGameApp');


// var body = document.body;
// var body = document.querySelector('.container');

// var body = selector('body');
// var divs = selector('div')
// console.log(body)

// addAttribute(body, 'data-module', 'dom-helper');
// addAttribute(body, 'class', 'hello');


// // Element 태그
// // attribute == Property, 속성 
// // Value 값
// // Selector id, class, tag

// //DOM은 HTML 문서를 여러 API를 사용할 수 있도록 하는 형태

// var divs = selector2('div');
// var page = selector2('.page');
// var page_in_divs = selector2('div', page);

//console.log(divs);
// console.log(page_in_divs);



//javascript 데이터유형
//객체(obeject)
//객체가 아닌것 -> undifined, null
	

//원시적인 데이터 종류
//Number - 실수 정수
// var num = new Number(9);//객체
// var num = 9;//리터럴

//String
// var str = new String('this is string obejct');//객체
// var str = 'this is string object';//리터럴

//Boolean
// var boo = new Boolean(false);//객체
// var boo = false;//리터럴

//복잡한 데이터 종류
//Function
// var fnc = function(){};

//Array
// var arr= [];
//var arr = new Array();->안티 패턴

//object는 모든것의 부모가 된다.
// var obj = {};

// 정규 표현식
// var reg = new RegExp('[a-z0-9]', 'ig');
// var reg = /[a-z0-9]ig/;

//Singleton 객체


//데이터 유형 체크
//1. typeof
// 약점 : 객체와 배열의 데이터 타입을 구분하지 못한다.

//2.instanceof
//데이터 유형 istansof 생성자 함수
//원시데이터의 유형을 체크할 수 없다.

