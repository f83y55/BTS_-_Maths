/*
 * Game
 *
 */

var isPlaying = false ;
var vquestion = 0 ;
var maximum = 10;
var time = 10;

var config = document.getElementById("submit");
config.onclick = function() {
    let vars = {};
    let parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,
                           function(m,key,value) {vars[key] = value;});
    if (vars["maximum"] != undefined) {
        maximum = parseInt(vars["maximum"], 10);
    }
    if (vars["time"] != undefined) {
        time = parseInt(vars["time"], 10);
    }
}

function fPlay() {
    if (isPlaying) {
        if (answer == vquestion){
            fScoreUp();
        }
        else {
            fScoreDown();
        }
        vquestion = fQuestion(maximum);
        fTimeReset(time);
        fAnswerReset()
    }
    else {
        isPlaying = true ;
        vquestion = fQuestion(maximum);
        fTimeReset(time);
        fAnswerReset();
        fScoreReset();
        timer = setInterval(fTimeDown, 1000);
    }
}

/*
 * Score
 *
 */

var score = 0;
var total = 0;
var vdisp_score = document.getElementById("disp_score");

function fScoreReset() {
    score = 0 ;
    total = 0 ;
    vdisp_score.innerHTML = "";
}

function fScoreUp() {
    score += 1;
    total += 1;
    vdisp_score.innerHTML = score.toString(10)+'/'+total.toString(10)+' ['+(Math.floor(100*score/total)).toString(10)+'%]';
}
function fScoreDown() {
    total += 1;
    vdisp_score.innerHTML = score.toString(10)+'/'+total.toString(10)+' ['+(Math.floor(100*score/total)).toString(10)+'%]';
}


/*
 * Time
 *
 */

var timer;
var stop = document.getElementById("time");
stop.onclick = function() {
    if (isPlaying) {
        clearInterval(timer);
        total = 0;
        score = 0;
        isPlaying = false;
        vdisp_time.innerHTML = "STOP"; 
    }
}

var vdisp_time = document.getElementById("disp_time");
function fTimeReset(time) {
    vdisp_time.innerHTML = '•'.repeat(time);
}
function fTimeDown() {
    if (vdisp_time.innerHTML.length>0) {
        vdisp_time.innerHTML = vdisp_time.innerHTML.slice(0, -1);
    }
    else {
        fPlay();
    }
}

/*
 * Question
 *
 */

var vdisp_question = document.getElementById("disp_question");
function getRandomInt(max) {
  return Math.floor(Math.random() * (max-1) +2);
}
function fQuestion(max) {
  let a = getRandomInt(max);
  let b = getRandomInt(max);
  vdisp_question.innerHTML = a.toString(10)+'×'+b.toString(10);
  return a*b;
}


/* 
 * Keyboard
 *
 */
var disp_answer_max = 4;

var answer = 0;
var vdisp_answer = document.getElementById("disp_answer");
function fAnswerReset() {
    vdisp_answer.innerHTML = "";
    answer = 0 ;
}

var vkey7 = document.getElementById("key7");
vkey7.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='7';
        answer = answer*10 + 7 ;
    }
}
var vkey8 = document.getElementById("key8");
vkey8.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='8';
        answer = answer*10 + 8 ;
    }
}
var vkey9 = document.getElementById("key9");
vkey9.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='9';
        answer = answer*10 + 9 ;
    }
}
var vkey4 = document.getElementById("key4");
vkey4.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='4';
        answer = answer*10 + 4 ;
    }
}
var vkey5 = document.getElementById("key5");
vkey5.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='5';
        answer = answer*10 + 5 ;
    }
}
var vkey6 = document.getElementById("key6");
vkey6.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='6';
        answer = answer*10 + 6 ;
    }
}
var vkey1 = document.getElementById("key1");
vkey1.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='1';
        answer = answer*10 + 1 ;
    }
}
var vkey2 = document.getElementById("key2");
vkey2.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='2';
        answer = answer*10 + 2 ;
    }
}
var vkey3 = document.getElementById("key3");
vkey3.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='3';
        answer = answer*10 + 3 ;
    }
}
var vkey0 = document.getElementById("key0");
vkey0.onclick = function() {
    if (vdisp_answer.innerHTML.length < disp_answer_max) {
        vdisp_answer.innerHTML +='0';
        answer = answer*10 ;
    }
}
var vkeyBackspace = document.getElementById("keyBackspace");
vkeyBackspace.onclick = function() {
    vdisp_answer.innerHTML = '';
    answer = 0 ;
}
var vkeyReturn = document.getElementById("keyReturn");
vkeyReturn.onclick = function() {
    fPlay();
}

