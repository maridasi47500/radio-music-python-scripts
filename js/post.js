$(function(){
$("form").on('submit', function () {
$.ajax({url: $(this)[0].action,
    data: new FormData($(this)[0]),
    cache: false,
    contentType: false,
    processData: false,
type:"post",
success:function(data){
var r=data.redirect;
if (r){
window.location=r;
}

}});
return false;
});
});
