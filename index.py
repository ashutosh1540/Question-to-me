# -*- coding: utf-8 -*-
header="""<!DOCTYPE html>
<html lang="en" >
<head>
     <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Randomized Lunches</title>
<style>
@import url(https://fonts.googleapis.com/css?family=Noto+Sans);

 {
	margin: 0;
	padding: 0;
}

#wrap {
	position: absolute;
	top: 0; left: 0; right: 0; bottom: 0;
	background-color: #333;
	overflow: hidden;
}

#popup {
	position: absolute;
	width: 300px;
	height: auto;
	top: 50%; left: 50%;
	margin-left: -150px; margin-top: -100px;

	-webkit-perspective: 800px;
  	-webkit-perspective-origin: 50% 50px;
   perspective: 800px;
   perspective-origin: 50% 50px;
}

.piece {
	background: rgba(95,144,222,0.5);
	float: left;
}

#popup h2 {
	position: absolute;
	text-align: center;
	width: 100%;
	height: 40px;
	top: 50%; margin-top: -20px;
	font-family: 'Noto Sans', sans-serif;
	color: #ccc;
}

.reverse {
	position: absolute;
	top: 30px;
	left: 50%;
	margin-left: -30px;
	font-family: 'Noto Sans', sans-serif;
	color: #ccc;
	cursor: pointer;
}
</style>
</head>

<body>
  <div id="wrap">
  <div id="popup">
  <h2><span></span></h2>
  </div>
</div>
<div class="reverse"><button>Randomize</button></div>
"""
footer_string="""
 <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js' type="text/javascript"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenMax.min.js'type="text/javascript"></script>
<script>
    var pieces = 100,
    speed = 1,
    pieceW =30,
    pieceH = 30;


for (var i = pieces - 1; i >= 0; i--) {
  $('#popup').prepend('<div class="piece" style="width:'+pieceW+'px; height:'+pieceH+'px"></div>');
};

function breakGlass(from){
  if (from === "reverse"){
    $('.piece').each(function(){
      TweenLite.to($(this), speed, {x:0, y:0, rotationX:0, rotationY:0, opacity: 1, z: 0});
      TweenLite.to($('#popup h2'),0.2,{opacity:1, delay: speed});
    });
    return;
  }

  if(!from){
    TweenLite.to($('#popup h1'),0.2,{opacity:0});
  } else {
    TweenLite.from($('#popup h1'),0.5,{opacity:0, delay: speed});
  }

  $('.piece').each(function(){
    var distX = getRandomArbitrary(-250, 250),
        distY = getRandomArbitrary(-250, 250),
        rotY  = getRandomArbitrary(-720, 720),
        rotX  = getRandomArbitrary(-720, 720),
        z = getRandomArbitrary(-500, 500);

    if(!from){
      TweenLite.to($(this), speed, {x:distX, y:distY, rotationX:rotX, rotationY:rotY, opacity: 0, z: z});
    } else {
      TweenLite.from($(this), speed, {x:distX, y:distY, rotationX:rotX, rotationY:rotY, opacity: 0, z: z});
    }
  });
}

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}


$('.piece, h2').click(function(){
  breakGlass();
});
$('.reverse').click(function(){
  breakGlass('reverse');
});

breakGlass(true);
$('button').click(function() {
        $('h2').text(randomEl(four_names))
});

function randomEl(list) {
    const fix=4;
    var i=0, random_list=[];
    while(i<fix){
    	var number=Math.floor(Math.random()*list.length)
      if(random_list.indexOf(number)==-1){
      random_list.push(number);
      i++;
      }
    }
    var final_list= getRandomListItem(random_list,list);
    console.log(random_list);
    console.log(final_list);
    return final_list;
}

function getRandomListItem(random_list,list){
	var final_list=[];
  for(i=0;i<random_list.length;i++){
    var j = Math.floor(Math.random() * list[random_list[i]].length);
    final_list.push(list[random_list[i]][j]);
  }
return final_list;
}


var Admin = ["Rosalinda Natal","Anne Dong","Vivian Lee", "Sangela Lam","Jessica Rovello"];
var Analytics = ["Audley Wilson","Sunny Zhu"];
var Core=["Jim Yang","Patrick Lee","Erik Buchholz","David Or","Tom Rassweiler","Terrance Peng"]
var Editorial=["John Dorn","Ben Widdicombe"]
var Marketing=["Zev Newman","Eric Bogard"]
var PDM=["Samantha Aviles","Katelyn Stanis"]
var Product=["Robert Caliolo","Stanislav Tkachenko","Tatyana Zuger"]
var Sales=["Jeffrey Weinman","George Trusca","Daniel Martin","Sasha Sorokin","Kenny Rosenblatt"]
var four_names = [Admin,Analytics,Core,Editorial,Marketing,PDM,Product,Sales]


$('button').click();
</script>
</body>
</html>
"""