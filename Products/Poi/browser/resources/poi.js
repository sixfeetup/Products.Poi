jQuery(function($) {
    $("#archetypes-fieldname-dueDate.error .fieldErrorBox").text("Enter a required due date using the MM/DD/YYYY format.");
    
    // No overlays for IE6
    if (!jQuery.browser.msie ||
        parseInt(jQuery.browser.version, 10) >= 7) {

        // Set up overlays
        $('#poi-login-form').prepOverlay({
            subtype: 'ajax',
            filter: '#content>*',
            formselector: '#content-core > form',
            noform: 'reload',
            closeselector: '[name=form.buttons.cancel]',
        });
    }

    // parse the current querystring
    var qsmap = URI(location).query(true);
    var headers = $('.issue-search-results thead th');
    // map headers to sort types
    var sortheaders = {
        0 : 'id',
        1 : 'sortable_title',
        2 : 'getRelease',
        3 : 'getArea',
        4 : 'getIssueType',
        5 : 'getSeverity',
        6 : 'getResponsibleManager',
        7 : '',
        8 : 'review_state',
    }
    // loop the headers and attach links
    for (var i = 0; i < headers.length; i++) {
        var newuri = URI(location);
        newuri.search(function(data) {
            data.sort_on = sortheaders[i];
            data.sort_order = 'ascending';
        });
        $(headers[i]).wrapInner(function() {
            var newheader = $("<div><a></a></div>");
            if (qsmap.hasOwnProperty('sort_on') && qsmap.sort_on == sortheaders[i]) {
                $(newheader).attr('class','sorted-header');
                if (qsmap.hasOwnProperty('sort_order') && qsmap.sort_order == 'ascending') {
                    newuri.search(function(data) {
                        data.sort_order = 'descending';
                    });
                    $(newheader).append('<img src="arrowUp.png" width="9" height="6" />');
                } else {
                    newuri.search(function(data) {
                        data.sort_order = 'ascending';
                    });
                    $(newheader).append('<img src="arrowDown.png" width="9" height="6" />');
                }
            };
            $('a', newheader).attr('href', newuri);
            return newheader;
        });
    }
});
