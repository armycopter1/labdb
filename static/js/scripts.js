/*!
* Start Bootstrap - Simple Sidebar v6.0.5 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
});

// This produces the experiment description detail when the '+' button is clicked on the open experiments page table.
function detailFormatter(index, row) {
    var html = []
    $.each(row, function (key, value) {
        if(key=="exp_descrip") {
            html.push('<p><b>Experiment Description: </b> ' + value + '</p>')
        }
        if(key=="ship_request_method") {
            html.push('<p><b>Ship Request Method: </b> ' + value + '</p>')
        }
        if(key=="supplied_material") {
            html.push('<p><b>Supplied Material: </b> ' + value + '</p>')
        }
        if(key=="match_type") {
            html.push('<p><b>Match Type: </b> ' + value + '</p>')
        }
        if(key=="pantone") {
            html.push('<p><b>Pantone: </b> ' + value + '</p>')
        }
        if(key=="sample_size") {
            html.push('<p><b>Sample Size: </b> ' + value + '</p>')
        }
        if(key=="other_reg") {
            html.push('<p><b>Other Reg: </b> ' + value + '</p>')
        }
        if(key=="cure_type") {
            html.push('<p><b>Cure Type: </b> ' + value + '</p>')
        }
        if(key=="cure_temp") {
            html.push('<p><b>Cure Temp: </b> ' + value + '</p>')
        }
        if(key=="pc_time") {
            html.push('<p><b>Post Cure Time: </b> ' + value + '</p>')
        }
        if(key=="pc_temp") {
            html.push('<p><b>Post Cure Temp: </b> ' + value + '</p>')
        }
        if(key=="lastname") {
            html.push('<p><b>Requestor: </b> ' + value + '</p>')
        }
    })
    return html.join('')
}

// This produces the experiment description detail when the '+' button is clicked on the open experiments page table.
function detailFormatterHist(index, row) {
    var html = []
    $.each(row, function (key, value) {
        if(key=="exp_descrip") {
            html.push('<p><b>Experiment Description: </b> ' + value + '</p>')
        }
        if(key=="matched") {
            html.push('<p><b>Matched?: </b> ' + value + '</p>')
        }
        if(key=="pphr_percent") {
            html.push('<p><b>PPHR or Percent: </b> ' + value + '</p>')
        }
        if(key=="com_number") {
            html.push('<p><b>Commercial Number</b> ' + value + '</p>')
        }
        if(key=="total_hours") {
            html.push('<p><b>Lab Hours: </b> ' + value + '</p>')
        }
        if(key=="shipping_company") {
            html.push('<p><b>Shipping Method: </b> ' + value + '</p>')
        }
        if(key=="ship_tracking") {
            html.push('<p><b>Tracking Number: </b> ' + value + '</p>')
        }
        if(key=="notes") {
            html.push('<p><b>Notes: </b> ' + value + '</p>')
        }
        if(key=="lastname") {
            html.push('<p><b>Requestor: </b> ' + value + '</p>')
        }
    })
    return html.join('')
}



// This produces the experiment description detail when the '+' button is clicked on the open stds page table.
function detailFormatter2(index, row) {
    var html = []
    $.each(row, function (key, value) {
        if(key=="std_descrip") {
            html.push('<p><b>Experiment Description: </b> ' + value + '</p>')
        }
    })
    return html.join('')
}

