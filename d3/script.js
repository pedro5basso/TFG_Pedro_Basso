function createBubbleChart(error, countries, filedGT, filedclusterGT, fileClusters, combinedClusterFile) {
    
    
    //File filedGT
    var array_photos_dGT = filedGT.map(function(photo){return photo.ID_Photo;});
    var array_clusters_dGT = filedGT.map(function(clust){return clust.ID_Cluster;});
    

    var array_photos_cf = combinedClusterFile.map(function(photo){return photo.ID_Photo;});
    var array_clustersr_cf = combinedClusterFile.map(function(clust){return clust.ID_RCluster;});
    var array_clusterse_cf = combinedClusterFile.map(function(photo){return photo.ID_ECluster;});

    
    
    //File filedclusterGT
    var array_clustnumber_dclusterGT = filedclusterGT.map(function(clust){return clust.Cluster_Number;});
    var array_clustname_dclusterGT = filedclusterGT.map(function(clust){return clust.Cluster_Name;});
    
    //File fileClusters
    var array_photos_Clusters = fileClusters.map(function(photo){return photo.ID_Photo;});
    var array_clust_Clusters = fileClusters.map(function(clust){return clust.ID_Cluster;});

    // console.log("Length Clusters: "+ array_photos_Clusters.length)
    
    F = 0.5;
  

    //colores para los clusters originales
    var dclustersColorsScale = d3.scaleOrdinal()
      .domain(array_clustersr_cf.values()).range(['silver','rosybrown', 'lightcoral','navy', 'maroon', 'red', 'tomato','sienna','peru','darkorange',
                                                  'gold', 'olive', 'yellow','purple', 'yellowgreen', 'darkolivegreen','deeppink', 'lawngreen', 'lightgreen',
                                                  'mediumaquamarine', 'turquoise', 'paleturquoise', 'darkcyan','aqua','deepskyblue', 'steelblue', 
                                                  'dodgerblue', 'blueviolet','magenta', 'mediumvioletred',  'hotpink', 'crimson', 'pink']);

    
    var ClustersColors = d3.scaleOrdinal()
    .domain(array_clusterse_cf.values()).range(['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
                                                '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
                                                '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
                                                '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
                                                '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
                                                '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
                                                '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
                                                '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
                                                '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
                                                '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']);


      

    var width = 1000,
      height = 600;
    var svg,
      circles;

    var forces,
      forceSimulation;


    createSVG();
    createCircles_solution();
    createForces();
    createForceSimulation_solutions();
    addFillListener();
    addGroupingListeners();
    CreateListClusters();


    //Crea el SVG: a partir del id, ancho y largo, y el zoom
    function createSVG() {
        svg = d3.select("#bubble-chart")
          .append("svg")
            .attr("width", width)
            .attr("height", height).call(d3.zoom().on("zoom", function () {
           svg.attr("transform", d3.event.transform)
        })).append("g")

    }    
    

    function ColorsFill() {
        return isChecked("#colors");
    }
    
    function FileFill(){
      return isChecked("#file");
    }
    

    function  isChecked(elementID) {
        return d3.select(elementID).property("checked");
    }
    
    

    function createCircles_solution() {


        circles = svg.selectAll("circle")
          .data(combinedClusterFile)
          .enter()
            .append("circle")
            .attr("r", 10)
            .on("mouseover", function(d) {
              updateCountryInfo(d); //muesstra la info del ciculo: (ejemplo): nombre_país y población
            })
            .on("mouseout", function(d) {
              updateCountryInfo();
            });
        updateCircles(); // para el color de los circulos

        function updateCountryInfo(d) {
            var info = "";
            if (d) {
                info = "PHOTO ID: " + d.ID_Photo + "; CLUSTER ID: " + d.ID_Cluster;
            }

            // d3.select("#country-info").html(info);
        }
    }

   

    //añade color a los círculos
    function updateCircles() {

      if(ColorsFill()){
        circles
          .attr("fill", function(d) {
            return dclustersColorsScale(d.ID_RCluster);
          });

      }
      else{
        circles
        .attr("fill", function(d) {
          return ClustersColors(d.ID_ECluster);
        });
      }

    }
    
    

    function createForces() {
        var forceStrength = 0.05;

        forces = {
          combine:        createCombineForces(),
          solutions:      createSolutionsForces()
        };

    function createCombineForces() {
      return {
        x: d3.forceX(width / 2).strength(forceStrength),
        y: d3.forceY(height / 2).strength(forceStrength)
      };
    }

   

    function createSolutionsForces(){

      var tam = 18;
      var num_columns = 5;
      var num_rows = 0;

      if(tam % num_columns == 0){
        num_rows = tam / num_columns;
        num_rows = parseInt(num_rows);
      }        
      else{
        num_rows = (tam / num_columns) + 1;
        num_rows = parseInt(num_rows);
      }
      

      
      return {
        x: d3.forceX(continentForceX).strength(forceStrength),
        y: d3.forceY(continentForceY).strength(forceStrength)
        
      };

      function continentForceX(d) {

        if(!FileFill()){
          var cluster = d.ID_RCluster;
        }else{
          var cluster = d.ID_ECluster;

        }
        
        // var cluster = d.ID_ECluster;
        var clust_int = parseInt(cluster);

        if (cluster == '1' || clust_int % num_columns == 1) {
          
          return moveRight(width, 1);
        } else if (cluster == '2' || clust_int % num_columns == 2) {
          return moveRight(width, 2);
        } else if (cluster == '3' || clust_int % num_columns == 3) {
          return moveRight(width, 3);
        } else if (cluster == '4' || clust_int % num_columns == 4) {
          return moveRight(width, 4);
        }
        return moveRight(width, 5);
      }

      function continentForceY(d) {

        if(!FileFill()){
          var cluster = d.ID_RCluster;
        }else{
          var cluster = d.ID_ECluster;

        }
        // var cluster = d.ID_ECluster;
        var clust_int = parseInt(cluster);
        

        if (clust_int <= 5) {          
          return moveDown(height,1);
        } else if (clust_int > 5 && clust_int <= 10) {
          return moveDown(height,2);
        } else if (clust_int > 10 && clust_int <= 15) {
          return moveDown(height,3);
        } else if (clust_int > 15 && clust_int <= 20) {
          return moveDown(height,4);
        } else if (clust_int > 20 && clust_int <= 25) {
          return moveDown(height,5);        
        }else if (clust_int > 25 && clust_int <= 30) {
          return moveDown(height,6);        
        }
        return moveDown(height,7);
      }

      function moveRight(dimensionX, iter ){return (dimensionX * ( iter /num_columns));}

      function moveDown(dimensionY, iter){return (dimensionY * ( iter / num_rows));}

    }

    }
    
    

    function createForceSimulation_solutions() {
        forceSimulation = d3.forceSimulation()
          .force("x", forces.combine.x)
          .force("y", forces.combine.y)
          .force("collide", d3.forceCollide(12).strength(F));
        forceSimulation.nodes(combinedClusterFile)
          .on("tick", function() {
            circles
              .attr("cx", function(d) { return d.x; })
              .attr("cy", function(d) { return d.y; });
          });
    }
    
    

    function addFillListener() {
        d3.selectAll('input[name="fill"]')
          .on("change", function() {
            updateCircles();
          });
    }
    
    

    function addGroupingListeners() {
        
        addListener("#combine",         forces.combine);
        addListener("#solutions",       forces.solutions);
        addListener("#file",       forces.solutions);

        function addListener(selector, forces) {
            d3.select(selector).on("click", function() {
                updateForces(forces);
                //togglePopulationAxes(populationGrouping());
            });
        }

        function updateForces(forces) {
            forceSimulation
                .force("x", forces.x)
                .force("y", forces.y)
                .force("collide", d3.forceCollide(12).strength(F))
                .alphaTarget(0.5)
                .restart();
        }    
        
    }


    function CreateListClusters(){


      for(i = 0; i < array_clustnumber_dclusterGT.length; i++){
        var li_element = document.createElement("LI");
        var text = document.createTextNode(array_clustname_dclusterGT[i]);
        li_element.appendChild(text);
        document.getElementById("ClustList").appendChild(li_element);
      }
      

    }

}
