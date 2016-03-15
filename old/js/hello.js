$(document).ready(function() {

	hello = ["नमस्ते", "Guten tag", "今日は", "Salam", "Ciao", "Γειά", "nuqneH", "Heus", "你好", "Sveiki", "Hola", "નમસ્તે", "God dag", "االسلام عليكم"];
	var i = 1;
	var max_i = hello.length - 1;

/*
	$("#fuckContent").text(hello[0]);

*/
	function changeHello(index) {
		$("#hello2").text(hello[index]);
	}

	
	setInterval(function(){
		changeHello(i);
		i = (i == max_i) ? 0 : i + 1;
	}, 2000);


});
