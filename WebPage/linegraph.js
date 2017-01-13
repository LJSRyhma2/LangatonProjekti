$(document).ready(function() {

                       $.getJSON("test.php", function (result) {
                            console.log(result);


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
 });


     
