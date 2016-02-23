/*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
문서객체모델을 조작하는 도움을 주는 함수들
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*/

//CSS선택자를 통해서 문서 객체를 선택하는 헬퍼 함수
function selector(selector, parent){

	var els = document.querySelectorAll(selector);
	//삼항식으로 표현가능
	// return els.length === 1? els[0]:els;

	//삼항식을 조건을 2개를 받아서 표현할 수도 있다.
	// return !els ? null : els.length > 1 ? els : els[0];

	//if 문으로  표현
	if (!els){
		return null;
	}
	else if(els.length>1){
		return els;
	}else{
		return els[0];
	}
	// if(els===1){
	// return els[0];
	// }
	// else{
	// 	return els;
	// }

}


//내가 짠 selector2 코드
// function selector2(selector, parent){
	
// 	var els = document.querySelectorAll(selector);

// 	if(!parent){
// 		if (!els){
// 			return null;
// 		}
// 		else if(els.length>1){
// 			return els;
// 		}else{
// 			return els[0];
// 		}
// 	}
// 	else{
// 		var els2 = parent.querySelectorAll(selector);
// 		if (!els2){
// 			return null;
// 		}
// 		else if(els2.length>1){
// 			return els2;
// 		}else{
// 			return els2[0];
// 		}
// 	}
// }

//내가 짠 것보다 효율적으로 짜여진 selector2코드
function selector2(selector, parent){
	//유효성 검사
	//데이터 유형체크
	
	if(parent){
		var els = parent.querySelectorAll(selector);
	}
	else{
		var els = document.querySelectorAll(selector);

	}
	return !els ? null : els.length>1 ? els : els[0];
}


//내가 짠 것보다 효율적으로 짜여진 selector2코드 제 2탄
// function selector2(selector, parent){
// 	if(parent){
// 		var els = parent.querySelectorAll(selector);
// 	}
// 	else{
// 		var els = document.querySelectorAll(selector);

// 	}
// 	return !els ? null : els.length>1 ? els : els[0];
// }





//속성을 설정하는 헬퍼함수
function addAttribute(element, property, value){
	//검사
	//element에 기존에 설정된 property값이 존재하는지 유무파악
	var old_prop = element.getAttribute(property);
	if(old_prop){
		element.setAttribute(property, old_prop + ' ' + value);
	}
	else{

	//존재하지 않으면 값을 설정함
		element.setAttribute(property, value);
	}

	// //설정
	// element.setAttribute(property, value);

}




//데이터 유형 체크
//1. Typeof
// 약점 : 객체와 배열의 데이터 타입을 구분하지 못한다.
//2.instanceof
//데이터 유형 istansof 생성자 함수
//원시데이터의 유형을 체크할 수 없다.
//3.constructor
//데이터(객체)를 생성한 생성자를 체크한다(데이터가 객체가 아니면 오류)
//4.Object.prototype.toString메소드 빌려쓰기(Function.prototype.call)

//데이터 타입을 체크하는 함수를 만들어보자
function isType(data, data_type){
	if(data === undefined || data ===null){
		return data;
	}else{
		return data.constructor === data_type;

	}
	// switch(data.constructor){
	// 	case : 
	// }	
}


function isType2(data, type){
	if(typeof type!=='string'){
		throw new Error('전달된 두번째 인자의 유형은 String형으로 받아져야한다.');
	}
	var _type = Object.prototype.toString.call(data).slice(8, -1).toLowerCase();
	return _type === type;
}

// function clickButton(){
// 	var now = document.
// };