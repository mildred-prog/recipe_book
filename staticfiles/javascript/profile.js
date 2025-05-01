/* globals $ */

// Initialize Summernote editors
$(document).ready(function () {
    // Initialize ingredients editor if it exists
    if ($('#ingredients').length) {
        $('#ingredients').summernote({
            placeholder: 'List the ingredients...',
            tabsize: 2,
            height: 150,
            toolbar: [
              ['style', ['style']],
              ['font', ['bold', 'underline', 'clear']],
              ['color', ['color']],
              ['para', ['ul', 'ol', 'paragraph']],
              ['table', ['table']],
              ['insert', ['link']],
              ['view', ['help']]
            ]
        });
    }

    // Initialize instructions editor if it exists
    if ($('#instructions').length) {
        $('#instructions').summernote({
            placeholder: 'Describe the cooking instructions...',
            tabsize: 2,
            height: 150,
            toolbar: [
              ['style', ['style']],
              ['font', ['bold', 'underline', 'clear']],
              ['color', ['color']],
              ['para', ['ul', 'ol', 'paragraph']],
              ['table', ['table']],
              ['insert', ['link']],
              ['view', ['help']]
            ]
        });
    }

    // Initialize toast notifications
    $('.toast').toast('show');

    // Profile Modal Functionality
    const modal = document.getElementById("myModal");
    const btn = document.getElementById("myBtn");
    const span = document.getElementsByClassName("close")[0];

    // Open modal when edit button is clicked
    if (btn) {
        btn.onclick = function() {
            console.log("Edit button clicked");
            if (modal) {
                modal.style.display = "block";
            }
        };
    }

    // Close modal when X is clicked
    if (span) {
        span.onclick = function() {
            if (modal) {
                modal.style.display = "none";
            }
        };
    }

    // Close modal when clicking outside
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
}); 