$(document).ready(function(){



    $('[data-toggle="tooltip"]').tooltip({

        placement : 'top'

    });




    $('#example').hide();
    $('#example2').hide();



   // $("#stbutton").click(); //This doesn't work

   var api_url = 'http://localhost:8000/api/books/';

   var main_url = 'http://localhost:8000/api/'

   $("#buildTeam2").on("click", function(){
      console.log($("#formation").val());
      $.ajax({
        url: main_url+'build/',
        contentType: "application/json;charset=utf-8",
        dataType: 'json',
        jsonp : false,
        jsonpCallback: 'jsonCallback',
        cache: 'true',
        data: JSON.stringify({ formation:$("#formation").val(),algo:$("#algoType").val()}),
        type:"POST",
        async:false,
        success: function(data, textStatus, jqXHR){
            var score = data.response.response.score;
            var dat = data.response.response.name;
            res = ""
            table= "<tbody>"
            var data = []
            for (var i = 0; i < dat.length; i++) {
              temp = '<div>'
              new_temp=''
              for (var j = 0; j < dat[i].length;j++)
              {
                temp_new = '<span><a data-toggle="tooltip" title="' + dat[i][j].Name+'"> <img src="' +dat[i][j].Photo+ '" style="'+'margin-top:'+dat[i][j].top+'px;margin-left:'+dat[i][j].left+'px;px;height:80px;width:80px" alt="..." class="img-thumbnail player"></a></span>'
                new_temp+='<span style="'+'margin-left:'+dat[i][j].left+'px; font-weight:bold;">'+ dat[i][j].Name+'</span>'
                temp+=temp_new;
                table+='<tr><td>Tiger Nixon</td><td>System Architect</td><td>Edinburgh</td><td>61</td><td>2011/04/25</td><td>$320,800</td></tr>'
                data.push([dat[i][j].Name,dat[i][j].Position,dat[i][j].Overall,dat[i][j].Nationality,dat[i][j].Club])
              }
//              temp+='<br>'
//              temp+=new_temp
              temp+='</div>'
              res+=temp


          }

//             var data = [];
//        for ( var i=0 ; i<500 ; i++ ) {
//            data.push( [ i, i, i, i, i ] );
//        }
//          table+='</tbody>'
$('#example').show();
            $('#example').DataTable( {
            data:           data,
            deferRender:    true,
            scrollY:        370,
            scrollCollapse: true,
            scroller:       true,
            bDestroy: true,
             bPaginate: false
        } );

          console.log(res)
          $("#red").fadeOut("slow",function() {
            $('#red').empty();
            $('#buildTeamScore').empty();
            $('#buildTeamScore').append('<h1>Team Score</h1><h2>'+score+'</h2>');
          $("#red").append(res);
          $('#red').fadeIn("slow");
          $('#buildTeamScore').show();
        });
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
          console.log("asassa");
          alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
        }
    })
   });



   $("#buildBudgetTeam2").on("click", function(){
    console.log($("#formation").val());
    $.ajax({
      url: main_url+'BuildBudgetTeam/',
      contentType: "application/json;charset=utf-8",
      dataType: 'json',
      jsonp : false,
      jsonpCallback: 'jsonCallback',
      cache: 'true',
      data: JSON.stringify({ formation:$("#formation").val(),algo:$("#algoType").val(),budget:$("#budgetTeam").val()}),
      type:"POST",
      async:false,
      success: function(data, textStatus, jqXHR){
          var score = data.response.response.score;
          var dat = data.response.response.name;
          res = ""
          table= "<tbody>"
          var data = []
          for (var i = 0; i < dat.length; i++) {
            temp = '<div>'
            new_temp=''
            for (var j = 0; j < dat[i].length;j++)
            {
              temp_new = '<span><a data-toggle="tooltip" title="' + dat[i][j].Name+'"> <img src="' +dat[i][j].Photo+ '" style="'+'margin-top:'+dat[i][j].top+'px;margin-left:'+dat[i][j].left+'px;px;height:80px;width:80px" alt="..." class="img-thumbnail player"></a></span>'
              new_temp+='<span style="'+'margin-left:'+dat[i][j].left+'px; font-weight:bold;">'+ dat[i][j].Name+'</span>'
              temp+=temp_new;
              table+='<tr><td>Tiger Nixon</td><td>System Architect</td><td>Edinburgh</td><td>61</td><td>2011/04/25</td><td>$320,800</td></tr>'
              data.push([dat[i][j].Name,dat[i][j].Position,dat[i][j].Overall,dat[i][j].Nationality,dat[i][j].Club])
            }
//              temp+='<br>'
//              temp+=new_temp
            temp+='</div>'
            res+=temp


        }

//             var data = [];
//        for ( var i=0 ; i<500 ; i++ ) {
//            data.push( [ i, i, i, i, i ] );
//        }
//          table+='</tbody>'
$('#example').show();
          $('#example').DataTable( {
          data:           data,
          deferRender:    true,
          scrollY:        370,
          scrollCollapse: true,
          scroller:       true,
          bDestroy: true,
           bPaginate: false
      } );

        console.log(res)
        $("#red").fadeOut("slow",function() {
          $('#red').empty();
          $('#buildTeamScore').empty();
          $('#buildTeamScore').append('<h1>Team Score</h1><h2>'+score+'</h2>');
        $("#red").append(res);
        $('#red').fadeIn("slow");
        $('#buildTeamScore').show();
      });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown){
        console.log("asassa");
        alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
      }
  })
 });


   $("#manageTeam").on("click", function(){
    console.log($("#formation").val());
    $('#sub').empty()
    $.ajax({
      url: main_url+'manage/',
      contentType: "application/json;charset=utf-8",
      dataType: 'json',
      jsonp : false,
      jsonpCallback: 'jsonCallback',
      cache: 'true',
      data: JSON.stringify({ formation:$("#clubFormation").val(),club:$("#clubSelection").val(),nation: $("#nationalitySection").val(),algo:$("#clubAlgoType").val()}),
      type:"POST",
      async:false,
      success: function(data, textStatus, jqXHR){
          var dat = data.response.response.name;
          var score = data.response.response.score;
          res = ""
             var datas = []
            for (var i = 0; i < dat.length; i++) {
              temp = '<div>'
              new_temp=''
              for (var j = 0; j < dat[i].length;j++)
              {
                temp_new = '<span><a data-toggle="tooltip" title="' + dat[i][j].Name+'"> <img src="' +dat[i][j].Photo+ '" style="'+'margin-top:'+dat[i][j].top+'px;margin-left:'+dat[i][j].left+'px;px;height:80px;width:80px" alt="..." class="img-thumbnail player"></a></span>'
                new_temp+='<span style="'+'margin-left:'+dat[i][j].left+'px; font-weight:bold;">'+ dat[i][j].Name+'</span>'
                temp+=temp_new;
                datas.push([dat[i][j].Name,dat[i][j].Position,dat[i][j].Overall,dat[i][j].Nationality,dat[i][j].Club])
              }
//              temp+='<br>'
//              temp+=new_temp
              temp+='</div>'
              res+=temp


          }
$('#example2').show();
           $('#example2').DataTable( {
            data:           datas,
            deferRender:    true,
            scrollY:        370,
            scrollCollapse: true,
            scroller:       true,
            bDestroy: true,
             bPaginate: false
        } );

        var players = data.response.response.players;
          sub = '<option value="" selected>Choose a Substitute</option> '
          for (var k = 0;k<players.length;k++)
          {
            sub+= '<option value="' + players[k]+'">' + players[k] + '</option> '
          }

          $('#substitutePlayer').empty();
          $("#substitutePlayer").append(sub);
        console.log(res)
        $("#manageTeamContent").fadeOut("slow",function() {
          $('#manageTeamContent').empty();
          $('#manageTeamScore').empty();
        $("#manageTeamContent").append(res);
        $('#manageTeamContent').fadeIn("slow");
        $('#manageTeamScore').append('<h1>Team Score</h1><h2>'+score+'</h2>');
        $('#manageTeamScore').show()

      });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown){
        console.log("asassa");
        alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
      }
  })
 });


 $("#substituteTeam").on("click", function(){
  console.log($("#substitutePlayer").val());
  var subb = $("#substitutePlayer").val()
  var playersList = [];

  console.log(playersList)
  $("#substitutePlayer option").each(function(){
    console.log("adadaa");
    if($(this).val() != "")
    {
      playersList.push($(this).val());
    }
  })
  console.log(playersList);
  $.ajax({
    url: main_url+'substitute/',
    contentType: "application/json;charset=utf-8",
    dataType: 'json',
    jsonp : false,
    jsonpCallback: 'jsonCallback',
    cache: 'true',
    data: JSON.stringify({ formation:$("#clubFormation").val(),club:$("#clubSelection").val(),'substitute':$("#substitutePlayer").val(),'players':playersList,'substitute':$("#substitutePlayer").val(),nation: $("#nationalitySection").val()}),
    type:"POST",
    async:false,
    success: function(data, textStatus, jqXHR){
        var dat = data.response.response.name;
        var score = data.response.response.score;
        res = ""
var datas = []
            for (var i = 0; i < dat.length; i++) {
              temp = '<div>'
              new_temp=''
              for (var j = 0; j < dat[i].length;j++)
              {
                if(dat[i][j].sub_flag == 0)
                {
                temp_new = '<span><a data-toggle="tooltip" title="' + dat[i][j].Name+'"> <img src="' +dat[i][j].Photo+ '" style="'+'margin-top:'+dat[i][j].top+'px;margin-left:'+dat[i][j].left+'px;px;height:80px;width:80px" alt="..." class="img-thumbnail player"></a></span>'
                new_temp+='<span style="'+'margin-left:'+dat[i][j].left+'px; font-weight:bold;">'+ dat[i][j].Name+'</span>'
                }
                else
                {
                  temp_new = '<span><a data-toggle="tooltip" title="' + dat[i][j].Name+'"> <img src="' +dat[i][j].Photo+ '" style="'+'margin-top:'+dat[i][j].top+'px;margin-left:'+dat[i][j].left+'px;px;height:80px;width:80px;border:4px solid" alt="..." class="img-thumbnail player"></a></span>'
                new_temp+='<span style="'+'margin-left:'+dat[i][j].left+'px; font-weight:bold;">'+ dat[i][j].Name+'</span>'
                }
                temp+=temp_new;
                datas.push([dat[i][j].Name,dat[i][j].Position,dat[i][j].Overall,dat[i][j].Nationality,dat[i][j].Club])
              }
//              temp+='<br>'
//              temp+=new_temp

              temp+='</div>'
              res+=temp


          }
          $('#sub').empty()
          $('#sub').append('<span>'+subb+' -> '+data.response.response.substitute+'</span>')

$('#example2').show();
           $('#example2').DataTable( {
            data:           datas,
            deferRender:    true,
            scrollY:        370,
//                        scrollX:        100,

            scrollCollapse: true,
            scroller:       true,
            bDestroy: true,
             bPaginate: false
        } );

      var players = data.response.response.players;
        sub = '<option value="" selected>Choose a Substitute</option> '
        for (var k = 0;k<players.length;k++)
        {
          sub+= '<option value="' + players[k]+'">' + players[k] + '</option> '
        }

        $('#substitutePlayer').empty();
        $("#substitutePlayer").append(sub);
      console.log(res)
      $("#manageTeamContent").fadeOut("slow",function() {
        $('#manageTeamContent').empty();
        $('#manageTeamScore').empty();
      $("#manageTeamContent").append(res);
      $('#manageTeamContent').fadeIn("slow");
       $('#manageTeamScore').append('<h1>Team Score</h1><h2>'+score+'</h2>');
        $('#manageTeamScore').show()
    });
    },
    error: function(XMLHttpRequest, textStatus, errorThrown){
      console.log("asassa");
      alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
    }
})
});





$("#analytics").on("change", function(){
  console.log($("#analytics").val());

  if($("#analytics").val() == "")
  {
    return
  }
  $.ajax({
    url: main_url+'analytics/',
    contentType: "application/json;charset=utf-8",
    dataType: 'json',
    jsonp : false,
    jsonpCallback: 'jsonCallback',
    cache: 'true',
    data: JSON.stringify({ chartType:$("#analytics").val()}),
    type:"POST",
    async:false,
    success: function(data, textStatus, jqXHR){

    if($("#analytics").val() == "ov")
    {
        var dat = data.response.response.name;
        var chart_type = data.response.response.type;
        var boxNumber = 30;
        var boxColor = [];
        // var allColors = numeric.linspace(0, 360, boxNumber);
        var data = [];
        // for( var i = 0; i < boxNumber;  i++ ){
        //   var result = 'hsl('+ allColors[i] +',50%'+',50%)';
        //   boxColor.push(result);
        // }
        for (var i = 0; i < dat.length; i++) {
          var trace1 = {
            x: dat[i].values,
            type: chart_type,
            name: dat[i].name
          };
          data.push(trace1)
        }

        var layout = {
          title: $("#analytics option:selected").text()
        };
        Plotly.newPlot('myChart', data, layout);
        }


    if($("#analytics").val() == "op")
    {
        var dat = data.response.response.name;
        var chart_type = data.response.response.type;

//        var boxNumber = 30;
//        var boxColor = [];
        // var allColors = numeric.linspace(0, 360, boxNumber);
        var data = [{
        // for( var i = 0; i < boxNumber;  i++ ){
        //   var result = 'hsl('+ allColors[i] +',50%'+',50%)';
        //   boxColor.push(result);
        // }

            values: dat.values,
            type: chart_type,
            labels: dat.name


        }];

//        var layout = {
//              height: 900,
//              width: 600
//         };

var layout = {
          title: $("#analytics option:selected").text()
        };



        Plotly.newPlot('myChart', data, layout);
        }
    if($("#analytics").val() == "age")
    {
        var dat = data.response.response.name;
        var chart_type = data.response.response.type;

//        var boxNumber = 30;
//        var boxColor = [];
        // var allColors = numeric.linspace(0, 360, boxNumber);
        var data = [{
        // for( var i = 0; i < boxNumber;  i++ ){
        //   var result = 'hsl('+ allColors[i] +',50%'+',50%)';
        //   boxColor.push(result);
        // }

            y: dat.values,
            type: chart_type,
            x: dat.name


        }];

//        var layout = {
//              height: 900,
//              width: 600
//         };

var layout = {
          title: $("#analytics option:selected").text()
        };

        Plotly.newPlot('myChart', data, layout);
        }
        if($("#analytics").val() == "att" || $("#analytics").val()=='mid' ||  $("#analytics").val()=='def')
    {
        var dat = data.response.response.name;
        var chart_type = data.response.response.type;
//        var boxNumber = 30;
//        var boxColor = [];
        // var allColors = numeric.linspace(0, 360, boxNumber);
        var data = [];
        // for( var i = 0; i < boxNumber;  i++ ){
        //   var result = 'hsl('+ allColors[i] +',50%'+',50%)';
        //   boxColor.push(result);
        // }
        for (var i = 0; i < dat.length; i++) {
          var trace1 = {

            type: chart_type,
            r:dat[i].values,
            theta:['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                'Marking', 'StandingTackle', 'SlidingTackle'],
            fill: 'toself',
            name: dat[i].name
          };
          data.push(trace1)
        }

       layout = {
            polar: {
            radialaxis: {
            visible: true,
            range: [15, 100]
                }
            }
        }

        Plotly.newPlot('myChart', data, layout);
        }
//

// var y0=[],y1=[]
// for ( i = 0; i < 50; i ++) 
// {
// 	y0[i] = Math.random();
// 	y1[i] = Math.random();
// }

// var trace1 = {
//   y: y0,
//   type: 'box'
// };

// var trace2 = {
//   y: y1,
//   type: 'box'
// };

// var data = [trace1, trace2];

// Plotly.newPlot('myChart', data, {}, {showSendToCloud: true});
    },
    error: function(XMLHttpRequest, textStatus, errorThrown){
      console.log("asassa");
      alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
    }
})
});

});
