var button = selector2('.hamburger');

button.onclick = function(){
	var offcampus_list = selector2('.offcampus');

	var offcampus_key = offcampus_list.classList;
	if(offcampus_key.length>1){
		offcampus_key.remove(offcampus_key[1]);
	}
	else{
		offcampus_key.add('clicked');
	}
};



 selector2('.sub-btn').onclick=function(){
 	var action_key = selector2('.small:nth-child(2)');
 	var f_key = selector2('.small:nth-child(1)');

 	var btn_key = action_key.classList;
 	if(btn_key.length>1){
 		btn_key.remove(btn_key[1]);
 		
 		f_key.style.position = 'static';
 	}
 	else{
 		btn_key.add('btn');
 		f_key.style.position = 'relative';
 		f_key.style.zIndex = '10000';
 		f_key.style.top = '100px';
 	}

}