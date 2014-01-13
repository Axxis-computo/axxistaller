
    $(document).ready(function(){
        $('.borrar-manual').click(function(){
            var manual_id = $(this).attr('id');
            var manual_titulo = $(this).data('name');
            $('#modal_name').text(manual_titulo);
            $('#modal_id').val(manual_id);
            $('#myModal').modal('show');
            return false;
        });
    });
    
    $(document).ready(function(){
        $('.borrar-ent').click(function(){
            var ent_id = $(this).attr('id');
            var ent_titulo = $(this).data('name');
            $('#modal_name').text(ent_titulo);
            $('#modal_id').val(ent_id);
            $('#myModal').modal('show');
            return false;
        });
    });