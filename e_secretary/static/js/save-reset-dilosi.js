var dilosi = [];
$("#submit-button").ready(function(){
    $("#submit-button").on("click",function(){
        var length = $("#table-dilosi tbody tr").length;
        rows = $("#table-dilosi").children("tbody").children("tr");
        for(i=0 ; i< length; i++){
            dilosi.push(rows.eq(i).find("td:eq(0)").text());
        }
        $.ajax({
            method: "POST",
            url: "",
            data: {"dilosi[]" : dilosi},
            success: function(data){
                alert("Δήλωση Επιτυχής");
            },
            error: function(data){
                alert("Δήλωση Ανεπιτυχής");
            }
        });
    });
});
$("#clear-button").ready(function(){
    $("#clear-button").on("click",function(){
        sessionStorage.clear();
        $("#table-dilosi tbody").empty();
        dilosi = [];
        $.ajax({
            method: "POST",
            url: "",
            data: {"dilosi[]" : dilosi},
            success: function(data){
                alert("Καθαρισμός Επιτυχής");
            },
            error: function(data){
                alert("Καθαρισμός Ανεπιτυχής");
            }
        });
    });
});