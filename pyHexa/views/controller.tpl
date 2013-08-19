<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
    <head>
        <title>Hexa Controller</title>
		
		<script>		
			function go_direction_ajax(direction)
			{
				var http = new XMLHttpRequest();
				var url = "/" + direction;
				
				http.open("GET", url, true);
				http.onreadystatechange = function() {}
				http.send(null);
			}
		</script>
    </head>
    <body>
		<img src="/static/controller.png" alt="Controller" usemap="#controllermap">
		
		<map name="controllermap">
		  <area shape="rect" coords="165, 210, 269, 314" alt="forward"  nohref onclick="go_direction_ajax('go/forward')">
		  <area shape="rect" coords="165, 520, 269, 413" alt="backward" nohref onclick="go_direction_ajax('go/backward')">
		  <area shape="rect" coords="48,  314, 165, 413" alt="left"     nohref onclick="go_direction_ajax('go/left')">
		  <area shape="rect" coords="48,  269, 371, 413" alt="right"    nohref onclick="go_direction_ajax('go/right')">
		  
		  <area shape="rect" coords="170,  13, 312,  63" alt="home"     nohref onclick="go_direction_ajax('go/start')">
		</map>
    </body>
</html>
