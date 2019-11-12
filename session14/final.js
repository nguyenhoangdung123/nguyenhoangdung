a=document.getElementById("song_container")
a.addEventListener("click",function(i){
    var element=i.target
    var div=element.parentNode;
    console.log(div);
})

var delbutton = document.getElementsByClassName("del_button");

for ( var i = 0; i < delbutton.length; i++) {
    var delbutton2 = delbutton [i];
    delbutton2.addEventListener('click', function(e) {
        var del = e.target;
        var div = del.parentNode;
        div.remove();
    });
}
var more1 = document.getElementsByClassName('more_button');
for (var m = 0; m < more1.length; m++) {
    var more2 = more1[m];
    more2.addEventListener('click', function(k) {
        var more = k.target;
        console.log(k.path[1].attributes[1].value);
        console.log(k.path[1].attributes[2].value);
        console.log(k.path[1].attributes[3].value);
    })
)