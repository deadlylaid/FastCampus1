var body = document.body,
toogle_grid_btn = document.createElement('a');
	
// toogle_grid_btn.setAttribute('class','button toggle-grid fa fa-bars');
// toogle_grid_btn.setAttribute('href','#');
// toogle_grid_btn.setAttribute('role','button');
// toogle_grid_btn.setAttribute('aria-label','toggle Grid');


attr(toogle_grid_btn, 'class', 'button toggle-grid fa fa-bars');

body.appendChild(toogle_grid_btn);

//속성을 설정하는데 도움을 주는 헬퍼 함수 attr()
function attr(el, prop, value){
	//유효성 검사
	//전달받은 각각의 인자 데이터 유형이 올바른지 검수
	if(!el || el.nodeType!==1){
		throw new Error('첫번째 전달 인자는 요소노드여야 합니다.');
	}
	if (!isType(prop, 'string')){
		throw new Error('두번째 전달 인자는 문자데이터 유형이여야 합니다.');
	}

	if(value){
		//SET
		el.setAttribute(prop, value);
	}else{//GET
		return el.getAttribute(prop);
	}


}

window.$ = selector;


//list a 요소를 클릭했을때
//각 목록 아이템의 앵커를 사용자가 클릭하면
//콘솔 패널에 각 아이템 인덱스를 출력
//문서객체에 새로운 속성(index)을 설정하여 값을 기억하는 방법
// var list = $('list'),
// list_links = $('a',list);

// console.log(list_links.length); // HTML Collection, Nodelist

// var i =0;

// for(i = 0 ; i<list_links.length; i++){
// 	item =list_links[i];//<a href ='#'>item-i</a>
// 	item.index = i;//a 객체 안에다가 인덱스 요소를 추가합니다.
// 	list_links[i].onclick=function(){
// 		console.log('this', this.index);//0~7??
// 		return false; //a태그의 기본동작을 차단함.
// 	};
// };

var list = $('list'),
list_links = $('a',list);

console.log(list_links.length); // HTML Collection, Nodelist

var i =0;

for(i = 0 ; i<list_links.length; i++){
	list_links[i].onclick = (function(index){
		return function(){
			console.log(this, index);
			return false;
		};
	})(i);
}

function outer(){
	var i =0;
	function inner(){
		return ++i;
	}
	return inner;
}

//(function(){  })(); -> function함수를 웹브라우저 동장과 동시에 실행한다. 
var counter = (function(){
	var count = 0;

	function increase(){
		return count++;
	}

	function decrease(){
		return count--;
	}

	function reset(){
		count=0;
		return count;
	}
	return {
		"plus":increase,//increase()함수를 반환한다. 마치 변수처럼 썻지만...
		"minus":decrease,
		"reset":reset
	};
})(); 
//counter.plus(), counter.minus(), counter.reset()


//버튼의 클릭에 따라 grid생성하는 코드
// var toggleBtn = $('.toggle-grid');

// toggleBtn.onclick = function() {
// 	toggleGrid('.container', 'grid');
// 	return false;
// };

// function toggleGrid(selector, className) {
// 	$(selector).classList.toggle(className);
// 	// if ( $(selector).classList.contains(className) ) {
// 	// 	$(selector).classList.remove(className);
// 	// } else {
// 	// 	$(selector).classList.add(className);
// 	// }
// }

