<?php  
 ### Display the popular restaurants 
 $connect = mysqli_connect("localhost", "root", "root", "esd-order");  
 $query = "SELECT restaurantName, count(*) as number FROM `order` GROUP BY restaurantName"; 
 $result = mysqli_query($connect, $query);   

 ?>  
 <!DOCTYPE html>  
 <html>  
      <head>  
           <title>Dashboard</title> 
           <meta name="viewport" content="width=device-width, initial-scale=1">
          <!--===============================================================================================-->	
            <link rel="icon" type="css/Table_Responsive_v2/image/png" href="css/Table_Responsive_v2/images/icons/favicon.ico"/>
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/vendor/bootstrap/css/bootstrap.min.css">
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/vendor/animate/animate.css">
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/vendor/select2/select2.min.css">
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/vendor/perfect-scrollbar/perfect-scrollbar.css">
          <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/css/util.css">
            <link rel="stylesheet" type="text/css" href="css/Table_Responsive_v2/css/main.css">
          <!--===============================================================================================--> 
           <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>  
           <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
           <style> 
                .container { 
                    align: center;
                }
                body {
                  background-color: pink;
                }
                .button4 {
                  border: 1px solid #555555;
                  background-color: white;
                  border: none;
                  color: black;
                  padding: 16px 32px;
                  text-align: center;
                  text-decoration: none;
                  display: inline-block;
                  font-size: 16px;
                  margin: 4px 2px;
                  transition-duration: 0.4s;
                  cursor: pointer;
                } 
                .button4 {
                    transition-duration: 0.4s;
                }
                .button4:hover {
                    background-color:pink; 
                    color: white;
                }
           </style>
           <script type="text/javascript">  
           google.charts.load('current', {'packages':['corechart']});  
           google.charts.setOnLoadCallback(drawChart);

           
           function drawChart()  
           {  
                var data = google.visualization.arrayToDataTable([  
                          ['Restaurant Name', 'Number'],  
                          <?php  
                          while($row = mysqli_fetch_array($result))  
                          {  
                               echo "['".$row["restaurantName"]."', ".$row["number"]."],";  
                          }  
                          ?>  
                     ]);  
                var options = {  
                      title: 'Popularity of Restaurants',  
                      //is3D:true,  
                      pieHole: 0.4  
                     };  
                var chart = new google.visualization.PieChart(document.getElementById('piechart'));  
                chart.draw(data, options);  
           }  
           </script>  

           <?php
            ### Display the number of orders within the months
            $connect = mysqli_connect("localhost", "root", "root", "esd-order");  
            $query1 = "SELECT EXTRACT(MONTH FROM created) as month, count(*) as number from `order` GROUP BY month"; 
            $result1 = mysqli_query($connect, $query1);  
           ?>
          <script type="text/javascript">  
           google.charts.load('current', {'packages':['corechart']});  
           google.charts.setOnLoadCallback(drawChart2);  

           function drawChart2()  
           {  
            var data = google.visualization.arrayToDataTable([  
                          ['Restaurant Name', 'Number'],  
                          <?php  
                          while($row = mysqli_fetch_array($result1))  
                          { 
                              if ($row["month"] == "1") {
                                echo "['"."January"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "2") {
                                echo "['"."February"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "3") {
                                echo "['"."March"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "4") {
                                echo "['"."April"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "5") {
                                echo "['"."May"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "6") {
                                echo "['"."June"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "7") {
                                echo "['"."July"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "8") {
                                echo "['"."August"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "9") {
                                echo "['"."September"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "10") {
                                echo "['"."October"."', ".$row["number"]."],";  
                              } else if ($row["month"] == "11") {
                                echo "['"."November"."', ".$row["number"]."],";  
                              } else {
                                echo "['"."December"."', ".$row["number"]."],";  
                              }
                               
                          }  
                          ?>  
                     ]);  
                var options = {  
                      title: 'Peak Period',  
                      //is3D:true,  
                      pieHole: 0.4  
                     };  
                var chart = new google.visualization.ColumnChart(document.getElementById('columchart'));  
                chart.draw(data, options);  
           }  
           </script>  

      </head>  
      <body>  
           <br /><br />  
           <javascript>
              <button style = "padding-left:100px;" class = "fa fa-home" onclick="window.location.href='./restaurant.html'">Back to Home</button>
            </javascript>
           <div align="center" id="chart_container">
            <div style="width:900px;">  
                    <h2 align="center">Dashboard</h2>  
                    <br>
                        <p id="piechart" style="width: 900px; height: 500px;"></p>  
                        <p id="columchart" style="width: 900px; height: 500px;"></p> 
            </div>  
           </div>
      </body>  
 </html> 