// https://select2.org/getting-started/basic-usage
// https://datatables.net/manual/installation

var xhr = new XMLHttpRequest();
var url = "https://tinytrader.io/wp-content/themes/ayro-child/";

var market_caps = [
    {id: 1, text: 'Large-Cap'},
    {id: 2, text: 'Mid-Cap'},
    {id: 3, text: 'Small-Cap'},
    {id: 4, text: 'Micro-Cap'}
];

var sectors = [
    {id: 1, text: 'Healthcare'},
    {id: 2, text: 'Technology'},
    {id: 3, text: 'Real Estate'},
    {id: 4, text: 'Industrials'},
    {id: 5, text: 'Consumer Defensive'},
    {id: 6, text: 'Consumer Cyclical'},
    {id: 7, text: 'Financial Services'},
    {id: 8, text: 'Basic Materials'},
    {id: 9, text: 'Energy'},
    {id: 10, text: 'Utilities'},
    {id: 11, text: 'Communication Services'}
];


var screener = jQuery('#stocks').DataTable( {
    dom: 'lBfrtip', //'Blfrtip'
    "scrollX": true,
    buttons: ['csv', 'excel'],
    columns: [
        {data: 'Symbol', title: 'Symbol', className: 'left-align-col'},
        {data: 'Name', title: 'Name', className: 'left-align-col'},
        {data: 'Size', title: 'Size', className: 'left-align-col'},
        {data: 'Sector', title: 'Sector', className: 'left-align-col'},
        //{data: 'Industry', title: 'Industry', className: 'left-align-col'},
        {data: 'Overall', title: 'Overall' },
        {data: 'Value', title: 'Value' },
        {data: 'Growth', title: 'Growth' },
        {data: 'Quality', title: 'Quality' }
    ]
} );

jQuery('#market-cap').select2( {
    placeholder: 'All Market Caps',
    data: market_caps,
    closeOnSelect : false
});

jQuery('#sector').select2( {
    placeholder: 'All Sectors',
    data: sectors,
    closeOnSelect : false
});

xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        
        // parse data from query
        var data = JSON.parse(this.responseText);
        
        screener.rows.add(data).draw();
    
    }
};        

xhr.open("GET", url + "stock-screener.php", true);
xhr.send();


function applyFilters() {
    var size_filter = jQuery('#market-cap').val();
    var sector_filter = jQuery('#sector').val();
    
    /*if (sector_filter === null) {
        //console.log('sector is null');
    }*/
    
    var sector_filters = '';
    if (sector_filter !== null) {
        sector_filters = sector_filter.join("+");
    }
    
    var size_filters = '';
    if (size_filter !== null) {
        size_filters = size_filter.join("+");
    }
    
    //var sectors_filter = '10+11';
    //var sectors_filter = "'"+sector_filter.join("','")+"'";
    
    //console.log(sectors_filter);
    
    var overall_min = document.getElementById("overall_min").value;
    var overall_max = document.getElementById("overall_max").value;
    var value_min = document.getElementById("value_min").value;
    var value_max = document.getElementById("value_max").value;
    var growth_min = document.getElementById("growth_min").value;
    var growth_max = document.getElementById("growth_max").value;
    var quality_min = document.getElementById("quality_min").value;
    var quality_max = document.getElementById("quality_max").value;
    
    //console.log(typeof overall_min);
    
    if (overall_min === '') {
        overall_min = 0;
    }
    if (overall_max === '') {
        overall_max = 100;
    }
    if (value_min === '') {
        value_min = 0;
    }
    if (value_max === '') {
        value_max = 100;
    }
    if (growth_min === '') {
        growth_min = 0;
    }
    if (growth_max === '') {
        growth_max = 100;
    }
    if (quality_min === '') {
        quality_min = 0;
    }
    if (quality_max === '') {
        quality_max = 100;
    }
    
    //console.log(overall_min);
    
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //console.log(this.responseText);
            var data = JSON.parse(this.responseText);
            
            screener.clear();
            screener.rows.add(data).draw();
            
        }
    };
    
    console.log("stock-screener-filter.php?overall_min=" + overall_min + "&overall_max=" + overall_max + "&value_min=" + value_min + "&value_max=" + value_max + "&growth_min=" + growth_min + "&growth_max=" + growth_max + "&quality_min=" + quality_min + "&quality_max=" + quality_max + "&sectors=" + sector_filters + "&size=" + size_filters);
    
    xhr.open("GET", url + "stock-screener-filter.php?overall_min=" + overall_min + "&overall_max=" + overall_max + "&value_min=" + value_min + "&value_max=" + value_max + "&growth_min=" + growth_min + "&growth_max=" + growth_max + "&quality_min=" + quality_min + "&quality_max=" + quality_max + "&sectors=" + sector_filters + "&size=" + size_filters, true);
    xhr.send();
    
}



function resetFilters() {
    jQuery('.select-filter').val('').trigger('change');
    document.getElementById("overall_min").value = 0;
    document.getElementById("overall_max").value = 100;
    document.getElementById("value_min").value = 0;
    document.getElementById("value_max").value = 100;
    document.getElementById("growth_min").value = 0;
    document.getElementById("growth_max").value = 100;
    document.getElementById("quality_min").value = 0;
    document.getElementById("quality_max").value = 100;
}

