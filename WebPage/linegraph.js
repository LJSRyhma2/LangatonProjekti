$(document).ready(function() {

                       $.getJSON("test.php", function (result) {
                           // console.log(result);


                            var time = []; 
                            var humidity = []; 
                            var temperature = []; 


                            for (var i in result){
                                time.push(result[i].slice(0,1).toString());
                                humidity.push(result[i].slice(1,2).toString());
                                
                                }
                                


                                var Data = {
                                    labels : time,
                                    datasets : [{
                                        label: "Kosteus",
                                        fill: false,
                                        lineTension: 0.2,
                                        backgroundColor: "rgba(59, 89, 152, 0.75)",
                                        borderColor: "rgba(59, 89, 152, 1)",
                                        pointHoverBackgroundColor: "rgba(59, 89, 152, 1)",
                                        pointHoverBorderColor: "rgba(59, 89, 152, 1)",
                                        data : humidity
                                    }


                                    ]
                                };


                            var ctx = $("#mycanvas");
                            var myNewChart = new Chart(ctx , {
                                    type: "line",
                                    data: Data,
                                });

     });

	window.initMap = function(){

		            $.getJSON("test.php", function (result1) {
                            console.log(result1);
    
    
                            var latDeg = []; 
                            var latitude = []; 
                            var longDeg = []; 
                            var longitude = []; 
    
                            for (var i in result1){
                                latDeg.push(result1[i].slice(2,3).toString());
                                latitude.push(result1[i].slice(3,4).toString());
                                longDeg.push(result1[i].slice(4,5).toString());
                                longitude.push(result1[i].slice(5,6).toString());
        


                                }


			var last_NorthDeg =  latDeg[latDeg.length - 1]; 
                        var last_Northlat =  latitude[latitude.length - 1];

                        var last_eastDeg =  longDeg[longDeg.length - 1];
                        var last_eastLong = longitude[longitude.length - 1];


    
                        var  northDeg= parseFloat(last_NorthDeg);
			var  northLat= parseFloat(last_Northlat);

                        var  eastDEG = parseFloat(last_eastDeg);
			var  eastLo =  parseFloat(last_eastLong);
				

	
				

			console.log(northDeg, northLat);
			console.log(eastDEG, eastLo);
    
				

					var locNow = {lat: northDeg,northLat, lng: eastDEG,eastLo};
        				
					


					var map = new google.maps.Map(document.getElementById('map'), {
         					zoom: 11,
          					center: locNow
        				});

        				var marker = new google.maps.Marker({
          					position: locNow,
				        	map: map
				        });
						
				
					

        			});
				

		};


 });


     
