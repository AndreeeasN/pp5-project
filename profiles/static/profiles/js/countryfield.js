// Sets color of country dropdown to gray if set to default
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#7d868f');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#7d868f');
    } else {
        $(this).css('color', '#000');
    }
});