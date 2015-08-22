

        function getErrorMessageIfExists(dataObj, type){
                var errorMessage = null;
                for(i=0; i<dataObj.length; i++){
                        if(dataObj[i].error != null && dataObj[i].error != undefined &&
                                        dataObj[i].error != ''){
                                errorMessage = dataObj[i].error;
                                break;
                        }
                }
                return errorMessage;
        }

        function countSentimentType(dataObj, type){
                var count = 0;
                for(i=0; i<dataObj.length; i++){
                        if(dataObj[i].type == type) count++;
                }
                return count;
        }

        function createPanelHtml(dataObj){
                var positiveCount = countSentimentType(dataObj, 'positive');
                var neutralCount = countSentimentType(dataObj, 'neutral');
                var negativeCount = countSentimentType(dataObj, 'negative');
                var total = positiveCount + neutralCount + negativeCount;
                var panelHtml = '';
                panelHtml += '<br/><div class="pure-g">';
                panelHtml += '<div class="pure-u-1-3" style="color:red; text-align:center"><b>NEGATIVES:</b> ' + negativeCount + '/' + total + '</div>';
                panelHtml += '<div class="pure-u-1-3" style="text-align:center"><b>NEUTRALS:</b> ' + neutralCount + '/' + total + '</div>';
                panelHtml += '<div class="pure-u-1-3" style="color:green; text-align:center"><b>POSITIVES:</b> ' + positiveCount + '/' + total + '</div>';
                panelHtml += '</div><br/>';
                return panelHtml;
        }


        function createTableHtml(dataObj){
                var tableHtml = '';
                tableHtml += '<table class="pure-table pure-table-bordered">';
                tableHtml += '<thead><tr><th>Tweet Text</th><th>Sentiment</th><th>Score</th></tr></thead>';
                tableHtml += '<tbody>';
                for(i=0; i<dataObj.length; i++){
                                
                        //add tweet text
                        tableHtml += '<tr><td>' + dataObj[i].text + '</td>';
                        
                        //add sentiment result type
                        if(dataObj[i].type == 'positive'){
                                tableHtml += '<td style="color:green">';
                        } else if(dataObj[i].type == 'negative'){
                                tableHtml += '<td style="color:red">';
                        } else{
                                tableHtml += '<td>';
                        }
                        tableHtml += '<b>' + dataObj[i].type.toUpperCase() + '</b></td>';
                
                        //add sentiment result score
                        tableHtml += '<td>';
                        if(dataObj[i].score != null && dataObj[i].score != ''){
                                tableHtml += dataObj[i].score;
                        }
                        else{
                                tableHtml += '-';
                        }
                        tableHtml += '</td></tr>';
                }
                        
                        
                tableHtml += '</tbody>';
                tableHtml += '</table>';
                return tableHtml;
        }




	function doSearchButtonClick(){
                        var searchText = $("#searchField").val();
                        if(searchText == null || searchText == ''){
                                alert("Search term cannot be empty!");
                                return;
                        }
                        $('#resultSummaryDiv').html('');
                        $('#resultDiv').html('');
                        
                        $.ajax({
                                url: "/search/term?q=" + searchText, 
                                success: function(data, status){
                                    var dataObj = JSON.parse(data);
                                
                                    //handle errors
                                    var errorMessage = getErrorMessageIfExists(dataObj);
                                    if(errorMessage != null){
                                        window.alert("Error ocurred.\nMaybe the alchemyApi request quota was reached?\n" + errorMessage);
                                        return;
                                    }
                                
                                    //add result summary
                                    var panelHtml = createPanelHtml(dataObj);
                                    $('#resultSummaryDiv').html(panelHtml);

                                    //add result table
                                    var tableHtml = createTableHtml(dataObj);
                                    $('#resultDiv').html(tableHtml);
                                },
                                beforeSend: function() { $('#wait').show(); },
                                complete: function() { $('#wait').hide(); }
                        });

	}


	function searchByTermOnReadyFunction(){
		$("#doSearchBtn").click(doSearchButtonClick);
	}

