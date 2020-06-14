$(document).ready(function() {
    $('#theme-select').on('change', () => {
        $.ajax({
            url: '/set',
            data: {
                'theme': $('#theme-select').val()
            },
            method: 'POST'
        }).done(() => {
            location.reload()
        })
    })
});