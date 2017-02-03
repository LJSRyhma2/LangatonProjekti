$(document).ready(function() {

                       $.getJSON("test.php", function (result) {
                           // console.log(result);


                            var time = []; 
                            var humidity = []; 
                            var temperature = []; 


                            for (var i in result){
                                time.push(result[i].slice(0,1).toString());
                                temperature.push(result[i].slice(1,2).toString());
                                humidity.push(result[i].slice(2,3).toString());
                                
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
                                    },

                                    {
                                        label: "Lämpötila",
                                        fill: false,
                                        lineTension: 0.2,
                                        backgroundColor: "rgba(29, 202, 255, 0.75)",
                                        borderColor: "rgba(29, 202, 255, 1)",
                                        pointHoverBackgroundColor: "rgba(29, 202, 255, 1)",
                                        pointHoverBorderColor: "rgba(29, 202, 255, 1)",
                                        data: temperature
                                    }

                                    ]
                                };


                            var ctx = $("#mycanvas");
                            var myNewChart = new Chart(ctx , {
                                    type: "line",
                                    data: Data,
                                });

     });

	function gmap(){

		            $.getJSON("test.php", function (result1) {
                            console.log(result1);
    
    
                            var latDeg = []; 
                            var latitude = []; 
                            var longDeg = []; 
                            var longitude = []; 
    
                            for (var i in result1){
                                latDeg.push(result1[i].slice(3,4).toString());
                                latitude.push(result1[i].slice(4,5).toString());
                                longDeg.push(result1[i].slice(5,6).toString());
                                longitude.push(result1[i].slice(6,7).toString());
                                        }
    
                        var  north = latDeg.pop() + latitude.pop();
                        var  east = longDeg.pop() + longitude.pop();
    
                        console.log(north);
                        console.debug(east);
    
				

				      
        				var locNow = {lat: north, lng: east};
        					var map = new google.maps.Map(document.getElementById('map'), {
         					zoom: 4,
          					center: locNow
        				});

        				var marker = new google.maps.Marker({
          					position: locNow,
				        	map: map
				        });
						
				
					

        			});
				

		};


 });


     
