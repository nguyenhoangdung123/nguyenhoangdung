function startClick() {
    console.log("Start clicked");
}

var song_container = document.getElementsById('song_container')
song_container.textContent = "Start";
song_container.addEventListener('click', function(e) {
    console.log("Click");
})

var searchBar = document.getElementsById("searchBar");
searchBar.value = "";
searchBar.style.backgroundColor = "Blue";
searchBar.style.color = "Red";

var album = document.getElementsById("album");
var liList = album.getElementsByTagName("li");
console.log(liList);
album.textContent = "" 
var liList = liList[0]
var newLi = document.createElement("li")
newLi