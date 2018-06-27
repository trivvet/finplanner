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
    var monthDate = $('#month_date').text();
    if (monthDate) {
        monthDate = new Date(monthDate);
    }
    $('.datetimepicker').datetimepicker({
        locale: 'uk',
        format: "YYYY-MM-DD",
        useCurrent: false,
        date: monthDate,
        maxDate: today,
        buttons: {
            showToday: true,
            showClose: true
        }
    });
}

function addMonthesCalendar() {
    $('#datetimepicker4').datetimepicker({
        locale: 'uk',
        format: "YYYY-MM"
    });
}

$(document).ready(function() {
    expenseAddButton();
    transactionAddButton();
    addExpenseCalendar();
    addMonthesCalendar();
});