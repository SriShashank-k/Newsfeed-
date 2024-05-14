// static/newsfeedapp/headline_list.js

$(document).ready(function() {
    $('#search-form').submit(function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();
        
        // Get the form data
        var formData = $(this).serialize();
        
        // Send an AJAX request to the server
        $.ajax({
            type: 'GET',
            url: '/headlines/',  // Use the correct URL for your endpoint
            data: formData,
            success: function(response) {
                // Clear existing headlines
                $('#headlines-container .row').empty();
                
                // Loop through the received headlines and append them to the container
                $.each(response.headlines, function(index, headline) {
                    var html = `
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">${headline.title}</h5>
                                    <div class="card-description">${headline.description}</div>
                                </div>
                                <div class="card-footer">
                                    <small>Source: ${headline.source_name}</small>
                                    <small>Published At: ${headline.published_at}</small>
                                    <a href="${headline.url}" target="_blank" class="btn btn-primary">Read More</a>
                                    <a href="/headlines/${headline.id}/reviews/" class="btn btn-primary">Reviews</a>
                                </div>
                            </div>
                        </div>
                    `;
                    $('#headlines-container .row').append(html);
                });
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
