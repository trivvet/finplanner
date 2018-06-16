function expenseAddButton() {
    $('#expenses .list-group-item').hover(
        function() {
            $(this).children('.addExpense').toggle();
        },
        function() {
            $(this).children('.addExpense').toggle();
        }
    );
}

function addExpenseCalendar() {
    var today = new Date();
    $('.datetimepicker').datetimepicker({
        locale: 'uk',
        format: "YYYY-MM-DD",
        maxDate: today,
        buttons: {
            showToday: true,
            showClose: true
        }
    });
}

$(document).ready(function() {
    expenseAddButton();
    addExpenseCalendar();
});