<?php



        header('Content-Type_ application/json');



        $servername = "localhost";

        $username = "root";

        $password = "raspberry";

        $dbname = "projekti";



        // Create connection

        $mysqli = new mysqli($servername, $username, $password, $dbname);




        // Check connection

        if ($mysqli->connect_error) {

                die("EI YHDISTA");

                print "ei yhdistä";

                                                          }


                        $data_points = array();
                        $result = mysqli_query($mysqli,"SELECT * FROM Mittaukset order by id ");

                        while($row = mysqli_fetch_array($result))
                        {        
                            $point = array($row['aika'],$row['kosteus'],$row['latitudeDegree'],$row['latitude'],$row['longitudedegree'],$row['longitude']);
                            array_push($data_points, $point);        
                        }



                        //output the return value of json encode using the echo function.

 
                                echo json_encode($data_points, JSON_NUMERIC_CHECK);
?>
