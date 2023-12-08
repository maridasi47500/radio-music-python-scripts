$(function(){

function init() {
	"use strict";
        
        var minduration=0;
	var posSlider = document.getElementById("myRange");
	var volSlider = document.getElementById("myVol");
	var audio1=new Audio();
	$(posSlider).on('input',function (e) {
            e.preventDefault();
		audio1.currentTime = posSlider.value;
	});
	$(posSlider).on('change',function (e) {

            e.preventDefault();
		audio1.currentTime = posSlider.value;
	});
        /*$.ajax({url:"/songs/jouerunechanson",success:function(data){
        audio1=new Audio('/uploads/'+data.song.filename);*/

	var goBut = document.getElementById("goButton");
	var playPic = "/img/play.png";
	var pausePic = "/img/pause.png";
        var paspremier=false;
	var mydata;
                    audio1.src="/uploads/shakira-acrostico.mp3";
               if (audio1 && !audio1.paused){
                    audio1.pause();
               }
                    audio1.play();
			goBut.src = pausePic;
       
	$(goBut).click(function (e) {
            e.preventDefault();
		if (!audio1 || audio1.paused) {
                     $.ajax({type:"get",url:"/songs/playmusique",data:{play:1},
        success:function(data){
console.log(data);
        }
        });
			
                        $.ajax({url:"/songs/jouerunechanson",success:function(data){
//console.log(JSON.stringify(data)+"azertyui"+(data.song));
                            minduration=audio1.duration;
                            mydata=data;
                            if(data.song){
var xxxxx=randomString(10);
                    audio1.src=('/uploads/'+data.song.filename);

                    if (!paspremier){
                    audio1.addEventListener('loadedmetadata',setMax);

                    $.ajax({url:"/passage",data:{title: audio1.src},success:function(data){
console.log("heure de passage ")
                        }});

        function setMax() {
            //e.preventDefault();
            console.log(Number(audio1.duration));
		posSlider.max= audio1.duration; posSlider.setAttribute('min', 0);
                //console.log(minduration);
                audio1.currentTime = 0;
                   if (!audio.paused){
                    audio1.pause();
                   }

                audio1.play();
	};
                audio1.addEventListener("timeupdate", voirmusique);
	function voirmusique() {
            console.log("tyui CURRENTIME",audio1.currentTime);
		//posSlider.value = 0;
		posSlider.value = audio1.currentTime;
		if (audio1.ended || audio1.max === audio1.duration) {
                    $.ajax({url:"/songs/jouerunechanson",success:function(data){
//console.log(JSON.stringify(data))
                                    minduration=audio1.duration;
                                    mydata=data;
                                    if(data.song){
                            audio1.src='/uploads/'+data.song.filename;
                                    }else{


			audio1.pause();
                            audio1=new Audio();
			goBut.src = playPic;
                                    }
                        }});
			posSlider.value = 0;
			audio1.currentTime = 0;
			//goBut.src = playPic;
			//audio1.pause();
		}
	};
        paspremier=true;
        }
                   if (!audio.paused){
                    audio1.pause();
                   }
                    audio1.play();
			goBut.src = pausePic;
                            }else{
                       //console.log("none");
                    audio1.pause();
                    audio1=new Audio();
                            }
                }});
            
                        
		} else {
			audio1.pause();
			audio1=new Audio();
			goBut.src = playPic;
                          $.ajax({type:"get",url:"/songs/playmusique",data:{play:0},
        success:function(data){
console.log(data);
        }
        });
		}
	});




	$(volSlider).on('input',function (e) {
            e.preventDefault();
		audio1.volume = volSlider.value / 100;
                $.ajax({type:"get",url:"/songs/playmusique1",data:{myvol: $("#myVol").val()},
        success:function(data){
console.log(data);
        }
        });
	});
     
        $.ajax({url:"/songs/musique",
        success:function(data){
            if (data.ok === "1"){
                //console.log(data.myvol)
                $(goBut).click();
                $("#myVol")[0].value=(parseInt(data.myvol));
                audio1.volume = volSlider.value / 100;
            }
        }
        });
            /*}});*/
};

init();

});
