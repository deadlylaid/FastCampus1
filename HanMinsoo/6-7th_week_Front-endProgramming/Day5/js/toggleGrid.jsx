#target photoshop
/*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
포토샵을 타겟으로한 jsx
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*/

/*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
선택한 레이어를 토글해준다(show/hide)

1.레이어 페널의 레어어 중에서 첫번째 레이어를 선택
2. 선택된 레이어에 visible상태(state)를 체크합니다.
3. visible상태라면 감추고(눈감기기)
4. 그렇지 않으면 visible상태로 (눈 띄우기)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*/

// 현재 사용자가 열어 놓고 있는 document
var first_layer = app.activeDocument.layers[0];//그룹도 레이어로 본다.
first_layer.visible = !first_layer.visible//상태의 반전값을 다시 대입한다.


// if(first_layer.visible){
// 	first_layer.visible = false;

// }
// else{
// 	first_layer.visible=true;
// }