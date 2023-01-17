$(document).ready(function() {
    $('#example').DataTable( {
        responsive: true,
        columnDefs: [
            { responsivePriority: 1, targets: 0 },
            { responsivePriority: 2, targets: -1 }
        ],
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.1/i18n/pt-BR.json'
        }
    } );
} );