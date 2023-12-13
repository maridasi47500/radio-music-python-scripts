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
	console.log(r);
if (r){
window.location=r;
}

},
xhr: function () {
          var myXhr = $.ajaxSettings.xhr();
          if (myXhr.upload) {
	           //For handling the progress of the upload
		           myXhr.upload.addEventListener('progress', function (e) {
		                     if (e.lengthComputable) {
		                                 $('progress').show();
		                                 $('progress').attr({
		                                               value: e.loaded,
		                                                             max: e.total,
		                                                                         });
		                                                                                   }
		                                                                                           }, false);
		                                                                                                 }
		                                                                                                       return myXhr;
		                                                                                                           }
		                                                                                                             });
return false;
});
});
