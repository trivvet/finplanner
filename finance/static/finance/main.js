function expenseAddButton() {
    $('#expenses .list-group-item').hover(
        function() {
            $(this).children('.addExpense').show();
        },
        function() {
            $(this).children('.addExpense').hide();
        }
    );
}

function transactionAddButton() {
    $('#balance .list-group-item').hover(
        function() {
            $(this).find('.addTransaction').show();
        },
        function() {
            if(!$(this).next().hasClass('show')) {
                $(this).find('.addTransaction').hide();
            }
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
    transactionAddButton();
    addExpenseCalendar();
});