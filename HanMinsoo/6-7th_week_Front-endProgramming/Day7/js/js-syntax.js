//new 를 강제시키는 생성자 함수 제작

function Monster(name, type){
	if(this.constructor !==Monster){
		return new Monster(name, type);
		// throw error("새로운 객체를 생성하고 싶다면 var 변수 = new Monster로 선언 해 주셔야합니다.")
	}
	// this.name = name;
	// this.type = type;
}
//프로토타입 객체 확장
// Monster.prototype = {
// 	'crying' : function(){ return this.name + '울부짖다.';},
// 	'runnig' : function(){ return this.name + '달리다.';},
// 	'sleeping' : function(){ return this.name + '잠을자다.';},
// 	'telltype' : function(){ return this.name + '의 유형은 ' + this.type + '이다.';}
// };



Monster.prototype.crying = function(){
	return this.name + "울부짖다.";
};
Monster.prototype.runnig = function(){
	return this.name + "달리다.";
};

Monster.prototype.sleeping = function(){
	return this.name + "잠을 자다.";
};
//일반함수
Monster.prototype.telltype = function(){
	return this.name + '의 유형은 ' + this.type + '이다.';
};

function ExtendMonster(name, type){
	if(this === window){
		return new ExtendMonster(name, type);
	}
	this.name=name;
	this.type = type;
}
ExtendMonster.prototype = new Monster();


Monster();

new Monster();