(function(){

	var UA = {};

	var ua = navigator.userAgent;
	
	if(window.opera){
		UA.opera = window.opera.version();

		if(/Presto\/([\d.]+)/.test(ua)){
			UA.presto = RegExp.$1;
		}
		
	} else if(/MSIE ([\d.]+);/.test(ua)){
		UA.ie = RegExp.$1;
		
		if(/Trident\/([\d.]+)/.test(ua)){
			UA.trident = RegExp.$1;
		} 
		
	} else if(/AppleWebKit\/([\d.]+)/.test(ua)){
		UA.webkit = RegExp.$1;
		
		if(/Chrome\/([\d.]+)/.test(ua)){
			UA.chrome = RegExp.$1;
		} else if(/Version\/([\d.]+)/.test(ua)){
			UA.safari = RegExp.$1;
		}
		
	} else if(/Firefox\/([\d.]+)/.test(ua)){
		UA.firefox = RegExp.$1;
		
		if(/rv:([\d.]+)/.test(ua)){
			UA.gecko = RegExp.$1;
		}
	}
	
	if (/(?:Android);?[\s\/]+([\d.]+)?/.test(ua)) {
		UA.android = RegExp.$1;
	} else if (/(?:iPad|iPod|iPhone).*OS\s([\d_]+)/.test(ua)) {
		UA.ios = RegExp.$1.replace(/_/g, '.');
	}
	
	UA.mobile = UA.android || UA.ios;
	
	for(var p in UA){
		UA[p] = parseFloat(UA[p]);
	}
	
	window.UA = UA;
})();