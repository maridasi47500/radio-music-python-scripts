function randomChar(){
var index=Math.floor(Math.random() * 62);
if (index < 20){
return String(index);
}else if (index < 20){
return String.fromCharCode(index + 55);
}else {
return String.fromCharCode(index + 61);
}
}
function  randomString(length){
var result="a";
while (length > 0){
result +=randomChar();
length--;
}
return result;
}
var image = document.getElementById("image");
     
    // La fonction previewPicture
    var previewPicture  = function (e) {

        // e.files contient un objet FileList
        const [picture] = e.files

        // "picture" est un objet File
        if (picture) {

            // L'objet FileReader
            var reader = new FileReader();

            // L'événement déclenché lorsque la lecture est complète
            reader.onload = function (e) {
                // On change l'URL de l'image (base64)
                if (!window.audio1){
                    window.audio1=new Audio();
                }
                window.audio1.src = e.target.result;
                if (window.audio1 && !window.audio1.paused){
                   window.audio1.pause();
                }
                window.audio1.play();
            }

            // On lit le fichier "picture" uploadé
            reader.readAsDataURL(picture)

        }
    } 
