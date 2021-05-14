

$(document).ready(function() {
	var table = $('#example').DataTable( {
		responsive: {
			details: {
				renderer: function ( api, rowIdx, columns ) {
                  console.log(columns);
					var data = $.map( columns, function ( col, i ) {
						return col.hidden ?
							'<tr data-dt-row="'+col.rowIndex+'" data-dt-column="'+col.columnIndex+'">'+
								'<td>'+col.title+':'+'</td> '+
								'<td>'+col.data+'</td>'+
							'</tr>' :
							'';
					} ).join('');
 
					return data ?$('<table/>').append( data ) :false;
				}
			} 
        }
	} );// end of DataTable
	
	// 
	 $('#example').on('click', 'tr.odd>td, tr.even>td', function (e) { 
		 e.preventDefault(); 
       var id = $(table.cell(this).index()).attr('class');
		var col = table.cell(this).index().columnVisible;
		var row = table.cell(this).index().row;
       
		//alert("CLICK: " + $(this).parent().html().trim());
		console.log("cellID: " + id + " rowIDX: " + row + " colIDX: " + col);
		//alert("CLICK");
	 });
//                            
} );
