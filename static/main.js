$(function(){
	$("#codetocolor").ajaxForm({
		beforeSubmit: function(){},
		success: function(data){
			$("div#codecolored").empty();
			$("div#codecolored").append(data);
			$("#pastecode").val("");
			var file = $("#uploadcodefile");
			file.after(file.clone().val(""));
			file.remove();
		}
	});	
	$("#tabs").tabs();
	$("li#share>a").click(function(event){
		$.getJSON('/filelist.json', function(jsondata){
			$("div#codefilelist>p").empty();
			var dataAppended="<br /><ul>";
			for(var key in jsondata){
				var val = jsondata[key];
				dataAppended += '<li>'+val+'</li><br />';
			}
			$("div#codefilelist>p").append(dataAppended+'</ul>');
		});
	});
	$("div#codefilelist>p>ul>li").live('click',function(event){
		var filename = $(this)[0].innerText;
		$.post("/getfilecontent",{codefilename: filename}, function(data){
			$("div#codefilecontent").empty().append(filename).append(data);
			});
		});
})
