$(document).ready(function() {
    $('#search').on('submit', () => {
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