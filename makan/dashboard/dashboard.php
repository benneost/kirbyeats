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
           <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>  
           <style> 
                .container { 
                    align: center;
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
           <div align="center" id="chart_container">
            <div style="width:900px;">  
                    <h3 align="center">Dashboard</h3>  
                        <p id="piechart" style="width: 900px; height: 500px;"></p>  
                        <p id="columchart" style="width: 900px; height: 500px;"></p> 
            </div>  
           </div>
      </body>  
 </html> 